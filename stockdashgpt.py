import streamlit as st
import pandas as pd
import mplfinance as mpf

st.set_page_config(page_title="Gold Price Chart", layout="wide")
st.title("Visualisasi Harga Emas")

uploaded_file = st.file_uploader("Upload file Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Membaca file Excel
        df = pd.read_excel(uploaded_file)

       # Pastikan kolom 'Tanggal' dalam datetime & jadikan index
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])
        df = df.set_index('Tanggal')

        # Ambil tanggal minimum dan maksimum dari data
        min_date = df.index.min().date()
        max_date = df.index.max().date()

        # Input tanggal awal dan akhir, otomatis dari range data
        d = st.date_input('Tanggal Awal', value=min_date, min_value=min_date, max_value=max_date)
        d2 = st.date_input('Tanggal Akhir', value=max_date, min_value=min_date, max_value=max_date)

        # Filter berdasarkan index yang sudah berupa datetime64
        df = df[(df.index >= pd.to_datetime(d)) & (df.index <= pd.to_datetime(d2))]

        # Menampilkan data
        st.subheader("📊 Data Harga Emas")
        st.dataframe(df)

        # Buat chart dan simpan sebagai gambar sementara
        st.subheader("📉 Candlestick Chart dengan MA (4 hari)")
        fig, axlist = mpf.plot(
            df,
            type='candle',
            style='starsandstripes',
            mav=(10,21),
            mavcolors=['#FFA500','#FF0000'],
            ylabel='Harga',
            returnfig=True
            
        )

        # Tampilkan chart di Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi error saat memproses file: {e}")

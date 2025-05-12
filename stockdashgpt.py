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

        # Menampilkan data
        st.subheader("📊 Data Harga Emas")
        st.dataframe(df)

        # Pastikan kolom 'Tanggal' dalam datetime & jadikan index
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])
        df = df.set_index('Tanggal')

        # # Hitung Moving Average (4 hari)
        # df['MA4'] = df['Close'].rolling(window=4).mean()

        # Buat chart dan simpan sebagai gambar sementara
        st.subheader("📉 Candlestick Chart dengan MA (4 hari)")
        fig, axlist = mpf.plot(
            df,
            type='candle',
            style='starsandstripes',
            mav=(4),
            mavcolors=['#FFA500'],
            ylabel='Harga',
            returnfig=True
            
        )

        # Tampilkan chart di Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi error saat memproses file: {e}")

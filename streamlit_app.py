import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Visualisasi Tema Daerah & Nama Angkatan PK-264")

csv_url = "https://raw.githubusercontent.com/soleh-hukumline/pk264/main/Ide%20Tema%20dan%20Nama%20Angkatan%20PK-264.csv"
df = pd.read_csv(csv_url)

# Cek kolom asli (debug)
st.write("📦 Kolom dari CSV:", df.columns.tolist())

# Rename kolom panjang jadi lebih pendek dan konsisten
df = df.rename(columns={
    "Tema Angkatan (Mengambil tema kedaerahan/budaya Indonesia contoh : Papua Barat Daya, dari pihak LPDP diharapkan daerah sumatera/sulawesi)": "Tema Daerah",
    "Nama Angkatan (Maksimal terdiri dari 2 kata dan menggunakan Bahasa Indonesia atau Bahasa Daerah)": "Nama Angkatan",
    "Arti dan filosofi Nama Angkatan": "Filosofi"
})

# Ambil hanya kolom yang relevan
df = df[["Tema Daerah", "Nama Angkatan", "Filosofi"]].dropna()

# Sunburst chart
fig = px.sunburst(
    df,
    path=["Tema Daerah", "Nama Angkatan"],
    values=[1] * len(df),
    color="Tema Daerah",
    title="Sebaran Tema Daerah dan Nama Angkatan PK-264"
)
st.plotly_chart(fig, use_container_width=True)

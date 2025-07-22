import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Visualisasi Tema Daerah & Nama Angkatan PK-264")

# Raw CSV dari GitHub
csv_url = "https://raw.githubusercontent.com/soleh-hukumline/pk264/main/Ide%20Tema%20dan%20Nama%20Angkatan%20PK-264.csv"

# Baca CSV
df = pd.read_csv(csv_url)

# Tampilkan nama kolom asli (debug)
st.write("📦 Kolom dari CSV:", df.columns.tolist())

# Ubah nama kolom biar lebih konsisten
df = df.rename(columns={
    "Tema Angkatan": "Tema Daerah",
    "Nama Angkatan": "Nama Angkatan",
    "Arti dan filosofi Nama Angkatan": "Filosofi"
})

df = df[["Tema Daerah", "Nama Angkatan", "Filosofi"]].dropna()

# Sunburst Chart
fig = px.sunburst(
    df,
    path=["Tema Daerah", "Nama Angkatan"],
    values=[1] * len(df),
    color="Tema Daerah",
    title="Sebaran Tema Daerah dan Nama Angkatan PK-264"
)
st.plotly_chart(fig, use_container_width=True)

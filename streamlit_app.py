import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Tema Daerah & Nama Angkatan PK-264")

csv_url = "https://raw.githubusercontent.com/soleh-hukumline/pk264/main/Ide%20Tema%20dan%20Nama%20Angkatan%20PK-264.csv"
df = pd.read_csv(csv_url)

# Rename kolom
df = df.rename(columns={
    "Tema Angkatan (Mengambil tema kedaerahan/budaya Indonesia contoh : Papua Barat Daya, dari pihak LPDP diharapkan daerah sumatera/sulawesi)": "Tema Daerah",
    "Nama Angkatan (Maksimal terdiri dari 2 kata dan menggunakan Bahasa Indonesia atau Bahasa Daerah)": "Nama Angkatan",
    "Arti dan filosofi Nama Angkatan": "Filosofi"
})
df = df[["Tema Daerah", "Nama Angkatan", "Filosofi"]].dropna()

# Filter Tema Daerah
tema_terpilih = st.multiselect(
    "🎯 Pilih Tema Daerah yang ingin ditampilkan:",
    options=df["Tema Daerah"].unique(),
    default=df["Tema Daerah"].unique()
)
df_filtered = df[df["Tema Daerah"].isin(tema_terpilih)]

# Sunburst chart besar & interaktif
fig = px.sunburst(
    df_filtered,
    path=["Tema Daerah", "Nama Angkatan"],
    values=[1] * len(df_filtered),
    color="Tema Daerah",
    title="Sebaran Tema Daerah dan Nama Angkatan PK-264",
    hover_data=["Filosofi"],
    width=950,
    height=950
)

st.plotly_chart(fig, use_container_width=True)

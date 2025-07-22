import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Visualisasi Tema Daerah & Nama Angkatan PK-264")

# ✅ Ganti dengan link CSV dari Google Sheets kamu
sheet_url = "https://docs.google.com/spreadsheets/d/1LtUlhadMhWbaKFR0GVxLP_3tTn9p9FGhVNM4tUNicng/edit?usp=sharing"

# 👇 Ini baca langsung datamu dari Google Sheets
df = pd.read_csv(sheet_url)

# (Opsional) Ubah nama kolom jika perlu
df.columns = ["Tema Daerah", "Nama Angkatan", "Filosofi"]
df = df.dropna()

# 🎯 Visualisasi Sunburst Chart
fig = px.sunburst(
    df,
    path=["Tema Daerah", "Nama Angkatan"],
    values=[1]*len(df),
    color="Tema Daerah",
    title="Sebaran Tema Daerah dan Nama Angkatan PK-264"
)
st.plotly_chart(fig, use_container_width=True)

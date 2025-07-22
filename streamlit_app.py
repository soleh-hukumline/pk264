import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Visualisasi Tema Daerah & Nama Angkatan PK-264")

# ✅ Link CSV Google Sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1LtUlhadMhWbaKFR0GVxLP_3tTn9p9FGhVNM4tUNicng/export?format=csv&gid=0"

# 👇 Baca data dari Sheet
df = pd.read_csv(sheet_url)

# Rename kolom kalau perlu
df.columns = ["Tema Daerah", "Nama Angkatan", "Filosofi"]
df = df.dropna()

# Sunburst Chart
fig = px.sunburst(
    df,
    path=["Tema Daerah", "Nama Angkatan"],
    values=[1]*len(df),
    color="Tema Daerah",
    title="Sebaran Tema Daerah dan Nama Angkatan PK-264"
)
st.plotly_chart(fig, use_container_width=True)

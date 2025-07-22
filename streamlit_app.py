import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from io import StringIO

st.set_page_config(layout="wide")
st.title("📊 Visualisasi Tema Daerah & Nama Angkatan PK-264")

# Google Sheets CSV export link
sheet_url = "https://docs.google.com/spreadsheets/d/1LtUlhadMhWbaKFR0GVxLP_3tTn9p9FGhVNM4tUNicng/export?format=csv&gid=0"

# Fix: Fetch manually then load with pandas
response = requests.get(sheet_url)
response.raise_for_status()
csv_data = StringIO(response.text)
df = pd.read_csv(csv_data)

# Pilih kolom yang diperlukan
df = df[["Tema Angkatan", "Nama Angkatan", "Arti dan filosofi Nama Angkatan"]]
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

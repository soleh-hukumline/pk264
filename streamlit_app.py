import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Dashboard Tema Daerah & Nama Angkatan PK-264")

# Ambil data dari Google Sheets (CSV URL)
sheet_url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv"
df = pd.read_csv(sheet_url)
df.columns = ["Tema Daerah", "Nama Angkatan", "Filosofi"]
df = df.dropna()

fig = px.sunburst(df, path=["Tema Daerah", "Nama Angkatan"], values=[1]*len(df),
                  color="Tema Daerah", title="Sunburst Tema PK-264")
st.plotly_chart(fig, use_container_width=True)

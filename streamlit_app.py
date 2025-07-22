import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Tema Daerah & Nama Angkatan PK-264")

# ✅ CSV dari GitHub RAW
csv_url = "https://raw.githubusercontent.com/soleh-hukumline/pk264/main/Ide%20Tema%20dan%20Nama%20Angkatan%20PK-264.csv"

# Baca CSV dari GitHub
df = pd.read_csv(csv_url)

# (Opsional) Rename kolom jika perlu
df.columns = ["Tema Daerah", "Nama Angkatan", "Filosofi"]
df = df.dropna()

# 🎯 Sunburst Chart
fig = px.sunburst(
    df,
    path=["Tema Daerah", "Nama Angkatan"],
    values=[1] * len(df),
    color="Tema Daerah",
    title="Sebaran Tema Daerah dan Nama Angkatan PK-264"
)

st.plotly_chart(fig, use_container_width=True)

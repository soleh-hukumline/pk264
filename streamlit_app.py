import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")

# Rename kolom agar seragam
df = df[[
    "Tema Angkatan (Mengambil tema kedaerahan/budaya Indonesia contoh : Papua Barat Daya, dari pihak LPDP diharapkan daerah sumatera/sulawesi)",
    "Nama Angkatan (Maksimal terdiri dari 2 kata dan menggunakan Bahasa Indonesia atau Bahasa Daerah)",
    "Arti dan filosofi Nama Angkatan"
]]
df.columns = ["Tema Daerah", "Nama Angkatan", "Filosofi"]
df = df.dropna()

st.set_page_config(layout="wide")
st.title("📦 Katalog Ide Angkatan PK-264")

# 🔍 Fitur Pencarian
query = st.text_input("Cari berdasarkan nama angkatan atau filosofi:", "").lower()
if query:
    df = df[df.apply(lambda row: query in row["Nama Angkatan"].lower() or query in row["Filosofi"].lower(), axis=1)]

# 🗺️ Tampilkan per tema
for tema in sorted(df["Tema Daerah"].unique()):
    subset = df[df["Tema Daerah"] == tema].reset_index(drop=True)
    if subset.empty:
        continue

    st.markdown(f"## 🗺️ {tema}")
    for i in range(0, len(subset), 5):
        cols = st.columns(5)
        for j, col in enumerate(cols):
            if i + j < len(subset):
                nama = subset.iloc[i + j]["Nama Angkatan"]
                filosofi = subset.iloc[i + j]["Filosofi"]

                with col:
                    st.markdown(f"""
                        <div style='background-color:#f9f9f9; padding:12px; border-radius:10px; 
                                    height:230px; overflow-y:auto; box-shadow:0 0 5px rgba(0,0,0,0.1);'>
                            <strong>{nama}</strong><br>
                            <div style='font-size:13px; margin-top:5px; color:#444; font-style:italic;'>{filosofi}</div>
                        </div>
                    """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd

# Baca file
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")

# Bersihkan dan rename kolom
df = df[[
    "Tema Angkatan (Mengambil tema kedaerahan/budaya Indonesia contoh : Papua Barat Daya, dari pihak LPDP diharapkan daerah sumatera/sulawesi)",
    "Nama Angkatan (Maksimal terdiri dari 2 kata dan menggunakan Bahasa Indonesia atau Bahasa Daerah)",
    "Arti dan filosofi Nama Angkatan"
]]
df.columns = ["Tema Daerah", "Nama Angkatan", "Filosofi"]
df = df.dropna()

# Judul
st.title("📦 Katalog Ide Angkatan PK-264")

# Loop per tema → tampilkan dalam grid 3 kolom
for tema in df["Tema Daerah"].unique():
    st.markdown(f"## 🗺️ {tema}")

    # Ambil subset
    subset = df[df["Tema Daerah"] == tema]
    cols = st.columns(3)

    for i, (_, row) in enumerate(subset.iterrows()):
        with cols[i % 3]:
            st.markdown(f"""
            <div style='border:1px solid #ccc; padding:12px; border-radius:8px; margin:5px; background-color:#f9f9f9'>
            <strong>{row['Nama Angkatan']}</strong><br>
            <em>{row['Filosofi']}</em>
            </div>
            """, unsafe_allow_html=True)

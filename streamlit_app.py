import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Ide Angkatan PK-264")

# Baca file CSV lokal (karena deploy dari GitHub/Streamlit Cloud)
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")

# Ubah nama kolom agar mudah diakses
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan", "Tema Angkatan",
    "Nama Angkatan", "Filosofi"
]

# Hapus baris kosong
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan", "Filosofi"])

# Kelompokkan berdasarkan Tema Angkatan
for tema, group in df.groupby("Tema Angkatan"):
    st.markdown(f"### 🗺️ {tema}")
    
    cols = st.columns(5)  # max 5 kolom per baris
    
    for i, (_, row) in enumerate(group.iterrows()):
        with cols[i % 5]:
            st.markdown(
                f"""<div style="background-color:#f9f9f9;padding:10px;border-radius:8px;min-height:150px">
                <strong>{row['Nama Angkatan']}</strong><br>
                <span style='font-size: 13px'>{row['Filosofi']}</span>
                </div>""",
                unsafe_allow_html=True
            )

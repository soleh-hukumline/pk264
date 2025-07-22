import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Ide Angkatan PK-264")

# Baca data CSV
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")

# Ganti nama kolom agar mudah diakses
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan", "Tema Angkatan",
    "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan", "Filosofi"])

# CSS custom biar lebih rapi
st.markdown("""
    <style>
    .card {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        min-height: 160px;
    }
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Loop berdasarkan Tema Angkatan
for tema, group in df.groupby("Tema Angkatan"):
    st.markdown(f"<h3>📍 {tema}</h3>", unsafe_allow_html=True)
    html = '<div class="grid">'
    for _, row in group.iterrows():
        html += f"""
        <div class="card">
            <strong>{row['Nama Angkatan']}</strong><br>
            <small>{row['Filosofi']}</small>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

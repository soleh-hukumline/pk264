import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Nama Angkatan PK-264")

# Baca data CSV
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan", "Tema Angkatan",
    "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Nama Angkatan", "Filosofi", "Tema Angkatan"])

# CSS layout grid
st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 1px 1px 4px rgba(0,0,0,0.05);
        font-size: 0.9rem;
    }
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Group by "Nama Angkatan"
for nama_angkatan, group in df.groupby("Nama Angkatan"):
    st.markdown(f"### 🏷️ {nama_angkatan}")
    html = '<div class="grid">'
    for _, row in group.iterrows():
        html += f"""
        <div class="card">
            <b>{row['Nama Lengkap']} ({row['Panggilan']})</b><br>
            <i><u>{row['Tema Angkatan']}</u></i><br>
            <small>{row['Filosofi']}</small>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

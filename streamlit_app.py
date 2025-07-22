import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.markdown("<h1>📦 Katalog Nama Angkatan PK-264</h1>", unsafe_allow_html=True)

# Load and clean data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan",
    "Tema Angkatan", "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Nama Angkatan", "Tema Angkatan"])

# CSS Styling
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    .card {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.2s ease-in-out;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
    }
    .card h3 {
        margin: 0.5rem 0 0.2rem 0;
        font-size: 1rem;
    }
    .card p {
        margin: 0;
        font-size: 0.85rem;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Grid render
html = '<div class="grid-container">'
for _, row in df.iterrows():
    nama = row["Nama Angkatan"].strip()
    tema = row["Tema Angkatan"].strip()
    filosofi = row["Filosofi"].strip().replace('"', '&quot;')
    html += f"""
    <div class="card" title="{filosofi}">
        <h3>🔥 {nama}</h3>
        <p>{tema}</p>
    </div>
    """
html += "</div>"

st.markdown(html, unsafe_allow_html=True)

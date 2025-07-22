import streamlit as st
import pandas as pd
import random

st.set_page_config(layout="wide")
st.markdown("<h1>📦 Katalog Nama Angkatan PK-264</h1>", unsafe_allow_html=True)

# URL Google Sheet (versi CSV)
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRXUdBLq2fv1iX_DFISjLfrKZhmui7SQzYC-2lvohTKSaOKRyQOdl05sdgg45O3wBsqSZXq8BiWgW8i/pub?gid=496735747&single=true&output=csv"

# Load data
df = pd.read_csv(csv_url)
df.columns = [
    "Timestamp", "Nama Lengkap", "Nama Panggilan", 
    "Tema Angkatan", "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Nama Angkatan", "Tema Angkatan", "Filosofi"])

# Warna latar per card (acak)
bg_colors = [
    "#FFFAF0", "#F0FFF4", "#F0F8FF", "#FFF5F5", "#F5F5DC",
    "#FAFAD2", "#F5FFFA", "#FDF5E6", "#F0FFFF", "#FFF0F5",
    "#E6E6FA", "#FFEFD5", "#F5DEB3", "#E0FFFF", "#FBEFFB"
]
random.shuffle(bg_colors)

# CSS untuk flip card
st.markdown("""
<style>
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}
.flip-card {
    background-color: transparent;
    width: 100%;
    height: 200px;
    perspective: 1000px;
}
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.6s;
    transform-style: preserve-3d;
}
.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}
.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 14px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.16);
    padding: 1rem;
    text-align: center;
    color: #222;
}
.flip-card-front {
    z-index: 2;
}
.flip-card-back {
    transform: rotateY(180deg);
    box-shadow: 0 6px 24px rgba(0,0,0,0.16);
}
h3, p {
    margin: 0.5rem 0;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# HTML grid render
html = '<div class="grid-container">'
for i, row in df.iterrows():
    nama = str(row["Nama Angkatan"]).strip() if pd.notna(row["Nama Angkatan"]) else "-"
    tema = str(row["Tema Angkatan"]).strip() if pd.notna(row["Tema Angkatan"]) else "-"
    filosofi = str(row["Filosofi"]).strip() if pd.notna(row["Filosofi"]) else "-"
    bg = bg_colors[i % len(bg_colors)]
    html += f"""
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front" style="background-color: {bg};">
                <h3>🔥 {nama}</h3>
                <p>{tema}</p>
            </div>
            <div class="flip-card-back" style="background-color: {bg};">
                <p>{filosofi}</p>
            </div>
        </div>
    </div>
    """
html += '</div>'
st.markdown(html, unsafe_allow_html=True)

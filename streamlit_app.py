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
    perspective: 1000px;
}
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 180px;
    text-align: center;
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
    padding: 1rem;
    box-shadow: 0 6px 24px rgba(0,0,0,0.12);
}
.flip-card-front {
    background-color: #ffffff;
}
.flip-card-back {
    background-color: #f0f0f0;
    transform: rotateY(180deg);
    font-size: 0.9rem;
    color: #333;
}
.flip-card h3 {
    margin: 0.5rem 0 0.2rem 0;
    font-size: 1rem;
    color: #222;
}
.flip-card p {
    margin: 0;
    font-size: 0.85rem;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

# HTML grid render
html = '<div class="grid-container">'
for i, row in df.iterrows():
    nama = row["Nama Angkatan"].strip()
    tema = row["Tema Angkatan"].strip()
    filosofi = row["Filosofi"].strip()
    bg = bg_colors[i % len(bg_colors)]
    html += f"""
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front" style="background-color: {bg};">
                <h3>🔥 {nama}</h3>
                <p>{tema}</p>
            </div>
            <div class="flip-card-back">
                <p>{filosofi}</p>
            </div>
        </div>
    </div>
    """
html += '</div>'
st.markdown(html, unsafe_allow_html=True)

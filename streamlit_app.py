import streamlit as st
import pandas as pd
import random

st.set_page_config(layout="wide")
st.markdown("<h1>📦 Katalog Nama Angkatan PK-264</h1>", unsafe_allow_html=True)

# Load data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan",
    "Tema Angkatan", "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Nama Angkatan", "Tema Angkatan"])

# Warna latar belakang per card
bg_colors = [
    "#FFFAF0", "#F0FFF4", "#F0F8FF", "#FFF5F5", "#F5F5DC",
    "#FAFAD2", "#F5FFFA", "#FDF5E6", "#F0FFFF", "#FFF0F5",
    "#E6E6FA", "#FFEFD5", "#F5DEB3", "#E0FFFF", "#FBEFFB"
]
random.shuffle(bg_colors)

# CSS grid dan kartu
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    .card {
        background: #fff;
        padding: 1rem;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 6px 24px rgba(0,0,0,0.16);
        transition: all 0.2s ease-in-out;
        color: #222;
    }
    @media (prefers-color-scheme: dark) {
        .card {
            background: #222;
            color: #eee;
            box-shadow: 0 6px 24px rgba(0,0,0,0.60);
        }
        .card h3, .card p {
            color: #eee;
        }
    }
    .card:hover {
        transform: translateY(-6px) scale(1.03);
        box-shadow: 0 12px 32px rgba(0,0,0,0.22);
    }
    @media (prefers-color-scheme: dark) {
    .card {
        /* Bisa tambahkan filter untuk redupkan warna */
        filter: brightness(0.8) contrast(1.2);
    }
    }
    </style>
""", unsafe_allow_html=True)




# Render
html = '<div class="grid-container">'
for i, (_, row) in enumerate(df.iterrows()):
    nama = row["Nama Angkatan"].strip()
    tema = row["Tema Angkatan"].strip()
    bg = bg_colors[i % len(bg_colors)]
    html += (
        f'<div class="card" style="background-color: {bg};">'
        f'<h3>{nama}</h3>'
        f'<p>{tema}</p>'
        f'</div>'
    )
html += '</div>'
st.markdown(html, unsafe_allow_html=True)

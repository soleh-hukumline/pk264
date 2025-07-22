import streamlit as st
import pandas as pd
import random

st.set_page_config(layout="wide")
st.markdown("<h1>📦 Katalog Nama Angkatan PK-264</h1>", unsafe_allow_html=True)

# 🔗 Google Sheet asli
sheet_id = "1LtUlhadMhWbaKFR0GVxLP_3tTn9p9FGhVNM4tUNicng"
sheet_gid = "0"  # ganti jika bukan sheet pertama
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_gid}"

# 📥 Baca dari Google Sheet (CSV)
df = pd.read_csv(csv_url)

# 🧹 Normalisasi kolom agar konsisten
df.columns = [c.strip().lower() for c in df.columns]
rename_map = {
    "tema angkatan (mengambil tema kedaerahan/budaya indonesia contoh : papua barat daya, dari pihak lpdp diharapkan daerah sumatera/sulawesi)": "tema",
    "nama angkatan (maksimal terdiri dari 2 kata dan menggunakan bahasa indonesia atau bahasa daerah)": "nama",
    "arti dan filosofi nama angkatan": "filosofi"
}
df = df.rename(columns=rename_map)
df = df.dropna(subset=["nama", "tema", "filosofi"])

# 🎨 Warna latar acak
bg_colors = [
    "#FFFAF0", "#F0FFF4", "#F0F8FF", "#FFF5F5", "#F5F5DC",
    "#FAFAD2", "#F5FFFA", "#FDF5E6", "#F0FFFF", "#FFF0F5",
    "#E6E6FA", "#FFEFD5", "#F5DEB3", "#E0FFFF", "#FBEFFB"
]
random.shuffle(bg_colors)

# 💅 CSS untuk flip card
st.markdown("""
<style>
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
}
.flip-card {
    background-color: transparent;
    width: 100%;
    height: 180px;
    perspective: 1000px;
}
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.7s;
    transform-style: preserve-3d;
}
.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}
.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    flex-direction: column;
}
.flip-card-front {
    background-color: #ffffff;
    color: #222;
}
.flip-card-back {
    transform: rotateY(180deg);
    background-color: #f1f1f1;
    color: #333;
    font-size: 0.85rem;
    overflow-y: auto;
}
h3 {
    margin: 0.4rem 0 0.2rem 0;
    font-size: 1rem;
}
p {
    margin: 0;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# 🚀 Render flip card
html = '<div class="grid-container">'
for i, (_, row) in enumerate(df.iterrows()):
    nama = row["nama"].strip().title()
    tema = row["tema"].strip().title()
    filosofi = row["filosofi"].strip()
    bg = bg_colors[i % len(bg_colors)]

    html += f"""
    <div class="flip-card" style="background-color: {bg};">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>{nama}</h3>
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

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Ide Angkatan PK-264")

# Baca data CSV
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan", "Tema Angkatan",
    "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan"])

# Kelompokkan berdasarkan Tema Angkatan
grouped = df.groupby("Tema Angkatan")

# CSS Grid
st.markdown("""
<style>
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}
.card {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 12px;
    box-shadow: 1px 1px 6px rgba(0,0,0,0.05);
    transition: 0.2s;
    position: relative;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 2px 4px 12px rgba(0,0,0,0.1);
}
.card h4 {
    margin-bottom: 0.3rem;
}
.card small {
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# Tampilkan tiap tema
for tema, subdf in grouped:
    st.markdown(f"### 📍 {tema}")
    html = '<div class="grid">'
    for _, row in subdf.iterrows():
        filosofi = row["Filosofi"].replace('"', "'")  # hindari konflik tag HTML
        html += f"""
        <div class="card" title="{filosofi}">
            <h4>🔥 {row['Nama Angkatan']}</h4>
            <small>{tema}</small>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

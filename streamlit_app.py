import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Nama Angkatan PK-264")

# Baca file CSV
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan",
    "Tema Angkatan", "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan"])

# CSS untuk tampilan grid
st.markdown("""
<style>
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}
.card {
    background-color: #ffffff;
    border-radius: 14px;
    padding: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    text-align: center;
    font-family: sans-serif;
    transition: transform 0.1s ease-in-out;
}
.card:hover {
    transform: scale(1.02);
}
.card h4 {
    margin: 0.2rem 0;
    font-size: 1.1rem;
}
.card small {
    color: #555;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# Group berdasarkan Tema Angkatan
grouped = df.groupby("Tema Angkatan")

for tema, group in grouped:
    st.markdown(f"### 📍 {tema}")
    html = '<div class="card-grid">'
    for _, row in group.iterrows():
        html += f"""
        <div class="card">
            <h4>🔥 {row['Nama Angkatan']}</h4>
            <small>{tema}</small>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Ide Angkatan PK-264")

# Baca dan siapkan data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan", "Tema Angkatan",
    "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan"])

# CSS untuk grid layout
st.markdown("""
<style>
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    padding: 0.5rem 0;
}
.card {
    background-color: #f9f9f9;
    border-radius: 10px;
    padding: 1rem;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
    transition: transform 0.2s ease;
    cursor: default;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 2px 4px 12px rgba(0,0,0,0.1);
}
.card h5 {
    margin: 0;
    font-size: 1.1rem;
}
.card small {
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# Kelompokkan berdasarkan Tema Angkatan
grouped = df.groupby("Tema Angkatan")

for tema, subdf in grouped:
    st.markdown(f"### 📍 {tema}")
    html = '<div class="grid-container">'
    for _, row in subdf.iterrows():
        nama = row["Nama Angkatan"]
        filosofi = row["Filosofi"].replace('"', "'")  # hindari error kutip
        html += f"""
        <div class="card" title="{filosofi}">
            <h5>🔥 {nama}</h5>
            <small>{tema}</small>
        </div>
        """
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Ide Angkatan PK-264")

# Load data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan",
    "Tema Angkatan", "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan"])

# Group by Tema Angkatan
grouped = df.groupby("Tema Angkatan")

# CSS untuk grid 4 kolom
st.markdown("""
<style>
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}
.card {
    background-color: #f9f9f9;
    border-radius: 16px;
    padding: 1rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    text-align: center;
    font-size: 1rem;
    transition: 0.2s ease-in-out;
}
.card:hover {
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
.card small {
    font-size: 0.8rem;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# Tampilkan per tema
for tema, group in grouped:
    st.markdown(f"### 📍 {tema}")
    html = '<div class="card-grid">'
    for _, row in group.iterrows():
        html += f"""
        <div class="card" title="{row['Filosofi']}">
            🔥 <b>{row['Nama Angkatan']}</b>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

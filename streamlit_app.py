import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Nama Angkatan PK-264")

# Load dan bersihkan data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan",
    "Tema Angkatan", "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan"])

# CSS grid responsive
st.markdown("""
<style>
.card-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 2rem;
}
.card {
    background-color: #fff;
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    width: 230px;
    text-align: center;
    font-family: sans-serif;
    transition: transform 0.2s ease;
}
.card:hover {
    transform: translateY(-3px);
}
.card h4 {
    margin: 0.2rem 0;
    font-size: 1.1rem;
    font-weight: 600;
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
    
    html_block = '<div class="card-grid">'
    for _, row in group.iterrows():
        nama = row['Nama Angkatan'].strip()
        html_block += f"""
        <div class="card">
            <h4>🔥 {nama}</h4>
            <small>{tema}</small>
        </div>
        """
    html_block += '</div>'
    st.markdown(html_block, unsafe_allow_html=True)

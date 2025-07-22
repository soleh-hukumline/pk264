import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.markdown("<h1 style='font-size: 36px;'>📦 Katalog Ide Angkatan PK-264</h1>", unsafe_allow_html=True)

# Load data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan",
    "Tema Angkatan", "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Tema Angkatan", "Nama Angkatan"])

# Styling modern grid
st.markdown("""
<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  gap: 1.2rem;
  margin-top: 2rem;
}
.card {
  background: white;
  border-radius: 1rem;
  padding: 1.2rem;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  text-align: center;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.08);
}
.card h3 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
}
.card p {
  font-size: 0.9rem;
  color: #444;
  margin-top: 0.2rem;
}
</style>
""", unsafe_allow_html=True)

# Grid layout per angkatan
html = '<div class="grid-container">'
for _, row in df.iterrows():
    nama = row["Nama Angkatan"].strip()
    tema = row["Tema Angkatan"].strip()
    html += f"""
    <div class="card">
        <h3>🔥 {nama}</h3>
        <p>{tema}</p>
    </div>
    """
html += "</div>"
st.markdown(html, unsafe_allow_html=True)

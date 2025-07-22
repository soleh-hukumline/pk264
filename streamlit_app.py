import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📦 Katalog Ide Angkatan PK-264")

# Load data
df = pd.read_csv("Ide Tema dan Nama Angkatan PK-264.csv")
df.columns = [
    "Timestamp", "Nama Lengkap", "Panggilan", "Tema Angkatan",
    "Nama Angkatan", "Filosofi"
]
df = df.dropna(subset=["Nama Angkatan", "Tema Angkatan"])

# Ambil daftar nama angkatan unik
angkatan_group = df.groupby("Nama Angkatan")["Tema Angkatan"].unique().reset_index()

# Tambahkan CSS grid
st.markdown("""
<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
  margin-top: 20px;
}
.card {
  background-color: #f9f9f9;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
}
.card h4 {
  margin-bottom: 0.5rem;
  color: #333;
}
.card ul {
  margin: 0;
  padding-left: 1.2rem;
}
</style>
""", unsafe_allow_html=True)

# Tampilkan dalam grid
html = '<div class="grid-container">'
for _, row in angkatan_group.iterrows():
    tema_list = "".join(f"<li>{tema}</li>" for tema in row["Tema Angkatan"])
    html += f"""
    <div class="card">
        <h4>📛 {row['Nama Angkatan']}</h4>
        <ul>{tema_list}</ul>
    </div>
    """
html += "</div>"

st.markdown(html, unsafe_allow_html=True)

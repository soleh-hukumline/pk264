import streamlit as st
import pandas as pd

# Dummy data
df = pd.DataFrame({
    "Nama Angkatan": ["Alpha", "Beta", "Gamma"],
    "Tema Angkatan": ["Inovasi", "Kreativitas", "Kolaborasi"],
    "Filosofi": ["Berani", "Cerdas", "Solid"]
})

bg_colors = ["#f8b400", "#6dd5ed", "#ff6f91"]  # Contoh warna

# Inject CSS
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }
    .flip-card {
        background-color: transparent;
        width: 250px;
        height: 150px;
        perspective: 1000px;
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
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
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .flip-card-back {
        transform: rotateY(180deg);
    }
    </style>
""", unsafe_allow_html=True)

# Build HTML
html = '<div class="grid-container">'
for i, (_, row) in enumerate(df.iterrows()):
    nama = row["Nama Angkatan"].strip()
    tema = row["Tema Angkatan"].strip()
    filosofi = row["Filosofi"].strip() if pd.notna(row["Filosofi"]) else "-"
    bg = bg_colors[i % len(bg_colors)]

    html += f'''
    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front" style="background-color: {bg}">
          <h3>{nama}</h3>
          <p>{tema}</p>
        </div>
        <div class="flip-card-back" style="background-color: {bg}">
          <p>{filosofi}</p>
        </div>
      </div>
    </div>
    '''
html += '</div>'

# Render
st.markdown(html, unsafe_allow_html=True)

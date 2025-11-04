import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

"""Guilherme Couto
   Eugenio
   Leonardo
   	Grupo T3 12
"""
st.title("Fight Championship 🥊")
st.write("Bem-vindo ao sistema de gerenciamento de lutas!")


st.page_link("pages/Lutadores.py", label="👉 Ir para a página dos Lutadores", icon="🥋")

st.markdown("---")
st.markdown("### 🌳 Estrutura do Projeto")

st.code("""
(Página Principal)
└── Lutadores
    ├── Akira
    ├── Arun
    ├── Daigo
    ├── Goro
    ├── Hiro
    ├── Kenji
    ├── Mali
    └── Surya
""")
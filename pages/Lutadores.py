import base64
import streamlit as st


st.title("Lutadores 🥋")
st.write("Bem-vindo à página dos lutadores!")

st.page_link("Pagina_Inicial.py", label="⬅️ Voltar para a página inicial")

def img_to_bytes(img_path):
    img_bytes = None
    with open(img_path, "rb") as f:
        img_bytes = f.read()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# Lista de lutadores
lutadores = [
    "Akira", "Arun", "Daigo", "Goro", 
    "Hiro", "Kenji", "Mali", "Surya"
]

# Cria colunas para organizar os lutadores
cols = st.columns(4)

# Distribui os lutadores nas colunas
for i, lutador in enumerate(lutadores):
    col_index = i % 4  # Alterna entre as 4 colunas
    with cols[col_index]:
        image_path = f"fotos/{lutador}.png"
        st.markdown(
            f'<div style="text-align: center;">'
            f'<a href="{lutador}">'
            f'<img src="data:image/png;base64,{img_to_bytes(image_path)}" width="100">'
            f'<br>{lutador}</a></div>',
            unsafe_allow_html=True
        )




st.markdown("---")
st.markdown("### 🌳 Estrutura do Projeto")

st.code("""
Página Principal
└── (Lutadores)
    ├── Akira
    ├── Arun
    ├── Daigo
    ├── Goro
    ├── Hiro
    ├── Kenji
    ├── Mali
    └── Surya
""")

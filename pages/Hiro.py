import streamlit as st
import pandas as pd
from PIL import Image

# Verifica se os dados existem no session_state, se não, carrega-os
if 'dados' not in st.session_state:
    try:
        st.session_state.dados = pd.read_csv("Dados.csv")
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        st.session_state.dados = pd.DataFrame()

# Filtra os dados para o Hiro
Hiro_data = st.session_state.dados[st.session_state.dados['Nome'] == 'Hiro']
st.page_link("pages/Lutadores.py", label="⬅️ Voltar para Lutadores", icon="🥋")
st.title("Hiro 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Hiro.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Hiro", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_Hiro, Altura_Hiro, Idade_Hiro, = st.columns(3)
with Nome_Hiro:
    st.metric(label="Nome", value=Hiro_data.iloc[0]['Nome'])
with Altura_Hiro:
    st.metric(label="Altura", value=Hiro_data.iloc[0]['Altura'])
with Idade_Hiro:
    st.metric(label="Idade", value=Hiro_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Hiro_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Hiro_data.iloc[0]['Descrição'])




st.markdown("---")
st.markdown("### 🌳 Estrutura do Projeto")

st.code("""
Página Principal
└── Lutadores
    ├── Akira
    ├── Arun
    ├── Daigo
    ├── Goro
    ├── (Hiro)
    ├── Kenji
    ├── Mali
    └── Surya
""")
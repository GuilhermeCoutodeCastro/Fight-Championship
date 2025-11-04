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

# Filtra os dados para o Daigo
Daigo_data = st.session_state.dados[st.session_state.dados['Nome'] == 'Daigo']
st.page_link("pages/Lutadores.py", label="⬅️ Voltar para Lutadores", icon="🥋")
st.title("Daigo 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Daigo.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Daigo", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_Daigo, Altura_Daigo, Idade_Daigo, = st.columns(3)
with Nome_Daigo:
    st.metric(label="Nome", value=Daigo_data.iloc[0]['Nome'])
with Altura_Daigo:
    st.metric(label="Altura", value=Daigo_data.iloc[0]['Altura'])
with Idade_Daigo:
    st.metric(label="Idade", value=Daigo_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Daigo_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Daigo_data.iloc[0]['Descrição'])



st.markdown("---")
st.markdown("### 🌳 Estrutura do Projeto")

st.code("""
Página Principal
└── Lutadores
    ├── Akira
    ├── Arun
    ├── (Daigo)
    ├── Goro
    ├── Hiro
    ├── Kenji
    ├── Mali
    └── Surya
""")
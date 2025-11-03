import streamlit as st
import pandas as pd
from PIL import Image


# Acessa os dados do session_state
dados = st.session_state.dados
Akira_data = dados[dados['Nome'] == 'Akira']

st.title("Akira 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Akira.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Akira", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_akira, Altura_akira, Idade_akira, = st.columns(3)
with Nome_akira:
    st.metric(label="Nome", value=Akira_data.iloc[0]['Nome'])
with Altura_akira:
    st.metric(label="Altura", value=Akira_data.iloc[0]['Altura'])
with Idade_akira:
    st.metric(label="Idade", value=Akira_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Akira_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Akira_data.iloc[0]['Descrição'])
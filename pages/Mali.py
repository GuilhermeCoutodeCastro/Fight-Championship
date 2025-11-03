import streamlit as st
import pandas as pd
from PIL import Image


# Acessa os dados do session_state
dados = st.session_state.dados
Mali_data = dados[dados['Nome'] == 'Mali']

st.title("Mali 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Mali.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Mali", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_Mali, Altura_Mali, Idade_Mali, = st.columns(3)
with Nome_Mali:
    st.metric(label="Nome", value=Mali_data.iloc[0]['Nome'])
with Altura_Mali:
    st.metric(label="Altura", value=Mali_data.iloc[0]['Altura'])
with Idade_Mali:
    st.metric(label="Idade", value=Mali_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Mali_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Mali_data.iloc[0]['Descrição'])
import streamlit as st
import pandas as pd
from PIL import Image


# Acessa os dados do session_state
dados = st.session_state.dados
Surya_data = dados[dados['Nome'] == 'Surya']

st.title("Surya 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Surya.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Surya", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_Surya, Altura_Surya, Idade_Surya, = st.columns(3)
with Nome_Surya:
    st.metric(label="Nome", value=Surya_data.iloc[0]['Nome'])
with Altura_Surya:
    st.metric(label="Altura", value=Surya_data.iloc[0]['Altura'])
with Idade_Surya:
    st.metric(label="Idade", value=Surya_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Surya_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Surya_data.iloc[0]['Descrição'])
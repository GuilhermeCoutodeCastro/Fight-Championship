import streamlit as st
import pandas as pd
from PIL import Image


# Acessa os dados do session_state
dados = st.session_state.dados
Kenji_data = dados[dados['Nome'] == 'Kenji']

st.title("Kenji 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Kenji.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Kenji", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_Kenji, Altura_Kenji, Idade_Kenji, = st.columns(3)
with Nome_Kenji:
    st.metric(label="Nome", value=Kenji_data.iloc[0]['Nome'])
with Altura_Kenji:
    st.metric(label="Altura", value=Kenji_data.iloc[0]['Altura'])
with Idade_Kenji:
    st.metric(label="Idade", value=Kenji_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Kenji_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Kenji_data.iloc[0]['Descrição'])
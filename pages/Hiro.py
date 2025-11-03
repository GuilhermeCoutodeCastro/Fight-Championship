import streamlit as st
import pandas as pd
from PIL import Image


# Acessa os dados do session_state
dados = st.session_state.dados
Daigo_data = dados[dados['Nome'] == 'Daigo']

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
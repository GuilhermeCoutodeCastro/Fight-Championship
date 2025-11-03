import streamlit as st
import pandas as pd
from PIL import Image


# Acessa os dados do session_state
dados = st.session_state.dados
Arun_data = dados[dados['Nome'] == 'Arun']

st.title("Arun 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Arun.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Arun", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_Arun, Altura_Arun, Idade_Arun, = st.columns(3)
with Nome_Arun:
    st.metric(label="Nome", value=Arun_data.iloc[0]['Nome'])
with Altura_Arun:
    st.metric(label="Altura", value=Arun_data.iloc[0]['Altura'])
with Idade_Arun:
    st.metric(label="Idade", value=Arun_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Arun_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Arun_data.iloc[0]['Descrição'])
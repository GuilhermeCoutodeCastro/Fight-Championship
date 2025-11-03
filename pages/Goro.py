import streamlit as st
import pandas as pd
from PIL import Image


# Acessa os dados do session_state
dados = st.session_state.dados
Goro_data = dados[dados['Nome'] == 'Goro']

st.title("Goro 🥊")
st.write("Bem-vindo à página dos lutadores!")

try:
    image_path = "fotos/Goro.png"
    col_img = st.columns([1,2,1])[1]
    with col_img:
        st.image(image_path, caption="Goro", width=300)
except Exception as e:
    st.error(f"Não foi possível carregar a imagem: {e}")

st.markdown("---")
st.subheader("Informações do Lutador")
Nome_Goro, Altura_Goro, Idade_Goro, = st.columns(3)
with Nome_Goro:
    st.metric(label="Nome", value=Goro_data.iloc[0]['Nome'])
with Altura_Goro:
    st.metric(label="Altura", value=Goro_data.iloc[0]['Altura'])
with Idade_Goro:
    st.metric(label="Idade", value=Goro_data.iloc[0]['Idade'])

st.metric(label="Arte Marcial", value=Goro_data.iloc[0]['Arte Marcial'])

st.markdown("---")
st.subheader("Descrição")


st.write(Goro_data.iloc[0]['Descrição'])
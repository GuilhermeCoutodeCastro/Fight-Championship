import streamlit as st
import pandas as pd

# Configuração inicial da página
st.set_page_config(page_title="Fight Championship", page_icon="🥋")

# Inicializa os dados no session_state (isso deve ser feito ANTES de qualquer página tentar acessar)
if 'dados' not in st.session_state:
    try:
        dados = pd.read_csv("Dados.csv")
        st.session_state['dados'] = dados
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        st.session_state['dados'] = pd.DataFrame()



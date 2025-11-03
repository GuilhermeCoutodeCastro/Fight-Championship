import streamlit as st
import pandas as pd

if 'dados' not in st.session_state:
    try:
        st.session_state.dados = pd.read_csv("Dados.csv")
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        st.session_state.dados = pd.DataFrame()


    

    main_page = st.Page("pages\Pagina_Inicial.py", title="Página Inicial", icon="🏠")
    Akira = st.Page("pages\Akira.py", title="Akira", icon="🥊")
    Kenji = st.Page("pages\Kenji.py", title="Kenji", icon="🥊")



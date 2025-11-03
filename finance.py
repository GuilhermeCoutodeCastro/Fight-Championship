import streamlit as st
import pandas as pd
import yfinance as yf


def carregar_dados(empresa):
    dados_acoes = yf.Ticker(empresa)yf.history(period="1mo")
    cotacoes = dados_acoes.history(period="1d",start="2020-01-01", end="2026-06-01")
    
    return dados_acoes

dados = carregar_dados("MXRF11.SA")


st.title("Dashboard Financeiro")
st.write(""" Preço de ações que eu acompanho. """)

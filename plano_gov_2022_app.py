# Importa Bibliotecas.
import streamlit as st

import os
import re
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS

# Variáveis Globais
path = "C:/Users/GITHUB/analise-plano-governo-br-2022/dados/"

df_e = pd.read_csv(path+'estatisticas_planos_gov.txt', sep=';')

st.bar_chart(df_e, x="SGL_PARTIDO", y="QTD_PAGINAS")
#title="PRODUÇÃO DE SOJA POR ANO NO BRASIL")

st.bar_chart(df_e, x="SGL_PARTIDO", y="QTD_PALAVRAS")
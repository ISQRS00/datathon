
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import date, timedelta
from plotly.subplots import make_subplots


st.set_page_config(page_title="Introdução", page_icon="📖")

st.title("📖 Introdução")

st.title('Datathon: Fase Final')


st.markdown("## Objetivo do Projeto")


st.markdown("""
   
            

A educação é uma ferramenta poderosa de transformação social, especialmente para crianças e jovens em situação de vulnerabilidade. Neste contexto, o Datathon Passos Mágicos propõe um desafio de análise e modelagem de dados para demonstrar o impacto educacional da ONG Passos Mágicos ao longo dos anos.

Para abordar esse desafio, meu trabalho foi estruturado em duas frentes principais:

Análise Exploratória e Dashboard Interativo (Power BI)
Foi desenvolvida uma análise detalhada dos dados educacionais e socioeconômicos dos alunos atendidos pela ONG. A partir dessa análise, um dashboard interativo no Power BI foi criado para visualizar e comunicar os principais insights, como:

Evolução do desempenho acadêmico dos estudantes ao longo dos anos.
Fatores socioeconômicos que influenciam o aprendizado.
Indicadores que demonstram o impacto das ações da Passos Mágicos na educação dos alunos.
Modelo Preditivo com Machine Learning
Além da análise exploratória, foi criado um modelo preditivo utilizando técnicas de Machine Learning para prever o comportamento dos alunos com base em indicadores acadêmicos e de engajamento. A proposta preditiva inclui:

Predição do Ponto de Virada (IPV) → Identifica se o aluno atingiu um nível crítico de desenvolvimento acadêmico.
Classificação da Pedra-Conceito → Representa o nível de progresso do aluno, categorizando-o em Quartzo, Ágata, Ametista ou Topázio com base em seu desempenho.
Este projeto combina ciência de dados, aprendizado de máquina e visualização interativa para fornecer insights valiosos que auxiliam na tomada de decisões e no aprimoramento das estratégias educacionais da Passos Mágicos. 🚀📊
            """)

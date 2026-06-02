import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURAÇÃO DA PÁGINA (Tema Escuro Forçado)
st.set_page_config(layout="wide", page_title="Painel Executivo - Controladoria", page_icon="📊")

# Customização CSS corrigida para evitar o TypeError
st.html("""
    <style>
    /* Fundo geral e textos */
    .stApp { background-color: #0B0F19; color: #FFFFFF; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; font-family: 'sans-serif'; }
    
    /* Topo do Painel */
    .header-container { margin-bottom: 25px; border-bottom: 1px solid #1E293B; padding-bottom: 15px; }
    .main-title { font-size: 28px; font-weight: bold; letter-spacing: 0.5px; margin: 0; }
    .sub-title { font-size: 13px; color: #64748B; margin-top: 5px; }
    
    /* Estilização dos Cards de Indicadores */
    .kpi-card { background-color: #111827; border: 1px solid #1F2937; border-radius: 8px; padding: 15px; position: relative; margin-bottom: 15px; }
    .kpi-title { font-size: 11px; color: #9CA3AF; text-transform: uppercase; font-weight: 600; }
    .kpi-value { font-size: 24px; font-weight: bold; margin: 8px 0; color: #FFFFFF; }
    .kpi-sub { font-size: 11px; color: #38BDF8; background: rgba(56, 189, 248, 0.1); padding: 2px 6px; border-radius: 4px; display: inline-block; }
    .kpi-meta { font-size: 11px; color: #6B7280; float: right; margin-top: 2px; }
    
    /* Barras de Progresso customizadas dentro dos cards */
    .progress-bg { background-color: #374151; border-radius: 4px; height: 6px; width: 100%; margin-top: 8px; }
    .progress-fill-green { background-color: #10B981; height: 6px; border-radius: 4px; }
    .progress-fill-purple { background-color: #8B5CF6; height: 6px; border-radius: 4px; }
    
    /* Mini Cards de Ranking */
    .ranking-card { background-color: #111827; border: 1px solid #1F2937; border-radius: 8px; padding: 12px; text-align: center; }
    .ranking-title { font-size: 10px; color: #9CA3AF; text-transform: uppercase; margin-bottom: 4px; }
    .ranking-value { font-size: 15px; font-weight: bold; color: #FFFFFF; }
    </style>
""")

# 2. BASE DE DADOS (Extraída da sua tabela original)
data = [
    {"Unidade": "Jaragua", "Mês": "Janeiro", "Faturamento": 204604.98, "CMV": 71294.86, "CMO": 35948.78, "Clientes": 4786, "Ticket": 42.75},
    {"Unidade": "Jaragua", "Mês": "Fevereiro", "Faturamento": 156953.50, "CMV": 60616.18, "CMO": 30486.17, "Clientes": 3697, "Ticket": 42.45},
    {"Unidade": "Jaragua", "Mês": "Março", "Faturamento": 165966.30, "CMV": 54429.78, "CMO": 26337.95, "Clientes": 3919, "Ticket": 42.35},
    
    {"Unidade": "Lupo", "Mês": "Janeiro", "Faturamento": 60357.61, "CMV": 18387.95, "CMO": 11215.10, "Clientes": 1481, "Ticket": 40.75},
    {"Unidade": "Lupo", "Mês": "Fevereiro", "Faturamento": 68656.94, "CMV": 18172.35, "CMO": 10610.62, "Clientes": 1196, "Ticket": 57.41},
    {"Unidade": "Lupo", "Mês": "Março", "Faturamento": 59560.86, "CMV": 15478.63, "CMO": 10519.23, "Clientes": 1661, "Ticket": 35.86},
    
    {"Unidade": "Bento", "Mês": "Janeiro", "Faturamento": 191055.51, "CMV": 75215.21, "

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
    
    {"Unidade": "Bento", "Mês": "Janeiro", "Faturamento": 191055.51, "CMV": 75215.21, "CMO": 43029.58, "Clientes": 3331, "Ticket": 57.36},
    {"Unidade": "Bento", "Mês": "Fevereiro", "Faturamento": 170716.76, "CMV": 67097.70, "CMO": 31559.60, "Clientes": 2995, "Ticket": 57.00},
    {"Unidade": "Bento", "Mês": "Março", "Faturamento": 178785.09, "CMV": 64646.62, "CMO": 29542.19, "Clientes": 3220, "Ticket": 55.52},
    
    {"Unidade": "Pantanal", "Mês": "Janeiro", "Faturamento": 268797.22, "CMV": 77765.34, "CMO": 41365.89, "Clientes": 6466, "Ticket": 41.57},
    {"Unidade": "Pantanal", "Mês": "Fevereiro", "Faturamento": 196481.55, "CMV": 60283.32, "CMO": 42456.30, "Clientes": 4687, "Ticket": 41.92},
    {"Unidade": "Pantanal", "Mês": "Março", "Faturamento": 208748.95, "CMV": 62180.41, "CMO": 45737.78, "Clientes": 5033, "Ticket": 41.48},
    
    {"Unidade": "Estação", "Mês": "Janeiro", "Faturamento": 283561.46, "CMV": 75288.36, "CMO": 35830.37, "Clientes": 7165, "Ticket": 39.58},
    {"Unidade": "Estação", "Mês": "Fevereiro", "Faturamento": 224957.07, "CMV": 64990.35, "CMO": 37576.53, "Clientes": 5667, "Ticket": 39.70},
    {"Unidade": "Estação", "Mês": "Março", "Faturamento": 224115.66, "CMV": 56498.73, "CMO": 37253.45, "Clientes": 5426, "Ticket": 41.30}
]
df = pd.DataFrame(data)

# 3. FILTROS (Na barra lateral)
st.sidebar.markdown("### Parâmetros de Visão")
mes_selecionado = st.sidebar.selectbox("Selecione o Período:", ["Consolidado", "Janeiro", "Fevereiro", "Março"])

if mes_selecionado == "Consolidado":
    df_filtrado = df.copy()
else:
    df_filtrado = df[df["Mês"] == mes_selecionado]

# 4. CÁLCULO DOS INDICADORES
fat_total = df_filtrado["Faturamento"].sum()
cmv_total = df_filtrado["CMV"].sum()
cmo_total = df_filtrado["CMO"].sum()
clientes_total = df_filtrado["Clientes"].sum()

pct_cmv = (cmv_total / fat_total) * 100 if fat_total > 0 else 0
pct_cmo = (cmo_total / fat_total) * 100 if fat_total > 0 else 0
resultado_total = fat_total - (cmv_total + cmo_total)
margem_res = (resultado_total / fat_total) * 100 if fat_total > 0 else 0
ticket_medio = df_filtrado["Faturamento"].sum() / df_filtrado["Clientes"].sum() if df_filtrado["Clientes"].sum() > 0 else 0

# 5. HEADER DO PAINEL
st.html(f"""
    <div class="header-container">
        <div class="main-title">Painel Executivo · Controladoria</div>
        <div class="sub-title">Análise gerencial multiunidades · Visão: {mes_selecionado}</div>
    </div>
""")

# 6. LINHA 1: INDICADORES DO PERÍODO (KPIs)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.html(f"""
        <div class="kpi-card">
            <div class="kpi-title">Faturamento</div>
            <div class="kpi-value">R$ {fat_total:,.0f}</div>
            <div class="kpi-sub">{clientes_total:,} clientes</div>
        </div>
    """)

with col2:
    st.html(f"""
        <div class="kpi-card">
            <div class="kpi-title">CMV</div>
            <div class="kpi-value">R$ {cmv_total:,.0f}</div>
            <span class="kpi-meta">Meta: 30%</span>
            <div style="font-size:11px; color:#9CA3AF;">Realizado: {pct_cmv:.1f}%</div>
            <div class="progress-bg"><div class="progress-fill-green" style="width: {min(pct_cmv, 100)}%;"></div></div>
        </div>
    """)

with col3:
    st.html(f"""
        <div class="kpi-card">
            <div class="kpi-title">CMO</div>
            <div class="kpi-value">R$ {cmo_total:,.0f}</div>
            <span class="kpi-meta">Meta: 18%</span>
            <div style="font-size:11px; color:#9CA3AF;">Realizado: {pct_cmo:.1f}%</div>
            <div class="progress-bg"><div class="progress-fill-purple" style="width: {min(pct_cmo, 100)}%;"></div></div>
        </div>
    """)

with col4:
    st.html(f"""
        <div class="kpi-card">
            <div class="kpi-title">Resultado</div>
            <div class="kpi-value">R$ {resultado_total:,.0f}</div>
            <div class="kpi-sub" style="color:#10B981; background:rgba(16,185,129,0.1);">Margem {margem_res:.1f}%</div>
        </div>
    """)

with col5:
    st.html(f"""
        <div class="kpi-card">
            <div class="kpi-title">Ticket Médio</div>
            <div class="kpi-value">R$ {ticket_medio:.2f}</div>
            <div class="kpi-sub" style="color:#A855F7; background:rgba(168,85,247,0.1);">{clientes_total:,} atendimentos</div>
        </div>
    """)

st.write("")

# 7. LINHA 2: GRÁFICOS (Evolução e Meta)
col_g1, col_g2 = st.columns([2, 1])

with col_g1:
    st.markdown("### Evolução do Faturamento por Loja")
    df_linha = df.copy()
    df_linha['Mês'] = pd.Categorical(df_linha['Mês'], categories=["Janeiro", "Fevereiro", "Março"], ordered=True)
    df_linha = df_linha.groupby(['Mês', 'Unidade'], as_index=False)['Faturamento'].sum()
    
    fig_linha = px.line(df_linha, x="Mês", y="Faturamento", color="Unidade", markers=True,
                        color_discrete_sequence=["#38BDF8", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6"])
    fig_linha.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#FFFFFF", margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(showgrid=True, gridcolor='#1E293B'), yaxis=dict(showgrid=True, gridcolor='#1E293B')
    )
    st.plotly_chart(fig_linha, use_container_width=True)

with col_g2:
    st.markdown("### CMV vs Meta (30%)")
    df_barra = df_filtrado.groupby("Unidade", as_index=False).agg({"Faturamento":"sum", "CMV":"sum"})
    df_barra["CMV%"] = (df_barra["CMV"] / df_barra["Faturamento"]) * 100
    df_barra["Cor"] = df_barra["CMV%"].apply(lambda x: "#EF4444" if x > 30 else "#10B981")
    
    fig_barra = go.Figure()
    fig_barra.add_trace(go.Bar(x=df_barra["Unidade"], y=df_barra["CMV%"], marker_color=df_barra["Cor"], name="CMV %"))
    fig_barra.add_shape(type="line", x0=-0.5, x1=len(df_barra)-0.5, y0=30, y1=30,
                        line=dict(color="#F59E0B", width=2, dash="dash"))
    
    fig_barra.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#FFFFFF", 
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis=dict(ticksuffix="%", showgrid=True, gridcolor='#1E293B')
    )
    st.plotly_chart(fig_barra, use_container_width=True)

# 8. LINHA 3: RANKING DAS UNIDADES
st.markdown("### 🏆 Ranking das Unidades")
col_r1, col_r2, col_r3, col_r4, col_r5, col_r6 = st.columns(6)

df_rank = df_filtrado.groupby("Unidade", as_index=False).agg({
    "Faturamento": "sum", "CMV": "sum", "CMO": "sum", "Clientes": "sum", "Ticket": "mean"
})
df_rank["Resultado"] = df_rank["Faturamento"] - (df_rank["CMV"] + df_rank["CMO"])
df_rank["CMV%"] = (df_rank["CMV"] / df_rank["Faturamento"]) * 100
df_rank["CMO%"] = (df_rank["CMO"] / df_rank["Faturamento"]) * 100

with col_r1:
    top_fat = df_rank.sort_values(by="Faturamento", ascending=False).iloc[0]["Unidade"]
    st.html(f'<div class="ranking-card"><div class="ranking-title">🥇 Maior Faturamento</div><div class="ranking-value">{top_fat}</div></div>')
with col_r2:
    top_res = df_rank.sort_values(by="Resultado", ascending=False).iloc[0]["Unidade"]
    st.html(f'<div class="ranking-card"><div class="ranking-title">💰 Maior Resultado</div><div class="ranking-value">{top_res}</div></div>')
with col_r3:
    top_tkt = df_rank.sort_values(by="Ticket", ascending=False).iloc[0]["Unidade"]
    st.html(f'<div class="ranking-card"><div class="ranking-title">🎯 Maior Ticket Médio</div><div class="ranking-value">{top_tkt}</div></div>')
with col_r4:
    top_flx = df_rank.sort_values(by="Clientes", ascending=False).iloc[0]["Unidade"]
    st.html(f'<div class="ranking-card"><div class="ranking-title">👥 Maior Fluxo</div><div class="ranking-value">{top_flx}</div></div>')
with col_r5:
    top_cmv = df_rank.sort_values(by="CMV%").iloc[0]["Unidade"]
    st.html(f'<div class="ranking-card"><div class="ranking-title">✅ CMV Eficiente</div><div class="ranking-value">{top_cmv}</div></div>')
with col_r6:
    top_cmo = df_rank.sort_values(by="CMO%").iloc[0]["Unidade"]
    st.html(f'<div class="ranking-card"><div class="ranking-title">⚡ CMO Eficiente</div><div class="ranking-value">{top_cmo}</div></div>')

st.write("")

# 9. LINHA 4: TABELA COMPARATIVA DE UNIDADES
st.markdown("### Comparativo Entre Unidades")

df_tabela = df_filtrado.groupby("Unidade").agg({
    "Faturamento": "sum", "CMV": "sum", "CMO": "sum", "Clientes": "sum", "Ticket": "mean"
}).reset_index()

df_tabela["CMV%"] = (df_tabela["CMV"] / df_tabela["Faturamento"]) * 100
df_tabela["CMO%"] = (df_tabela["CMO"] / df_tabela["Faturamento"]) * 100

st.dataframe(
    df_tabela.style.format({
        "Faturamento": "R$ {:,.0f}", "CMV": "R$ {:,.0f}", "CMO": "R$ {:,.0f}",
        "CMV%": "{:.2f}%", "CMO%": "{:.2f}%", "Ticket": "R$ {:.2f}", "Clientes": "{:,}"
    }), use_container_width=True
)

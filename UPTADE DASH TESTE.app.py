<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel Executivo | Controladoria</title>
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --bg: #080d14;
            --surface: #0e1622;
            --surface2: #151f2e;
            --border: rgba(255,255,255,0.06);
            --text: #e8edf5;
            --muted: #64748b;
            --accent: #3b82f6;
            --green: #10b981;
            --red: #ef4444;
            --yellow: #f59e0b;
            --cyan: #06b6d4;
            --purple: #8b5cf6;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'DM Sans', sans-serif;
            min-height: 100vh;
            overflow-x: hidden;
        }
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(59,130,246,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(59,130,246,0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            pointer-events: none;
            z-index: 0;
        }
        .wrap { position: relative; z-index: 1; padding: 24px 32px; max-width: 1600px; margin: 0 auto; }
        .header { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 20px; margin-bottom: 32px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
        .header-left h1 { font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800; letter-spacing: -0.5px; background: linear-gradient(135deg, #e8edf5 0%, #64a8ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .header-left p { font-size: 13px; color: var(--muted); margin-top: 4px; }
        .header-right { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
        select {
            background: var(--surface2);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 13px;
            font-family: 'DM Sans', sans-serif;
            cursor: pointer;
            outline: none;
            appearance: none;
            padding-right: 32px;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2364748b' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 12px center;
        }
        .badge-live { display: flex; align-items: center; gap: 6px; background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.25); color: var(--green); padding: 8px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .dot { width: 7px; height: 7px; border-radius: 50%; background: var(--green); animation: pulse 2s infinite; }
        @keyframes pulse { 0%,100% { opacity: 1 } 50% { opacity: 0.3 } }
        .tabs { display: flex; gap: 4px; margin-bottom: 28px; background: var(--surface); padding: 4px; border-radius: 12px; width: fit-content; }
        .tab { padding: 10px 20px; border-radius: 9px; cursor: pointer; font-size: 13px; font-weight: 500; color: var(--muted); transition: all 0.2s; }
        .tab.active { background: var(--surface2); color: var(--text); box-shadow: 0 2px 8px rgba(0,0,0,0.3); }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        .section-title { font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--muted); margin-bottom: 16px; }
        .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 28px; }
        .card { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 20px; position: relative; overflow: hidden; transition: transform 0.2s, box-shadow 0.2s; }
        .card:hover { transform: translateY(-3px); box-shadow: 0 12px 30px rgba(0,0,0,0.4); }
        .card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, var(--card-color, var(--accent)), transparent); }
        .card h3 { font-size: 11px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; color: var(--muted); margin-bottom: 14px; }
        .card .val { font-family: 'Syne', sans-serif; font-size: 26px; font-weight: 700; margin-bottom: 10px; letter-spacing: -0.5px; }
        .card .sub { display: flex; flex-direction: column; gap: 4px; font-size: 12px; color: var(--muted); }
        .card .tag { display: inline-flex; align-items: center; gap: 4px; padding: 4px 8px; border-radius: 6px; font-size: 11px; font-weight: 600; width: fit-content; }
        .tag.up { background: rgba(16,185,129,0.12); color: var(--green); }
        .tag.down { background: rgba(239,68,68,0.12); color: var(--red); }
        .tag.info { background: rgba(59,130,246,0.12); color: var(--accent); }
        .meta-bar { margin-top: 10px; }
        .meta-label { display: flex; justify-content: space-between; font-size: 11px; color: var(--muted); margin-bottom: 5px; }
        .bar-track { height: 5px; background: var(--surface2); border-radius: 3px; overflow: hidden; }
        .bar-fill { height: 100%; border-radius: 3px; transition: width 0.8s ease; }
        .charts-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; margin-bottom: 28px; }
        .chart-box { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 22px; }
        .chart-box h2 { font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; margin-bottom: 20px; }
        .chart-box canvas { max-height: 260px; }
        .insights-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 28px; }
        .insight-card { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--ins-color, var(--accent)); border-radius: 12px; padding: 16px; }
        .insight-card .ins-title { font-size: 11px; font-weight: 600; letter-spacing: 0.8px; text-transform: uppercase; color: var(--muted); margin-bottom: 6px; }
        .insight-card p { font-size: 13px; line-height: 1.5; }
        .table-box { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 22px; margin-bottom: 28px; overflow-x: auto; }
        .table-box h2 { font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; min-width: 800px; }
        table th { background: var(--surface2); padding: 12px 14px; text-align: left; font-size: 11px; font-weight: 600; letter-spacing: 0.8px; text-transform: uppercase; color: var(--muted); }
        table th:first-child { border-radius: 8px 0 0 8px; }
        table th:last-child { border-radius: 0 8px 8px 0; }
        table td { padding: 13px 14px; border-bottom: 1px solid var(--border); font-size: 13px; vertical-align: middle; }
        table tr:last-child td { border-bottom: none; }
        table tr:hover td { background: rgba(255,255,255,0.02); }
        .badge { padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; }
        .badge.ok { background: rgba(16,185,129,0.12); color: var(--green); }
        .badge.warn { background: rgba(245,158,11,0.12); color: var(--yellow); }
        .badge.bad { background: rgba(239,68,68,0.12); color: var(--red); }
        .ranking-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 28px; }
        .rank-card { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 18px; text-align: center; }
        .rank-card .rank-icon { font-size: 24px; margin-bottom: 8px; }
        .rank-card h4 { font-size: 11px; font-weight: 600; letter-spacing: 0.8px; text-transform: uppercase; color: var(--muted); margin-bottom: 6px; }
        .rank-card p { font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; }
        .dre-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 28px; }
        .dre-row { display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; border-radius: 8px; margin-bottom: 4px; font-size: 13px; }
        .dre-row.header-row { background: var(--surface2); font-weight: 600; font-size: 12px; color: var(--muted); letter-spacing: 0.5px; }
        .dre-row.highlight { background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.15); }
        .dre-row.total { background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.15); font-weight: 600; }
        .dre-val { font-weight: 600; }
        @media(max-width:900px){ .charts-grid, .dre-grid { grid-template-columns: 1fr; } .wrap { padding: 16px; } }
    </style>
</head>
<body>
<div class="wrap">

<div class="header">
  <div class="header-left">
    <h1>Painel Executivo · Controladoria</h1>
    <p>Análise gerencial multiunidades · Dados até Abril/2026</p>
  </div>
  <div class="header-right">
    <select id="selPeriodo">
      <option value="jan">Janeiro/2026</option>
      <option value="fev">Fevereiro/2026</option>
      <option value="mar">Março/2026</option>
      <option value="abr" selected>Abril/2026</option>
    </select>
    <select id="selLoja">
      <option value="consolidado">Consolidado</option>
      <option value="jaragua">Jaragua</option>
      <option value="lupo">Lupo</option>
      <option value="bento">Bento</option>
      <option value="estacao">Estação</option>
      <option value="pantanal">Pantanal</option>
      <option value="bento_lupo">Bento/Lupo</option>
    </select>
    <div class="badge-live"><span class="dot"></span>Maio em andamento</div>
  </div>
</div>

<div class="tabs">
  <div class="tab active" onclick="switchTab('visao')">Visão Executiva</div>
  <div class="tab" onclick="switchTab('dre')">DRE Gerencial</div>
  <div class="tab" onclick="switchTab('forecast')">Forecast</div>
</div>

<div id="tab-visao" class="tab-content active">
  <p class="section-title">Indicadores do Período</p>
  <div class="cards" id="cards-kpi"></div>
  
  <div class="charts-grid">
    <div class="chart-box">
      <h2>Evolução do Faturamento por Loja</h2>
      <canvas id="chartLinha"></canvas>
    </div>
    <div class="chart-box">
      <h2>CMV vs Meta (30%)</h2>
      <canvas id="chartCMV"></canvas>
    </div>
  </div>

  <p class="section-title">Ranking das Unidades</p>
  <div class="ranking-grid">
    <div class="rank-card"><div class="rank-icon">🏆</div><h4>Maior Faturamento</h4><p id="rank-fat">—</p></div>
    <div class="rank-card"><div class="rank-icon">💰</div><h4>Maior Resultado</h4><p id="rank-res">—</p></div>
    <div class="rank-card"><div class="rank-icon">🎯</div><h4>Maior Ticket Médio</h4><p id="rank-ticket">—</p></div>
    <div class="rank-card"><div class="rank-icon">👥</div><h4>Maior Fluxo</h4><p id="rank-clientes">—</p></div>
    <div class="rank-card"><div class="rank-icon">✅</div><h4>CMV Eficiente</h4><p id="rank-cmv">—</p></div>
    <div class="rank-card"><div class="rank-icon">⚡</div><h4>CMO Eficiente</h4><p id="rank-cmo">—</p></div>
  </div>

  <div class="table-box">
    <h2>Comparativo Entre Unidades</h2>
    <table>
      <thead>
        <tr>
          <th>Unidade</th>
          <th>Faturamento</th>
          <th>Var. Mês</th>
          <th>CMV</th>
          <th>CMV%</th>
          <th>CMO</th>
          <th>CMO%</th>
          <th>Ticket Médio</th>
          <th>Clientes</th>
          <th>Eficiência</th>
        </tr>
      </thead>
      <tbody id="tbody-lojas"></tbody>
    </table>
  </div>

  <p class="section-title">Insights da Controladoria</p>
  <div class="insights-grid" id="insights-box"></div>
</div>

<div id="tab-dre" class="tab-content">
  <p class="section-title">DRE Gerencial Estruturada</p>
  <div class="dre-grid">
    <div class="chart-box">
      <h2>Estrutura de Custos Relativa (%)</h2>
      <canvas id="chartDRE"></canvas>
    </div>
    <div class="table-box" style="margin-bottom:0; padding:10px;">
      <div class="dre-row header-row"><span>Estrutura Comercial</span><span>Valor Absoluto</span></div>
      <div class="dre-row"><span>(+) Receita Bruta</span><span class="dre-val" id="dre-fat">R$ 0</span></div>
      <div class="dre-row"><span>(-) Custos de Mercadorias (CMV)</span><span class="dre-val" id="dre-cmv" style="color:var(--red)">R$ 0</span></div>
      <div class="dre-row highlight"><span>(=) Margem Bruta Comercial</span><span class="dre-val" id="dre-mb">R$ 0</span></div>
      <div class="dre-row"><span>(-) Custos Operacionais (CMO)</span><span class="dre-val" id="dre-cmo" style="color:var(--red)">R$ 0</span></div>
      <div class="dre-row total"><span>(=) Resultado Operacional Gerencial</span><span class="dre-val" id="dre-res" style="color:var(--green)">R$ 0</span></div>
    </div>
  </div>
</div>

<div id="tab-forecast" class="tab-content">
  <p class="section-title">Análise de Performance Histórica Acumulada</p>
  <div class="charts-grid" style="grid-template-columns: 1fr 1fr;">
    <div class="chart-box">
      <h2>Faturamento Total Acumulado por Canal (Jan-Abr)</h2>
      <canvas id="chartForecast"></canvas>
    </div>
    <div class="chart-box">
      <h2>Participação no Faturamento Total da Rede</h2>
      <canvas id="chartRanking"></canvas>
    </div>
  </div>
</div>

</div>

<script>
// ==================== BANCO DE DADOS OFICIAL (ATUALIZADO) ====================
const DB = {
  jan: {
    consolidado: { fat: 1276297, cmv: 441334, cmo: 236318, res: 598645, ticket: 48.97, clientes: 26065 },
    jaragua: { fat: 204604.98, cmv: 71294.86, cmv_p: 34.85, cmo: 35948.78, cmo_p: 17.57, ticket: 42.75, clientes: 4786, res: 97361.34 },
    lupo: { fat: 60357.61, cmv: 18387.95, cmv_p: 30.47, cmo: 11215.10, cmo_p: 18.58, ticket: 40.75, clientes: 1481, res: 30754.56 },
    bento: { fat: 191055.51, cmv: 75215.21, cmv_p: 39.37, cmo: 43029.58, cmo_p: 22.52, ticket: 57.36, clientes: 3331, res: 72810.72 },
    pantanal: { fat: 268797.22, cmv: 77765.34, cmv_p: 28.93, cmo: 41365.89, cmo_p: 15.39, ticket: 41.57, clientes: 6466, res: 149665.99 },
    estacao: { fat: 283561.46, cmv: 75288.36, cmv_p: 26.55, cmo: 35830.37, cmo_p: 12.64, ticket: 39.58, clientes: 7165, res: 172442.73 },
    bento_lupo: { fat: 259712.45, cmv: 93387.56, cmv_p: 35.96, cmo: 53640.20, cmo_p: 20.65, ticket: 57.37, clientes: 4527, res: 112684.69 }
  },
  fev: {
    consolidado: { fat: 1345423, cmv: 419253, cmo: 236113, res: 690057, ticket: 52.88, clientes: 25444 },
    jaragua: { fat: 156953.50, cmv: 60616.18, cmv_p: 38.62, cmo: 30486.17, cmo_p: 19.42, ticket: 42.45, clientes: 3697, res: 65851.15 },
    lupo: { fat: 68656.94, cmv: 18172.35, cmv_p: 26.47, cmo: 10610.62, cmo_p: 15.45, ticket: 57.41, clientes: 1196, res: 39873.97 },
    bento: { fat: 170716.76, cmv: 67097.70, cmv_p: 39.30, cmo: 31559.60, cmo_p: 18.49, ticket: 57.00, clientes: 2995, res: 72059.46 },
    pantanal: { fat: 196481.55, cmv: 60283.32, cmv_p: 30.68, cmo: 42456.30, cmo_p: 21.61, ticket: 41.92, clientes: 4687, res: 93741.93 },
    estacao: { fat: 224957.07, cmv: 64990.35, cmv_p: 28.89, cmo: 37576.53, cmo_p: 16.70, ticket: 39.70, clientes: 5667, res: 122390.19 },
    bento_lupo: { fat: 336683.06, cmv: 121527.48, cmv_p: 36.10, cmo: 57897.55, cmo_p: 17.20, ticket: 48.70, clientes: 6914, res: 157258.03 }
  },
  mar: {
    consolidado: { fat: 1076338, cmv: 346202, cmo: 178940, res: 551196, ticket: 51.52, clientes: 20892 },
    jaragua: { fat: 165966.30, cmv: 54429.78, cmv_p: 32.80, cmo: 26337.95, cmo_p: 15.87, ticket: 42.35, clientes: 3919, res: 85198.57 },
    lupo: { fat: 59560.86, cmv: 15478.63, cmv_p: 25.99, cmo: 10519.23, cmo_p: 17.66, ticket: 35.86, clientes: 1661, res: 33562.99 },
    bento: { fat: 178785.09, cmv: 64646.62, cmv_p: 36.16, cmo: 29542.19, cmo_p: 16.52, ticket: 55.52, clientes: 3220, res: 84596.28 },
    pantanal: { fat: 208748.95, cmv: 62180.41, cmv_p: 29.79, cmo: 45737.78, cmo_p: 21.91, ticket: 41.48, clientes: 5033, res: 100830.76 },
    estacao: { fat: 224115.66, cmv: 56498.73, cmv_p: 25.21, cmo: 37253.45, cmo_p: 16.62, ticket: 41.30, clientes: 5426, res: 130363.48 },
    bento_lupo: { fat: 239142.70, cmv: 83034.57, cmv_p: 34.72, cmo: 40757.29, cmo_p: 17.04, ticket: 50.87, clientes: 4701, res: 115350.84 }
  },
  abr: {
    consolidado: { fat: 491567, cmv: 134503, cmo: 88763, res: 268301, ticket: 40.60, clientes: 12108 },
    jaragua: { fat: 0, cmv: 0, cmv_p: 0, cmo: 0, cmo_p: 0, ticket: 0, clientes: 0, res: 0 },
    lupo: { fat: 0, cmv: 0, cmv_p: 0, cmo: 0, cmo_p: 0, ticket: 0, clientes: 0, res: 0 },
    bento: { fat: 0, cmv: 0, cmv_p: 0, cmo: 0, cmo_p: 0, ticket: 0, clientes: 0, res: 0 },
    pantanal: { fat: 236604.68, cmv: 68480.69, cmv_p: 28.94, cmo: 53278.41, cmo_p: 22.52, ticket: 40.45, clientes: 5849, res: 114845.58 },
    estacao: { fat: 254962.47, cmv: 66022.53, cmv_p: 25.89, cmo: 35485.50, cmo_p: 13.92, ticket: 40.74, clientes: 6259, res: 153454.44 },
    bento_lupo: { fat: 0, cmv: 0, cmv_p: 0, cmo: 0, cmo_p: 0, ticket: 0, clientes: 0, res: 0 }
  }
};

const LOJAS = ['jaragua','lupo','bento','estacao','pantanal','bento_lupo'];
const LABELS = {jaragua:'Jaragua',lupo:'Lupo',bento:'Bento',estacao:'Estação',pantanal:'Pantanal',bento_lupo:'Bento/Lupo',consolidado:'Consolidado'};
const COLORS = ['#3b82f6','#10b981','#f59e0b','#ef4444','#8b5cf6','#ec4899'];

let currentPeriodo = 'abr';
let currentLoja = 'consolidado';
let charts = {};

function fmt(v){ return 'R$ ' + v.toLocaleString('pt-BR',{minimumFractionDigits:0,maximumFractionDigits:0}); }

function eficiencia(cmvp, cmop){
  if(cmvp === 0) return '<span class="badge warn">Sem Dados</span>';
  if(cmvp <= 30 && cmop <= 18) return '<span class="badge ok">Excelente</span>';
  if(cmvp <= 35 && cmop <= 20) return '<span class="badge warn">Boa</span>';
  return '<span class="badge bad">Atenção</span>';
}

function varMes(loja, periodo){
  const order = ['jan','fev','mar','abr'];
  const idx = order.indexOf(periodo);
  if(idx === 0) return '<span class="tag info">Início</span>';
  const prev = order[idx-1];
  const curr = DB[periodo][loja]?.fat || 0;
  const ant = DB[prev][loja]?.fat || 0;
  if(!ant || !curr) return '—';
  const v = ((curr-ant)/ant*100).toFixed(1);
  return v >= 0 ? `<span class="tag up">▲ +${v}%</span>` : `<span class="tag down">▼ ${v}%</span>`;
}

function renderKPI(){
  const d = DB[currentPeriodo][currentLoja];
  const cmv_perc = d.fat > 0 ? (d.cmv_p || (d.cmv/d.fat*100)) : 0;
  const cmo_perc = d.fat > 0 ? (d.cmo_p || (d.cmo/d.fat*100)) : 0;
  
  const cards = [
    {label:'Faturamento', val:fmt(d.fat), style:'--card-color:#3b82f6', extra:`<span class="tag info">${d.clientes.toLocaleString('pt-BR')} clientes</span>`},
    {label:'CMV', val:fmt(d.cmv), style:'--card-color:#f59e0b', extra:`
      <div class="meta-bar">
        <div class="meta-label"><span>Realizado: ${cmv_perc.toFixed(1)}%</span><span>Meta: 30%</span></div>
        <div class="bar-track"><div class="bar-fill" style="width:${Math.min(cmv_perc/40*100,100)}%;background:${cmv_perc<=30?'var(--green)':'var(--red)'}"></div></div>
      </div>`},
    {label:'CMO', val:fmt(d.cmo), style:'--card-color:#8b5cf6', extra:`
      <div class="meta-bar">
        <div class="meta-label"><span>Realizado: ${cmo_perc.toFixed(1)}%</span><span>Meta: 18%</span></div>
        <div class="bar-track"><div class="bar-fill" style="width:${Math.min(cmo_perc/25*100,100)}%;background:${cmo_perc<=18?'var(--green)':'var(--red)'}"></div></div>
      </div>`},
    {label:'Resultado', val:fmt(d.res), style:'--card-color:#10b981', extra:`<span class="tag up">Margem ${d.fat>0?(d.res/d.fat*100).toFixed(1):0}%</span>`},
    {label:'Ticket Médio', val:'R$ '+d.ticket.toFixed(2).replace('.',','), style:'--card-color:#06b6d4', extra:`<span class="tag info">${d.clientes.toLocaleString('pt-BR')} atendimentos</span>`},
  ];
  document.getElementById('cards-kpi').innerHTML = cards.map(c=>`
    <div class="card" style="${c.style}">
      <h3>${c.label}</h3>
      <div class="val">${c.val}</div>
      <div class="sub">${c.extra}</div>
    </div>`).join('');
}

function renderTabela(){
  const periodo = currentPeriodo;
  const rows = LOJAS.map(l=>{
    const d = DB[periodo][l];
    if(!d) return '';
    const cmv_p = d.fat > 0 ? (d.cmv_p || (d.cmv/d.fat*100)) : 0;
    const cmo_p = d.fat > 0 ? (d.cmo_p || (d.cmo/d.fat*100)) : 0;
    return `<tr>
      <td><b>${LABELS[l]}</b></td>
      <td>${fmt(d.fat)}</td>
      <td>${varMes(l,periodo)}</td>
      <td>${fmt(d.cmv)}</td>
      <td>${cmv_p.toFixed(1)}%</td>
      <td>${fmt(d.cmo)}</td>
      <td>${cmo_p.toFixed(1)}%</td>
      <td>R$ ${d.ticket.toFixed(2).replace('.',',')}</td>
      <td>${d.clientes.toLocaleString('pt-BR')}</td>
      <td>${eficiencia(cmv_p, cmo_p)}</td>
    </tr>`;
  }).join('');
  document.getElementById('tbody-lojas').innerHTML = rows;
}

function renderRanking(){
  const d = DB[currentPeriodo];
  const validLojas = LOJAS.filter(l => d[l].fat > 0);
  
  if(validLojas.length === 0){
    ['rank-fat','rank-res','rank-ticket','rank-clientes','rank-cmv','rank-cmo'].forEach(id => {
      document.getElementById(id).textContent = "N/A";
    });
    return;
  }

  const byFat = validLojas.slice().sort((a,b)=>d[b].fat-d[a].fat);
  const byRes = validLojas.slice().sort((a,b)=>d[b].res-d[a].res);
  const byTicket = validLojas.slice().sort((a,b)=>d[b].ticket-d[a].ticket);
  const byClientes = validLojas.slice().sort((a,b)=>d[b].clientes-d[a].clientes);
  const byCMV = validLojas.slice().sort((a,b)=>(d[a].cmv_p||(d[a].cmv/d[a].fat*100))-(d[b].cmv_p||(d[b].cmv/d[b].fat*100)));
  const byCMO = validLojas.slice().sort((a,b)=>(d[a].cmo_p||(d[a].cmo/d[a].fat*100))-(d[b].cmo_p||(d[b].cmo/d[b].fat*100)));

  document.getElementById('rank-fat').textContent = LABELS[byFat[0]];
  document.getElementById('rank-res').textContent = LABELS[byRes[0]];
  document.getElementById('rank-ticket').textContent = LABELS[byTicket[0]];
  document.getElementById('rank-clientes').textContent = LABELS[byClientes[0]];
  document.getElementById('rank-cmv').textContent = LABELS[byCMV[0]];
  document.getElementById('rank-cmo').textContent = LABELS[byCMO[0]];
}

function renderInsights(){
  const d = DB[currentPeriodo];
  const validLojas = LOJAS.filter(l => d[l].fat > 0);
  if(validLojas.length === 0) {
    document.getElementById('insights-box').innerHTML = '<p style="padding:15px; color:var(--muted);">Sem movimentação financeira relevante registrada no período.</p>';
    return;
  }
  const byFat = validLojas.slice().sort((a,b)=>d[b].fat-d[a].fat);
  const byCMO = validLojas.slice().sort((a,b)=>(d[b].cmo_p||(d[b].cmo/d[b].fat*100))-(d[a].cmo_p||(d[a].cmo/d[a].fat*100)));

  const insights = [
    {color:'var(--accent)', title:'📊 Liderança Mensal', msg:`A unidade ${LABELS[byFat[0]]} performou a maior receita com ${fmt(d[byFat[0]].fat)}.`},
    {color:'var(--red)', title:'⚠️ Alerta de Eficiência (CMO)', msg:`A filial ${LABELS[byCMO[0]]} acusou desvio operacional em CMO, fechando em ${(d[byCMO[0]].cmo_p || (d[byCMO[0]].cmo/d[byCMO[0]].fat*100)).toFixed(1)}%.`}
  ];
  document.getElementById('insights-box').innerHTML = insights.map(i=>`
    <div class="insight-card" style="--ins-color:${i.color}">
      <div class="ins-title">${i.title}</div>
      <p>${i.msg}</p>
    </div>`).join('');
}

function destroyChart(id){ if(charts[id]){ charts[id].destroy(); delete charts[id]; } }

function renderChartLinha(){
  destroyChart('linha');
  const periodos = ['jan','fev','mar','abr'];
  const labels = ['Janeiro','Fevereiro','Março','Abril'];
  const datasets = LOJAS.map((l,i)=>({
    label: LABELS[l],
    data: periodos.map(p=>DB[p][l]?.fat||0),
    borderColor: COLORS[i],
    backgroundColor: COLORS[i]+'11',
    borderWidth: 2,
    tension: 0.2
  }));
  charts['linha'] = new Chart(document.getElementById('chartLinha'),{
    type:'line',
    data:{labels, datasets},
    options:{responsive:true, plugins:{legend:{labels:{color:'#94a3b8'}}}, scales:{x:{ticks:{color:'#64748b'}},y:{ticks:{color:'#64748b',callback:v=>'R$'+(v/1000).toFixed(0)+'k'}}}}
  });
}

function renderChartCMV(){
  destroyChart('cmv');
  const d = DB[currentPeriodo];
  const vals = LOJAS.map(l=> {
    const p = d[l]?.fat > 0 ? (d[l]?.cmv_p || (d[l]?.cmv/d[l]?.fat*100)) : 0;
    return parseFloat(p).toFixed(1);
  });
  const colors = vals.map(v=>v<=30 && v>0?'rgba(16,185,129,0.7)':'rgba(239,68,68,0.7)');
  charts['cmv'] = new Chart(document.getElementById('chartCMV'),{
    type:'bar',
    data:{
      labels: LOJAS.map(l=>LABELS[l]),
      datasets:[
        {label:'CMV Realizado %', data:vals, backgroundColor:colors, borderRadius:4},
        {label:'Meta Teto (30%)', data:LOJAS.map(()=>30), type:'line', borderColor:'#f59e0b', borderDash:[5,5], pointRadius:0, fill:false}
      ]
    },
    options:{responsive:true, plugins:{legend:{labels:{color:'#94a3b8'}}}, scales:{x:{ticks:{color:'#64748b'}},y:{ticks:{color:'#64748b',callback:v=>v+'%'},max:50}}}
  });
}

function renderChartDRE(){
  destroyChart('dre');
  const d = DB[currentPeriodo][currentLoja];
  
  document.getElementById('dre-fat').textContent = fmt(d.fat);
  document.getElementById('dre-cmv').textContent = fmt(d.cmv);
  document.getElementById('dre-cmo').textContent = fmt(d.cmo);
  document.getElementById('dre-mb').textContent = fmt(d.fat - d.cmv);
  document.getElementById('dre-res').textContent = fmt(d.res);

  charts['dre'] = new Chart(document.getElementById('chartDRE'),{
    type:'doughnut',
    data:{
      labels:['CMV (%)','CMO (%)','Margem Líquida (%)'],
      datasets:[{
        data:[d.fat>0?(d.cmv/d.fat*100):0, d.fat>0?(d.cmo/d.fat*100):0, d.fat>0?(d.res/d.fat*100):0],
        backgroundColor:['#f59e0b','#8b5cf6','#10b981'],
        borderWidth:0
      }]
    },
    options:{responsive:true, plugins:{legend:{position:'bottom', labels:{color:'#94a3b8'}}}}
  });
}

function renderForecastCharts(){
  destroyChart('forecast');
  destroyChart('ranking');

  const acumulado = LOJAS.map(l => ['jan','fev','mar','abr'].reduce((acc,p)=>acc+(DB[p][l]?.fat||0),0));

  charts['forecast'] = new Chart(document.getElementById('chartForecast'),{
    type:'bar',
    data:{
      labels: LOJAS.map(l=>LABELS[l]),
      datasets:[{label:'Volume Faturado Acumulado 2026', data:acumulado, backgroundColor:'rgba(59,130,246,0.6)', borderRadius:4}]
    },
    options:{responsive:true, plugins:{legend:{labels:{color:'#94a3b8'}}}, scales:{x:{ticks:{color:'#64748b'}},y:{ticks:{color:'#64748b',callback:v=>'R$'+(v/1000).toFixed(0)+'k'}}}}
  });

  charts['ranking'] = new Chart(document.getElementById('chartRanking'),{
    type:'pie',
    data:{
      labels: LOJAS.map(l=>LABELS[l]),
      datasets:[{data:acumulado, backgroundColor:COLORS}]
    },
    options:{responsive:true, plugins:{legend:{position:'right', labels:{color:'#94a3b8'}}}}
  });
}

function switchTab(name){
  document.querySelectorAll('.tab').forEach((t,i)=>{
    const names=['visao','dre','forecast'];
    t.classList.toggle('active', names[i]===name);
  });
  document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active'));
  document.getElementById('tab-'+name).classList.add('active');
  
  if(name==='dre') setTimeout(renderChartDRE, 30);
  if(name==='forecast') setTimeout(renderForecastCharts, 30);
}

function atualizar(){
  currentPeriodo = document.getElementById('selPeriodo').value;
  currentLoja = document.getElementById('selLoja').value;
  renderKPI();
  renderTabela();
  renderRanking();
  renderInsights();
  renderChartLinha();
  renderChartCMV();
  if(document.getElementById('tab-dre').classList.contains('active')) renderChartDRE();
}

document.getElementById('selPeriodo').addEventListener('change', atualizar);
document.getElementById('selLoja').addEventListener('change', atualizar);

atualizar();
</script>
</body>
</html>

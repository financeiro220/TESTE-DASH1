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
        .insight-card .ins-title { font-size: 11px; font-weight: 600; letter-spacing

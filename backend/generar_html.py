import pandas as pd
file = '../MallaClientes.xlsx'
df = pd.read_excel(file, engine='openpyxl')
cols = [c for c in df.columns if 'nit' in c.lower() or 'nombre' in c.lower() or 'rutero' in c.lower() or 'cupo' in c.lower() or 'clasific' in c.lower() or 'cartera' in c.lower() or 'edad' in c.lower() or 'vendedor' in c.lower() or 'ciudad' in c.lower() or 'departamento' in c.lower()]
df_out = df[cols].head(100)
total_clientes = len(df)
por_cluster = df_out.groupby(df_out.columns[-1]).size().to_dict() if len(df_out.columns) > 0 else {}
html_table = df_out.to_html(index=False, classes='tabla-clientes', border=0)
kpi_html = f"<div class='kpis'><b>Total clientes:</b> {total_clientes}<br>" + "<br>".join([f"<b>{k}:</b> {v}" for k,v in por_cluster.items()]) + "</div>"
objetivos = "<ul><li>Segmentar clientes según importancia y ubicación.</li><li>Visualizar clusters y cartera.</li><li>Permitir análisis y toma de decisiones.</li></ul>"
html = f"""
<!DOCTYPE html>
<html lang='es'>
<head>
<meta charset='UTF-8'>
<title>Malla de Segmentación de Clientes</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 40px; }}
h1 {{ color: #2a4d7a; }}
.kpis {{ background: #f0f4fa; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; }}
.tabla-clientes {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
.tabla-clientes th, .tabla-clientes td {{ border: 1px solid #ccc; padding: 8px 12px; }}
.tabla-clientes th {{ background: #e3eaf6; }}
tr:nth-child(even) {{ background: #f9f9f9; }}
.filtros {{ margin: 20px 0; }}
</style>
</head>
<body>
<h1>Malla de Segmentación de Clientes</h1>
<p><b>Objetivos del proyecto:</b></p>
{objetivos}
{kpi_html}
<div class='filtros'><b>Filtros (simulados):</b> Por cluster, cartera, ciudad, vendedor...</div>
{html_table}
<p style='margin-top:40px;font-size:12px;color:#888;'>Fuente: MallaClientes.xlsx | Generado automáticamente</p>
</body>
</html>
"""
with open('../malla_clientes_profesional.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Archivo HTML profesional generado como malla_clientes_profesional.html')

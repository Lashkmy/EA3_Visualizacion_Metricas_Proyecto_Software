
from pathlib import Path
import pandas as pd
import plotly.express as px

from bokeh.io import output_file, save
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

# =====================================================
# 1. CONFIGURACIÓN
# =====================================================

ROOT = Path(__file__).resolve().parents[1]

CSV_PATH = (
    ROOT / "datos" /
    "Doc02_dataset_metricas_proyecto_software.csv"
)

OUTPUT_DIR = ROOT / "visualizaciones"
OUTPUT_DIR.mkdir(exist_ok=True)

# =====================================================
# 2. CARGA DE LOS DATOS
# =====================================================

df = pd.read_csv(CSV_PATH)

columnas = [
    "Sprint",
    "Equipo",
    "Errores_Detectados",
    "Retraso_Entrega (días)",
    "Costo_Excedente ($)"
]

faltantes = [
    columna for columna in columnas
    if columna not in df.columns
]

if faltantes:
    raise ValueError(f"Faltan columnas: {faltantes}")

for columna in [
    "Sprint",
    "Errores_Detectados",
    "Retraso_Entrega (días)",
    "Costo_Excedente ($)"
]:
    df[columna] = pd.to_numeric(
        df[columna],
        errors="coerce"
    )

if df[columnas].isnull().any().any():
    raise ValueError(
        "Hay valores vacíos o no numéricos "
        "en las variables utilizadas."
    )

# =====================================================
# 3. PLOTLY
# Gráfico interactivo de retraso y costo excedente
# =====================================================

fig_plotly = px.scatter(
    df,
    x="Retraso_Entrega (días)",
    y="Costo_Excedente ($)",
    color="Equipo",
    size="Errores_Detectados",
    size_max=28,
    hover_data=[
        "Sprint",
        "Horas_Desarrollo",
        "Horas_Pruebas"
    ],
    title="Relación entre retraso de entrega y costo excedente"
)

fig_plotly.update_layout(
    xaxis_title="Retraso de entrega (días)",
    yaxis_title="Costo excedente ($)",
    legend_title="Equipo",
    template="plotly_white"
)

ruta_plotly = (
    OUTPUT_DIR / "03_plotly_retraso_costo.html"
)

fig_plotly.write_html(
    ruta_plotly,
    include_plotlyjs=True
)

print("Plotly: visualización interactiva generada.")

# =====================================================
# 4. BOKEH
# Barras interactivas del costo promedio por equipo
# =====================================================

resumen = (
    df.groupby("Equipo", as_index=False)
    .agg(
        Costo_promedio=("Costo_Excedente ($)", "mean"),
        Registros=("Sprint", "count")
    )
)

resumen["Costo_promedio"] = resumen["Costo_promedio"].round(2)

source = ColumnDataSource(resumen)

grafica = figure(
    x_range=resumen["Equipo"].astype(str).tolist(),
    title="Costo excedente promedio por equipo",
    x_axis_label="Equipo",
    y_axis_label="Costo excedente promedio ($)",
    width=850,
    height=480,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

barras = grafica.vbar(
    x="Equipo",
    top="Costo_promedio",
    width=0.6,
    source=source,
    fill_alpha=0.8
)

# Información que aparece al pasar el cursor
hover = HoverTool(
    renderers=[barras],
    tooltips=[
        ("Equipo", "@Equipo"),
        ("Costo promedio", "@Costo_promedio{0,0.00}"),
        ("Registros", "@Registros")
    ]
)

grafica.add_tools(hover)

grafica.title.text_font_size = "14pt"
grafica.xgrid.grid_line_color = None

ruta_bokeh = (
    OUTPUT_DIR / "04_bokeh_costo_equipo.html"
)

output_file(
    ruta_bokeh,
    title="Bokeh - Costo excedente por equipo"
)

save(grafica)

print("Bokeh: visualización interactiva generada.")

# =====================================================
# 5. FINALIZACIÓN
# =====================================================

print("\n========== ARCHIVOS GENERADOS ==========")
print(f"Plotly: {ruta_plotly}")
print(f"Bokeh: {ruta_bokeh}")

print("\nProceso finalizado correctamente.")
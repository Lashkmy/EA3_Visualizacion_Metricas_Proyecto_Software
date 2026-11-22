
from pathlib import Path
import urllib.request
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# ==========================================
# 1. CONFIGURACIÓN
# ==========================================

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "datos"
OUTPUT_DIR = ROOT / "visualizaciones"

GEOJSON_PATH = DATA_DIR / "ne_110m_admin_0_countries.geojson"
CSV_PATH = DATA_DIR / "world_countries_2021.csv"

OUTPUT_DIR.mkdir(exist_ok=True)

# Fuentes externas
GEOJSON_URL = (
    "https://raw.githubusercontent.com/nvkelso/"
    "natural-earth-vector/master/geojson/"
    "ne_110m_admin_0_countries.geojson"
)

CSV_URL = (
    "https://raw.githubusercontent.com/johanneswachs/"
    "OSS_Geography_Data/main/data/world_countries_2021.csv"
)

# ==========================================
# 2. DESCARGAR LOS ARCHIVOS
# ==========================================

def descargar(url, destino):
    if destino.exists():
        print(f"Archivo encontrado: {destino.name}")
        return

    print(f"Descargando {destino.name}...")

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "EA3-Software-Visualization"}
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        contenido = response.read()

    destino.write_bytes(contenido)
    print("Descarga completada.")


descargar(GEOJSON_URL, GEOJSON_PATH)
descargar(CSV_URL, CSV_PATH)

# ==========================================
# 3. LEER LOS CONJUNTOS DE DATOS
# ==========================================

world = gpd.read_file(GEOJSON_PATH)
developers = pd.read_csv(CSV_PATH)

print("\nDATOS GEOGRÁFICOS:")
print(world.shape)
print(world.columns.tolist())

print("\nDATOS DE DESARROLLO DE SOFTWARE:")
print(developers.shape)
print(developers.head())

# ==========================================
# 4. PREPARAR LAS CLAVES GEOGRÁFICAS
# ==========================================

# Se emplea el código ISO de dos letras
# para relacionar países entre ambas fuentes.

join_column = (
    "ISO_A2_EH"
    if "ISO_A2_EH" in world.columns
    else "ISO_A2"
)

world[join_column] = (
    world[join_column]
    .astype(str)
    .str.upper()
)

developers["iso2"] = (
    developers["iso2"]
    .astype(str)
    .str.upper()
)

developers["contributors_per_100k"] = pd.to_numeric(
    developers["contributors_per_100k"],
    errors="coerce"
)

# ==========================================
# 5. INTEGRAR TABLA Y GEOMETRÍAS
# ==========================================

world_data = world.merge(
    developers,
    left_on=join_column,
    right_on="iso2",
    how="left"
)

matched = world_data[
    "contributors_per_100k"
].notna().sum()

print("\nRESULTADO DE LA INTEGRACIÓN")
print("Países con información asociada:", matched)

if matched == 0:
    raise ValueError(
        "No se encontraron coincidencias entre los códigos ISO."
    )

# Guardar tabla integrada
columns_to_save = [
    "ADMIN",
    "iso2",
    "country",
    "count_total_contributors",
    "population",
    "contributors_per_100k"
]

world_data[columns_to_save].to_csv(
    OUTPUT_DIR / "datos_geograficos_software_integrados.csv",
    index=False,
    encoding="utf-8-sig"
)

# ==========================================
# 6. CREAR MAPA COROPLÉTICO
# ==========================================

fig, ax = plt.subplots(figsize=(15, 8))

world_data.plot(
    column="contributors_per_100k",
    cmap="YlOrRd",
    legend=True,
    ax=ax,
    edgecolor="white",
    linewidth=0.3,
    missing_kwds={
        "color": "lightgrey",
        "label": "Sin datos"
    },
    legend_kwds={
        "label": "Contribuidores activos por cada 100.000 habitantes",
        "shrink": 0.7
    }
)

ax.set_title(
    "Distribución geográfica de contribuidores "
    "de software de código abierto",
    fontsize=15,
    fontweight="bold"
)

ax.set_axis_off()

fig.text(
    0.5,
    0.025,
    "Fuente: Wachs et al. (2022). Datos correspondientes "
    "a la actividad 2019-2020.",
    ha="center",
    fontsize=9
)

plt.tight_layout()

# ==========================================
# 7. GUARDAR RESULTADOS
# ==========================================

output = (
    OUTPUT_DIR /
    "05_geopandas_contribuidores_github.png"
)

plt.savefig(
    output,
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("\nMAPA GEOGRÁFICO GENERADO")
print(output)

print("\nPROCESO FINALIZADO CORRECTAMENTE")

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# 1. CONFIGURACIÓN DE RUTAS
# =====================================================

ROOT = Path(__file__).resolve().parents[1]

CSV_PATH = (
    ROOT / "datos" /
    "Doc02_dataset_metricas_proyecto_software.csv"
)

OUTPUT_DIR = ROOT / "visualizaciones"
OUTPUT_DIR.mkdir(exist_ok=True)

# =====================================================
# 2. CARGA Y PREPARACIÓN DE LOS DATOS
# =====================================================

df = pd.read_csv(CSV_PATH)

columnas_numericas = [
    "Sprint",
    "Horas_Desarrollo",
    "Horas_Pruebas",
    "Errores_Detectados"
]

for columna in columnas_numericas:
    df[columna] = pd.to_numeric(
        df[columna],
        errors="coerce"
    )

if df.empty:
    raise ValueError("El archivo CSV no contiene registros.")

if df[columnas_numericas].isnull().any().any():
    raise ValueError(
        "Existen valores vacíos o no numéricos "
        "en las variables utilizadas."
    )

# =====================================================
# 3. VISUALIZACIÓN CON MATPLOTLIB
# Horas de desarrollo por sprint y equipo
# =====================================================

resumen = (
    df.groupby(["Sprint", "Equipo"], as_index=False)
    ["Horas_Desarrollo"]
    .mean()
)

fig, ax = plt.subplots(figsize=(11, 6))

for equipo in sorted(resumen["Equipo"].unique()):

    datos_equipo = resumen[
        resumen["Equipo"] == equipo
    ]

    ax.plot(
        datos_equipo["Sprint"],
        datos_equipo["Horas_Desarrollo"],
        marker="o",
        linewidth=2,
        label=equipo
    )

ax.set_title(
    "Horas de desarrollo por sprint y equipo",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Número de sprint")
ax.set_ylabel("Horas de desarrollo")

ax.set_xticks(sorted(df["Sprint"].unique()))

ax.grid(
    True,
    linestyle="--",
    alpha=0.35
)

ax.legend(title="Equipos")

fig.tight_layout()

ruta_matplotlib = (
    OUTPUT_DIR / "01_matplotlib_horas_desarrollo.png"
)

fig.savefig(
    ruta_matplotlib,
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig)

print("Matplotlib: gráfica generada correctamente.")

# =====================================================
# 4. VISUALIZACIÓN CON SEABORN
# Horas de pruebas frente a errores detectados
# =====================================================

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Horas_Pruebas",
    y="Errores_Detectados",
    hue="Equipo",
    s=100,
    alpha=0.85,
    ax=ax
)

ax.set_title(
    "Horas de pruebas y errores detectados por equipo",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Horas de pruebas")
ax.set_ylabel("Cantidad de errores detectados")

ax.grid(
    True,
    linestyle="--",
    alpha=0.35
)

ax.legend(title="Equipos")

fig.tight_layout()

ruta_seaborn = (
    OUTPUT_DIR / "02_seaborn_pruebas_errores.png"
)

fig.savefig(
    ruta_seaborn,
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig)

print("Seaborn: gráfica generada correctamente.")

# =====================================================
# 5. FINALIZACIÓN
# =====================================================

print("\n========== RESULTADOS ==========")
print(f"Gráfica Matplotlib: {ruta_matplotlib}")
print(f"Gráfica Seaborn: {ruta_seaborn}")
print("\nProceso finalizado correctamente.")
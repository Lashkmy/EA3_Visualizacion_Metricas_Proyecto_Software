
from pathlib import Path
import pandas as pd

# Rutas del proyecto
ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "datos" / "Doc02_dataset_metricas_proyecto_software.csv"
OUTPUT_DIR = ROOT / "visualizaciones"

OUTPUT_DIR.mkdir(exist_ok=True)

# Verificar que exista el archivo
if not CSV_PATH.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo CSV: {CSV_PATH}"
    )

# Cargar los datos
df = pd.read_csv(CSV_PATH)

# Verificar las columnas
columnas_esperadas = [
    "Sprint",
    "Equipo",
    "Horas_Desarrollo",
    "Horas_Pruebas",
    "Errores_Detectados",
    "Retraso_Entrega (días)",
    "Costo_Excedente ($)"
]

faltantes = [
    columna for columna in columnas_esperadas
    if columna not in df.columns
]

if faltantes:
    raise ValueError(f"Faltan columnas: {faltantes}")

# Comprobar tipos numéricos
columnas_numericas = [
    "Sprint",
    "Horas_Desarrollo",
    "Horas_Pruebas",
    "Errores_Detectados",
    "Retraso_Entrega (días)",
    "Costo_Excedente ($)"
]

for columna in columnas_numericas:
    df[columna] = pd.to_numeric(
        df[columna],
        errors="coerce"
    )

# Validación general
print("\n========== VALIDACIÓN DEL DATASET ==========")
print(f"Registros: {len(df)}")
print(f"Columnas: {len(df.columns)}")

print("\nValores vacíos por columna:")
print(df.isna().sum())

print("\nEquipos:")
print(sorted(df["Equipo"].unique()))

print("\nSprints:")
print(sorted(df["Sprint"].unique()))

# Estadísticas generales
print("\n========== ESTADÍSTICAS GENERALES ==========")
print(df[columnas_numericas].describe().round(2))

# Promedios por equipo
resumen = (
    df.groupby("Equipo")
    .agg(
        Registros=("Sprint", "count"),
        Horas_Desarrollo=("Horas_Desarrollo", "mean"),
        Horas_Pruebas=("Horas_Pruebas", "mean"),
        Errores=("Errores_Detectados", "mean"),
        Retraso_Dias=("Retraso_Entrega (días)", "mean"),
        Costo_Excedente=("Costo_Excedente ($)", "mean")
    )
    .round(2)
)

print("\n========== PROMEDIOS POR EQUIPO ==========")
print(resumen)

# Guardar resultados
ruta_salida = OUTPUT_DIR / "resumen_por_equipo.csv"

resumen.to_csv(
    ruta_salida,
    encoding="utf-8-sig"
)

print("\nArchivo generado:")
print(ruta_salida)

print("\nVALIDACIÓN FINALIZADA CORRECTAMENTE")
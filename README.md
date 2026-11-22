# 📊 Análisis y visualización de métricas de un proyecto de software

**EA3 – Visualización para la toma de decisiones**  
**Institución:** IU Digital de Antioquia  
**Programa:** Ingeniería de Software y Datos  

**Integrantes:**
- Indira Hamdam Jarava
- Cristian Vicioso Escamilla

---

## 🧭 Descripción del proyecto

Este proyecto tiene como propósito analizar y representar visualmente diferentes métricas relacionadas con la gestión y el desarrollo de un proyecto de software, utilizando herramientas de análisis de datos y visualización.

A partir de un conjunto de datos sobre equipos de desarrollo y sus resultados por sprint, se exploran variables como las horas de desarrollo, las horas de pruebas, los errores registrados, los retrasos en las entregas y los costos adicionales.

Adicionalmente, se incorpora una fuente de información geográfica sobre contribuyentes de GitHub para explorar una dimensión territorial de la actividad de desarrollo de software de código abierto.

El trabajo aplica diferentes técnicas de visualización para facilitar la exploración de los datos, reconocer patrones y presentar información que pueda apoyar la interpretación de resultados y la toma de decisiones.

## 🎯 Objetivo general

Aplicar herramientas y técnicas de visualización de datos para analizar métricas de un proyecto de software, identificar comportamientos relevantes y comunicar los resultados mediante representaciones gráficas estáticas, interactivas y geográficas.

## 🛠️ Tecnologías y herramientas

| Herramienta | Aplicación en el proyecto |
|---|---|
| Python | Lenguaje principal de desarrollo |
| Pandas | Carga, transformación y análisis de datos |
| Matplotlib | Elaboración de gráficos estáticos |
| Seaborn | Exploración de relaciones entre variables |
| Plotly | Visualizaciones interactivas |
| Bokeh | Representaciones interactivas |
| GeoPandas | Procesamiento y visualización de información geográfica |
| Visual Studio Code | Entorno de desarrollo |

## 📁 Estructura del repositorio

```text
EA3_Visualizacion_Metricas_Proyecto_Software/
│
├── codigo/
│   ├── 00_validar_datos.py
│   ├── 01_visualizaciones_estaticas.py
│   ├── 02_visualizaciones_interactivas.py
│   └── 03_visualizacion_geopandas.py
│
├── datos/
│   ├── Doc02_dataset_metricas_proyecto_software.csv
│   └── [Archivos de datos geográficos]
│
├── visualizaciones/
│   ├── 01_matplotlib_horas_desarrollo.png
│   ├── 02_seaborn_pruebas_errores.png
│   ├── 03_plotly_retraso_costo.html
│   ├── 04_bokeh_costo_equipo.html
│   └── 05_geopandas_contribuidores_github.png
│
├── informe/
│   └── [Informe académico]
│
├── guia/
│   └── [Documentación de apoyo]
│
├── video/
│   ├── audios/
│   └── evidencias/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 📈 Desarrollo y visualizaciones

El proyecto se organiza en cuatro etapas principales:

**1. Validación de los datos**

Se realiza la revisión inicial del conjunto de datos, verificando su estructura, dimensiones, tipos de variables y presencia de valores faltantes.

**2. Visualizaciones estáticas**

Se utilizan Matplotlib y Seaborn para representar métricas del proyecto y explorar comportamientos entre variables.

**3. Visualizaciones interactivas**

Se emplean Plotly y Bokeh para construir gráficos que permiten explorar la información con mayor detalle.

**4. Visualización geográfica**

Mediante GeoPandas se representa información relacionada con contribuyentes de GitHub por país, utilizando códigos ISO2 para integrar los datos geográficos.

## 🔎 Fuentes de información

El proyecto utiliza dos fuentes de datos con propósitos diferentes:

- **Métricas del proyecto de software:** conjunto de datos `Doc02_dataset_metricas_proyecto_software.csv`, que contiene registros asociados a cinco equipos y diez sprints.
- **Información geográfica:** conjunto de datos `OSS_Geography_Data`, de Johannes Wachs, junto con información de países de 2021. Se utiliza para representar la distribución geográfica de contribuyentes de GitHub.

**Nota metodológica:** las dos fuentes son independientes. No existe una variable común que permita relacionar los equipos A–E del conjunto de métricas con los países de la información geográfica. Por tanto, la visualización geográfica constituye un análisis complementario y no representa la ubicación de los equipos del proyecto.

## ⚙️ Instalación y ejecución

Para ejecutar el proyecto localmente se requiere Python y las dependencias incluidas en `requirements.txt`.

**1. Clonar el repositorio**

```bash
git clone https://github.com/Lashkmy/EA3_Visualizacion_Metricas_Proyecto_Software.git
```

**2. Ingresar a la carpeta**

```bash
cd EA3_Visualizacion_Metricas_Proyecto_Software
```

**3. Crear un entorno virtual**

```bash
python -m venv .venv
```

**4. Activar el entorno virtual en Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**5. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**6. Ejecutar los scripts**

Desde la carpeta raíz del proyecto:

```bash
python codigo/00_validar_datos.py
python codigo/01_visualizaciones_estaticas.py
python codigo/02_visualizaciones_interactivas.py
python codigo/03_visualizacion_geopandas.py
```

Los archivos de entrada deben encontrarse en las ubicaciones esperadas por los scripts dentro de la carpeta `datos`.

## 📌 Consideraciones del análisis

- El conjunto principal contiene 50 registros correspondientes a diez sprints y cinco equipos.
- Los resultados describen los datos disponibles y no permiten establecer relaciones causales.
- Las horas, los errores, los retrasos y los costos no son suficientes por sí solos para determinar la productividad o el rendimiento integral de un equipo.
- La información geográfica corresponde a una fuente independiente y tiene sus propias limitaciones de cobertura y periodo.
- Las visualizaciones interactivas se generan en formato HTML y pueden abrirse desde un navegador web.

## 👥 Autores

**Indira Hamdam Jarava**  
**Cristian Vicioso Escamilla**

Ingeniería de Software y Datos  
IU Digital de Antioquia

---

*Proyecto académico desarrollado en el marco de la actividad EA3 de la asignatura Visualización para la toma de decisiones.*
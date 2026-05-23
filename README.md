# aqualimpia-analytics
Proyecto analítico para el tratamiento de aguas residuales
# 💧 Sistema Integrado de Monitoreo Analítico — AquaLimpia S.A.

Este proyecto presenta una solución integral de ciencia de datos y software para el monitoreo operativo y ambiental de las plantas de tratamiento de aguas residuales de **AquaLimpia S.A.** El sistema automatiza la ingesta de datos crudos, realiza análisis estadísticos descriptivos avanzados y despliega un dashboard interactivo para la toma de decisiones.

## 🚀 Características del Proyecto
- **Procesamiento Automatizado (`src/data_processing.py`):** Limpieza, ordenamiento temporal y estructuración de datos desde fuentes en formato Excel.
- **Análisis Estadístico (`src/utils_analytics.py`):** Funciones modulares para el cálculo de eficiencia avanzada de remoción de carga orgánica ($DBO$) y métricas descriptivas (media, moda mediante SciPy).
- **Dashboard Interactivo (`src/app_dashboard.py`):** Interfaz gráfica web moderna construida con **Streamlit** que permite filtrar por planta, visualizar KPIs operativos y analizar gráficos de cumplimiento normativo respecto al límite legal (35 mg/L).

---

## 📂 Estructura del Repositorio
- `data/raw/`: Datos crudos de origen.
- `data/processed/`: Reportes de salida generados automáticamente por el script (`reporte_operaciones_plantas.csv` y `reporte_gestion_ambiental.csv`).
- `src/`: Código fuente modular del sistema.
- `requirements.txt`: Librerías y dependencias necesarias para el entorno de ejecución.

---

## 🛠️ Instalación y Ejecución

Siga estos pasos para replicar el entorno de desarrollo de forma local:

### 1. Clonar el repositorio e instalar dependencias
```bash
git clone <ENLACE_DE_TU_REPOSITORIO>
cd "Pagina HTML"
pip install -r requirements.txt

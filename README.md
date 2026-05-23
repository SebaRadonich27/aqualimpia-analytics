# Documentación del Proyecto: Sistema Analítico AquaLimpia S. A.

## 1. Objetivos del Proyecto
* **Objetivo General:** Desarrollar un ecosistema analítico automatizado y reproducible para monitorear los niveles de Demanda Biológica de Oxígeno (DBO) y optimizar la toma de decisiones operativas y ambientales.
* **Objetivos Específicos:**
  * **Automatizar el proceso ETL:** Diseñar un script en Python que limpie, ordene y procese los datos crudos de las plantas.
  * **Centralizar métricas de eficiencia:** Calcular automáticamente el porcentaje de remoción de carga orgánica contaminante.
  * **Segmentar la información:** Generar reportes independientes y específicos para el Área de Operaciones y el Área de Gestión Ambiental.

---

## 2. Metodología y Proceso Operativo
El proyecto implementa una arquitectura estructurada de ciencia de datos dividida en tres etapas clave:

1. **Ingesta e Ingeniería de Variables (`src/data_processing.py`):** El script lee el dataset inmutable desde la ruta de datos crudos (`data/raw/`), normaliza las fechas al orden cronológico correcto y calcula de forma matemática el indicador de rendimiento operativo mediante la fórmula:

$$\text{Eficiencia DBO (\%)} = \left( \frac{\text{DBO Entrada} - \text{DBO Salida}}{\text{DBO Entrada}} \right) \times 100$$

2. **Generación de Reportes Segmentados (`data/processed/`):**
   Para disolver silos de información, el flujo de datos exporta de manera automatizada dos archivos independientes:
   * `reporte_operaciones_plantas.csv`: Contiene caudales, carga de DBO, lodos generados y energía consumida en aireación.
   * `reporte_gestion_ambiental.csv`: Contiene la fecha, la planta, la DBO de salida del agua tratada y su estado explícito de cumplimiento normativo.

3. **Visualización Interactiva (`src/app_dashboard.py`):**
   Uso de **Streamlit** para desplegar un panel gerencial interactivo que permite filtrar datos por planta y rangos de fecha, facilitando el análisis visual mediante curvas temporales de calidad del agua y gráficos de dispersión multivariables.

---

## 3. Resultados Obtenidos
* **Gobernanza y Reproducibilidad:** Se eliminó por completo la manipulación manual de planillas, reduciendo el riesgo de error humano a cero y blindando técnicamente a la empresa ante fiscalizaciones ambientales.
* **Sustento de Inversiones:** El análisis cruzado entre el caudal entrante y el consumo energético en aireación permite a la gerencia identificar qué plantas están trabajando al límite de su capacidad para justificar inversiones en infraestructura.
* **Código Estructurado:** El proyecto quedó organizado bajo un estándar profesional en el entorno local (carpetas `data` y `src`), listo para ser integrado y escalado en cualquier momento.
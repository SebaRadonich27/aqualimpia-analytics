import os
import sys
import pandas as pd

# Fuerza a Python a buscar módulos en la carpeta actual (src)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils_analytics import calcular_eficiencia_avanzada, obtener_metricas_estadisticas

def ejecutar_analisis():
    ruta_entrada = 'data/raw/dataset_set_A_aguas_residuales.xlsx'
    if not os.path.exists(ruta_entrada): return

    # Cargar y ordenar datos
    df = pd.read_excel(ruta_entrada)
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
    df = df.sort_values(by='fecha_registro').reset_index(drop=True)

    # REUTILIZACIÓN MODULAR
    df['eficiencia_remocion_DBO_pct'] = calcular_eficiencia_avanzada(df, 'DBO_entrada_mg_L', 'DBO_salida_mg_L')
    stats_globales = obtener_metricas_estadisticas(df, 'eficiencia_remocion_DBO_pct')

    # Imprimir resumen de control en terminal
    print(f"📊 Eficiencia Promedio: {stats_globales['Media']}% | Moda: {stats_globales['Moda']}%")

    # Exportar resultados de forma automatizada
    os.makedirs('data/processed', exist_ok=True)
    
    # Reporte Operaciones
    # # Reporte Operaciones (Asegúrate de que termine en .to_csv)
    df[['fecha_registro', 'planta', 'caudal_entrada_m3_d', 'DBO_entrada_mg_L', 'DBO_salida_mg_L', 'eficiencia_remocion_DBO_pct']].to_csv('data/processed/reporte_operaciones_plantas.csv', index=False)
    
    # # Reporte Ambiental
    df[['fecha_registro', 'planta', 'DBO_salida_mg_L']].to_csv('data/processed/reporte_gestion_ambiental.csv', index=False)
    
    print("✅ Reportes generados con éxito.")

if __name__ == "__main__":
    ejecutar_analisis()
import numpy as np
from scipy import stats

def calcular_eficiencia_avanzada(df, col_entrada, col_salida):
    """Calcula el % de remoción de DBO evitando divisiones por cero."""
    entrada = df[col_entrada].astype(float)
    salida = df[col_salida].astype(float)
    eficiencia = np.where(entrada > 0, ((entrada - salida) / entrada) * 100, np.nan)
    return np.round(eficiencia, 2)

def obtener_metricas_estadisticas(df, col_analisis):
    """Calcula media, moda (SciPy) y varianza del indicador."""
    datos = df[col_analisis].dropna()
    moda_res = stats.mode(datos, keepdims=True)
    return {
        "Media": round(np.mean(datos), 2),
        "Moda": round(float(moda_res.mode[0]), 2) if len(moda_res.mode) > 0 else np.nan,
        "Varianza": round(np.var(datos, ddof=1), 2)
    }
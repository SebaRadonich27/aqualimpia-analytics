import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="AquaLimpia S.A. - Dashboard", layout="wide")

# Rutas fijas relativas directas
ruta_operaciones = 'data/processed/reporte_operaciones_plantas.csv'
ruta_ambiental = 'data/processed/reporte_gestion_ambiental.csv'

st.title("💧 Sistema Integrado de Monitoreo Analítico — AquaLimpia S.A.")
st.markdown("---")

if not os.path.exists(ruta_operaciones) or not os.path.exists(ruta_ambiental):
    st.error("❌ Archivos procesados no encontrados. Ejecuta primero 'python src/data_processing.py' en la terminal.")
else:
    # Cargar datos procesados
    df_ops = pd.read_csv(ruta_operaciones)
    df_amb = pd.read_csv(ruta_ambiental)
    
    df_ops['fecha_registro'] = pd.to_datetime(df_ops['fecha_registro'])
    df_amb['fecha_registro'] = pd.to_datetime(df_amb['fecha_registro'])

    # Filtro lateral de planta
    st.sidebar.header("🎛️ Filtros de Control")
    planta_seleccionada = st.sidebar.selectbox("Seleccione la Planta:", sorted(df_ops['planta'].unique()))

    df_ops_filt = df_ops[df_ops['planta'] == planta_seleccionada]
    df_amb_filt = df_amb[df_amb['planta'] == planta_seleccionada]

    # Despliegue de KPIs
    st.subheader(f"📊 Indicadores Clave — {planta_seleccionada}")
    c1, c2, c3 = st.columns(3)
    c1.metric("Eficiencia Promedio DBO", f"{df_ops_filt['eficiencia_remocion_DBO_pct'].mean():.2f}%")
    c2.metric("Caudal Promedio Diario", f"{df_ops_filt['caudal_entrada_m3_d'].mean():.1f} m³/d")
    
    # Cálculo automático de cumplimiento normativo (Si es menor o igual a 35 mg/L, cumple)
    total = len(df_amb_filt)
    cumplen = len(df_amb_filt[df_amb_filt['DBO_salida_mg_L'] <= 35])
    tasa = (cumplen / total) * 100 if total > 0 else 0
    c3.metric("Tasa Cumplimiento Normatividad", f"{tasa:.1f}%")

    st.markdown("---")

    # Gráficos de análisis
    col_izq, col_der = st.columns(2)

    with col_izq:
        st.subheader("🌿 Monitoreo Ambiental Temporal")
        fig, ax = plt.subplots(figsize=(7, 4))
        sns.lineplot(data=df_amb_filt, x='fecha_registro', y='DBO_salida_mg_L', ax=ax, color='teal', marker='o', label='DBO Salida Real')
        ax.axhline(y=35, color='red', linestyle='--', label='Límite Normativo (35 mg/L)')
        plt.xticks(rotation=45)
        ax.legend()
        st.pyplot(fig)

    with col_der:
        st.subheader("⚙️ Relación Operativa de Cargas")
        fig, ax = plt.subplots(figsize=(7, 4))
        
        # Validamos si existen las columnas de lodos, si no, graficamos Entrada vs Salida de DBO
        if 'lodos_generados_kg_d' in df_ops_filt.columns:
            scatter = ax.scatter(df_ops_filt['caudal_entrada_m3_d'], df_ops_filt['lodos_generados_kg_d'], c=df_ops_filt['energia_aeracion_kWh'] if 'energia_aeracion_kWh' in df_ops_filt else None, cmap='viridis')
            ax.set_xlabel("Caudal (m³/d)")
            ax.set_ylabel("Lodos Generados (kg/d)")
            if 'energia_aeracion_kWh' in df_ops_filt:
                fig.colorbar(scatter, ax=ax).set_label('Energía Aireación (kWh)')
        else:
            # Gráfico de contingencia operativo: Carga de Entrada vs Carga de Salida
            scatter = ax.scatter(df_ops_filt['DBO_entrada_mg_L'], df_ops_filt['DBO_salida_mg_L'], color='coral', alpha=0.7, edgecolors='black')
            ax.set_xlabel("DBO Entrada (mg/L)")
            ax.set_ylabel("DBO Salida (mg/L)")
            ax.grid(True, linestyle='--', alpha=0.5)
            
        st.pyplot(fig)
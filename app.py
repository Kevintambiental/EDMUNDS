"""
EDMUNDS v3.0 - Versión Profesional de Ingeniería
Environmental Dispersion Modeling for Underground Natural Soil Systems
Software de modelado de dispersión de contaminantes en suelos - Nivel Ingeniería
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import sys
import os
from datetime import datetime

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from cundinamarca_ucs import CUNDINAMARCA_UCS, get_ucs_parameters, get_all_ucs_list
from contaminant_catalog import CONTAMINANT_CATALOG, get_contaminant_data, get_all_contaminants
from transport_equations import (
    ogata_banks_solution, calculate_longitudinal_dispersion,
    calculate_transverse_dispersion, detect_concentration_change,
    model_concentration_profile, calculate_plume_front,
    calculate_max_concentration_zone, partition_equation,
    calculate_darcy_velocity, calculate_linear_velocity
)
from segment_modeling import (
    calculate_segment_models, calculate_concentration_profile_by_segments,
    calculate_contaminant_front_progression, calculate_cross_section_concentration,
    calculate_3d_plume_detailed, calculate_attenuation
)
from plume_3d import create_3d_grid, calculate_3d_concentration, identify_plume_zones


# Configuración de la página profesional
st.set_page_config(
    page_title="EDMUNDS v3.0 - Sistema Profesional de Modelado",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS profesional de ingeniería
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        margin: 1rem;
    }
    .engineering-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-card {
        background: #f8f9fa;
        border-left: 5px solid #1e3c72;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .parameter-table {
        background: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .ucs-selector {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    div[data-testid="stTabs"] [role="tablist"] {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 10px;
        padding: 0.5rem;
    }
    div[data-testid="stTabs"] [role="tab"] {
        color: white;
        font-weight: 600;
        padding: 0.5rem 1rem;
    }
    div[data-testid="stTabs"] [aria-selected="true"] {
        background: rgba(255,255,255,0.2) !important;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .success-alert {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        border-left: 5px solid #009688;
        padding: 1rem;
        border-radius: 8px;
        color: #00695c;
    }
    .warning-alert {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        border-left: 5px solid #ff9800;
        padding: 1rem;
        border-radius: 8px;
        color: #e65100;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Inicializar variables de sesión profesional"""
    if 'selected_ucs' not in st.session_state:
        st.session_state.selected_ucs = []
    if 'ucs_active' not in st.session_state:
        st.session_state.ucs_active = {}
    if 'simulation_results' not in st.session_state:
        st.session_state.simulation_results = {}
    if 'segment_spacing' not in st.session_state:
        st.session_state.segment_spacing = 20  # metros por defecto


def main():
    initialize_session_state()
    
    # Header profesional
    st.markdown("""
    <div class="engineering-header">
        <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700;">🌍 EDMUNDS v3.0</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">
            Environmental Dispersion Modeling for Underground Natural Soil Systems
        </p>
        <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">
            Sistema Profesional de Modelado de Dispersión de Contaminantes en Suelos
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar profesional
    with st.sidebar:
        st.markdown("### 🎯 Navegación Principal")
        
        page = st.radio(
            "Seleccione el módulo:",
            [
                "🗺️ Selección de UCS",
                "⚙️ Configuración del Modelo",
                "📊 Modelado por Tramos",
                "🌐 Modelado 3D Avanzado",
                "📈 Análisis Comparativo",
                "📋 Normativas",
                "💾 Reportes Profesionales"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("### ℹ️ Información del Sistema")
        
        if st.session_state.selected_ucs:
            st.info(f"**UCS Seleccionadas:** {len(st.session_state.selected_ucs)}")
            for ucs in st.session_state.selected_ucs:
                ucs_data = get_ucs_parameters(ucs)
                if ucs_data:
                    st.write(f"• {ucs_data['name']}")
    
    # Router de páginas
    if page == "🗺️ Selección de UCS":
        ucs_selection_page()
    elif page == "⚙️ Configuración del Modelo":
        model_configuration_page()
    elif page == "📊 Modelado por Tramos":
        segment_modeling_page()
    elif page == "🌐 Modelado 3D Avanzado":
        advanced_3d_modeling_page()
    elif page == "📈 Análisis Comparativo":
        comparative_analysis_page()
    elif page == "📋 Normativas":
        regulatory_page()
    elif page == "💾 Reportes Profesionales":
        professional_reports_page()


def ucs_selection_page():
    """Página de selección de Unidades Cartográficas de Suelo"""
    st.markdown('<h2 style="color: #1e3c72; margin-bottom: 1rem;">🗺️ Selección de Unidades Cartográficas de Suelo (UCS)</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
        <p><strong>Estudio General de Suelos de Cundinamarca - IGAC (2000)</strong></p>
        <p>Seleccione las UCS que desea modelar. Cada UCS tendrá su propia gráfica de modelado.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_by_elevation = st.selectbox(
            "Filtrar por elevación:",
            ["Todas", "0-500 m", "500-1500 m", "1500-2500 m", "2500-3500 m", ">3500 m"]
        )
    
    with col2:
        filter_by_texture = st.selectbox(
            "Filtrar por textura:",
            ["Todas", "Arcilloso", "Arenoso", "Franco", "Franco limoso", "Franco arcilloso"]
        )
    
    with col3:
        filter_by_drainage = st.selectbox(
            "Filtrar por drenaje:",
            ["Todas", "Bien drenado", "Moderadamente bien drenado", "Pobremente drenado"]
        )
    
    # Mostrar UCS disponibles
    st.markdown("### 📋 Unidades Cartográficas Disponibles")
    
    ucs_list = get_all_ucs_list()
    
    # Crear tabla interactiva de UCS
    ucs_data = []
    for ucs_code in ucs_list:
        ucs = get_ucs_parameters(ucs_code)
        if ucs:
            ucs_data.append({
                "Código": ucs_code,
                "Nombre": ucs["name"],
                "Ubicación": ucs["location"],
                "Elevación": ucs["elevation_range"],
                "Textura": ucs["texture"],
                "Drenaje": ucs["drainage"],
                "MO (%)": ucs["hydraulic_properties"]["organic_matter_percent"],
                "Seleccionar": False
            })
    
    df_ucs = pd.DataFrame(ucs_data)
    
    # Mostrar tabla con selección
    edited_df = st.data_editor(
        df_ucs,
        column_config={
            "Seleccionar": st.column_config.CheckboxColumn(
                "Seleccionar",
                help="Marque para incluir esta UCS en el modelado"
            )
        },
        hide_index=True,
        use_container_width=True,
        height=400
    )
    
    # Botón para aplicar selección
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("✅ Aplicar Selección de UCS", type="primary", use_container_width=True):
            selected = edited_df[edited_df["Seleccionar"] == True]["Código"].tolist()
            st.session_state.selected_ucs = selected
            
            # Inicializar estado activo para cada UCS
            for ucs in selected:
                st.session_state.ucs_active[ucs] = True
            
            st.success(f"✅ {len(selected)} UCS seleccionadas para modelado")
    
    # Mostrar UCS seleccionadas
    if st.session_state.selected_ucs:
        st.markdown("---")
        st.markdown("### ✅ UCS Seleccionadas para Modelado")
        
        for ucs_code in st.session_state.selected_ucs:
            ucs = get_ucs_parameters(ucs_code)
            if ucs:
                with st.expander(f"🌍 {ucs_code} - {ucs['name']}", expanded=False):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Ubicación:** {ucs['location']}")
                        st.write(f"**Elevación:** {ucs['elevation_range']}")
                        st.write(f"**Clima:** {ucs['climate']}")
                    
                    with col2:
                        st.write(f"**Textura:** {ucs['texture']}")
                        st.write(f"**Drenaje:** {ucs['drainage']}")
                        st.write(f"**Pendiente:** {ucs['slope']}")
                    
                    # Parámetros hidráulicos
                    st.markdown("#### 🔬 Parámetros Hidráulicos")
                    props = ucs["hydraulic_properties"]
                    params_df = pd.DataFrame({
                        "Parámetro": ["Porosidad Total", "Porosidad Efectiva", "K (cm/d)", 
                                     "Capacidad de Campo", "Punto de Marchitez", "MO (%)", "pH"],
                        "Valor": [
                            f"{props['total_porosity']:.3f}",
                            f"{props['effective_porosity']:.3f}",
                            f"{props['hydraulic_conductivity_cm_d']:.2f}",
                            f"{props['field_capacity']:.3f}",
                            f"{props['wilting_point']:.3f}",
                            f"{props['organic_matter_percent']:.1f}",
                            f"{props['ph']:.1f}"
                        ]
                    })
                    st.dataframe(params_df, use_container_width=True, hide_index=True)
                    
                    # Control de activación
                    is_active = st.session_state.ucs_active.get(ucs_code, True)
                    if st.checkbox(f"Activar {ucs_code} para visualización", value=is_active, key=f"active_{ucs_code}"):
                        st.session_state.ucs_active[ucs_code] = not is_active


def model_configuration_page():
    """Página de configuración del modelo"""
    st.markdown('<h2 style="color: #1e3c72; margin-bottom: 1rem;">⚙️ Configuración del Modelo</h2>', unsafe_allow_html=True)
    
    if not st.session_state.selected_ucs:
        st.warning("⚠️ Primero seleccione las UCS en la pestaña 'Selección de UCS'")
        return
    
    # Configuración del contaminante
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #1e3c72;">☣️ Configuración del Contaminante</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        contaminant_type = st.selectbox(
            "Tipo de Contaminante:",
            ["Todos", "Hidrocarburo", "Metal pesado", "Solvente", "Pesticida"]
        )
        
        # Filtrar catálogo
        if contaminant_type == "Todos":
            available_contaminants = get_all_contaminants()
        else:
            from contaminant_catalog import get_contaminants_by_type
            available_contaminants = get_contaminants_by_type(contaminant_type)
        
        contaminant_name = st.selectbox(
            "Contaminante:",
            available_contaminants,
            format_func=lambda x: get_contaminant_data(x)["name"] if get_contaminant_data(x) else x
        )
    
    with col2:
        contaminant_data = get_contaminant_data(contaminant_name)
        
        if contaminant_data:
            st.markdown("#### 📊 Propiedades del Contaminante")
            props_df = pd.DataFrame({
                "Propiedad": ["Tipo", "Estado", "Solubilidad (mg/L)", "Koc (L/kg)", 
                              "Volatilidad", "Persistencia", "Toxicidad", "Reactivo"],
                "Valor": [
                    contaminant_data["type"],
                    contaminant_data["state"],
                    f"{contaminant_data['solubility_mg_L']:.2f}",
                    f"{contaminant_data['Koc_L_kg']:.1f}",
                    contaminant_data["volatility"],
                    contaminant_data["persistence"],
                    contaminant_data["toxicity"],
                    "Sí" if contaminant_data["reactive"] else "No"
                ]
            })
            st.dataframe(props_df, use_container_width=True, hide_index=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Configuración de concentración inicial
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #1e3c72;">💧 Concentración Inicial</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        C0 = st.number_input(
            "Concentración Inicial C0 (mg/L):",
            min_value=0.001,
            max_value=100000.0,
            value=100.0,
            step=1.0,
            format="%.3f"
        )
    
    with col2:
        injection_type = st.selectbox(
            "Tipo de Inyección:",
            ["continua", "momentanea"],
            format_func=lambda x: "Continua" if x == "continua" else "Momentánea"
        )
    
    with col3:
        initial_volume = st.number_input(
            "Volumen Inicial (L):",
            min_value=0.1,
            max_value=10000.0,
            value=100.0,
            step=10.0
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Configuración de condiciones hidráulicas
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #1e3c72;">🌊 Condiciones Hidráulicas</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        hydraulic_gradient = st.slider(
            "Gradiente Hidráulico (i):",
            min_value=0.001,
            max_value=0.5,
            value=0.01,
            step=0.001,
            format="%.4f"
        )
        
        scale = st.selectbox(
            "Escala del Modelo:",
            ["laboratory", "field_small", "field_large"],
            format_func=lambda x: {
                "laboratory": "Laboratorio (cm)",
                "field_small": "Campo Pequeño (m)",
                "field_large": "Campo Grande (m)"
            }[x]
        )
    
    with col2:
        # Mostrar valores calculados para cada UCS seleccionada
        st.markdown("#### 📊 Cálculos por UCS")
        
        for ucs_code in st.session_state.selected_ucs:
            if st.session_state.ucs_active.get(ucs_code, True):
                ucs = get_ucs_parameters(ucs_code)
                if ucs:
                    K = ucs["hydraulic_properties"]["hydraulic_conductivity_cm_d"]
                    me = ucs["hydraulic_properties"]["effective_porosity"]
                    
                    Vd = calculate_darcy_velocity(K, hydraulic_gradient)
                    V = calculate_linear_velocity(Vd, me)
                    
                    st.write(f"**{ucs_code}:** V = {V:.4f} cm/d")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Configuración de tiempo y espacio
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #1e3c72;">⏱️ Tiempo y Espacio</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        time_days = st.slider(
            "Tiempo de Simulación (días):",
            min_value=1,
            max_value=3650,
            value=365,
            step=1
        )
        
        segment_spacing_m = st.number_input(
            "Espaciado entre Tramos (metros):",
            min_value=5,
            max_value=100,
            value=20,
            step=5
        )
        
        st.session_state.segment_spacing = segment_spacing_m
    
    with col2:
        total_distance_m = st.number_input(
            "Distancia Total de Modelado (metros):",
            min_value=10,
            max_value=10000,
            value=100,
            step=10
        )
        
        spatial_resolution = st.slider(
            "Resolución Espacial (puntos):",
            min_value=50,
            max_value=500,
            value=200,
            step=10
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Guardar configuración
    st.markdown("---")
    if st.button("💾 Guardar Configuración", type="primary", use_container_width=True):
        st.session_state.config = {
            "contaminant": contaminant_name,
            "C0": C0,
            "injection_type": injection_type,
            "hydraulic_gradient": hydraulic_gradient,
            "scale": scale,
            "time_days": time_days,
            "segment_spacing_m": segment_spacing_m,
            "total_distance_m": total_distance_m,
            "spatial_resolution": spatial_resolution
        }
        st.success("✅ Configuración guardada")


def segment_modeling_page():
    """Página de modelado por tramos"""
    st.markdown('<h2 style="color: #1e3c72; margin-bottom: 1rem;">📊 Modelado por Tramos</h2>', unsafe_allow_html=True)
    
    if not st.session_state.selected_ucs:
        st.warning("⚠️ Primero seleccione las UCS en la pestaña 'Selección de UCS'")
        return
    
    if 'config' not in st.session_state:
        st.warning("⚠️ Primero configure el modelo en la pestaña 'Configuración del Modelo'")
        return
    
    config = st.session_state.config
    
    # Selector de UCS para visualizar
    st.markdown('<div class="ucs-selector">', unsafe_allow_html=True)
    st.markdown("### 🎯 Seleccione la UCS para Visualizar")
    
    active_ucs = [ucs for ucs in st.session_state.selected_ucs if st.session_state.ucs_active.get(ucs, True)]
    
    selected_ucs_to_view = st.selectbox(
        "UCS a visualizar:",
        active_ucs,
        format_func=lambda x: f"{x} - {get_ucs_parameters(x)['name']}"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Ejecutar modelado para la UCS seleccionada
    if st.button("🚀 Ejecutar Modelado por Tramos", type="primary", use_container_width=True):
        with st.spinner("Ejecutando modelado por tramos..."):
            ucs = get_ucs_parameters(selected_ucs_to_view)
            if ucs:
                # Calcular parámetros
                K = ucs["hydraulic_properties"]["hydraulic_conductivity_cm_d"]
                me = ucs["hydraulic_properties"]["effective_porosity"]
                Vd = calculate_darcy_velocity(K, config["hydraulic_gradient"])
                V = calculate_linear_velocity(Vd, me)
                
                # Calcular dispersión
                from soil_parameters import get_dispersivity
                dispersivity = get_dispersivity(config["scale"])
                DL = calculate_longitudinal_dispersion(dispersivity['longitudinal'] * 100, V)
                DT = calculate_transverse_dispersion(dispersivity['transverse'] * 100, V)
                
                # Modelar por tramos
                total_distance_cm = config["total_distance_m"] * 100
                segment_spacing_cm = config["segment_spacing_m"] * 100
                
                segment_models = calculate_segment_models(
                    total_distance_cm, segment_spacing_cm, config["C0"], V, DL, config["time_days"]
                )
                
                # Guardar resultados
                st.session_state.simulation_results[selected_ucs_to_view] = {
                    "segment_models": segment_models,
                    "V": V,
                    "DL": DL,
                    "DT": DT,
                    "C0": config["C0"],
                    "time_days": config["time_days"],
                    "total_distance_m": config["total_distance_m"],
                    "segment_spacing_m": config["segment_spacing_m"]
                }
                
                st.success(f"✅ Modelado completado para {selected_ucs_to_view}")
    
    # Mostrar resultados si existen
    if selected_ucs_to_view in st.session_state.simulation_results:
        results = st.session_state.simulation_results[selected_ucs_to_view]
        
        # Resumen de tramos
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #1e3c72;">📋 Resumen de Tramos</h3>', unsafe_allow_html=True)
        
        segment_df = pd.DataFrame.from_dict(results["segment_models"], orient='index')
        segment_df = segment_df.reset_index().rename(columns={"index": "Tramo"})
        
        st.dataframe(segment_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Gráfica de concentración por tramos
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #1e3c72;">📈 Concentración por Tramo</h3>', unsafe_allow_html=True)
        
        fig = go.Figure()
        
        x_positions = segment_df["position_m"]
        concentrations = segment_df["concentration_mg_L"]
        
        fig.add_trace(go.Scatter(
            x=x_positions,
            y=concentrations,
            mode='lines+markers',
            name='Concentración',
            line=dict(color='#1e3c72', width=3),
            marker=dict(size=10, color='#1e3c72')
        ))
        
        # Marcar tramos donde el contaminante llegó
        reached_segments = segment_df[segment_df["contaminant_reached"]]
        fig.add_trace(go.Scatter(
            x=reached_segments["position_m"],
            y=reached_segments["concentration_mg_L"],
            mode='markers',
            name='Contaminante llegó',
            marker=dict(size=15, color='red', symbol='circle'),
            text=reached_segments["Tramo"],
            textposition="top center"
        ))
        
        fig.update_layout(
            title=f"Concentración por Tramo - {selected_ucs_to_view}",
            xaxis_title="Distancia (m)",
            yaxis_title="Concentración (mg/L)",
            hovermode='x unified',
            template='plotly_white',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Gráfica de tiempo de llegada
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #1e3c72;">⏱️ Tiempo de Llegada por Tramo</h3>', unsafe_allow_html=True)
        
        arrival_data = segment_df[segment_df["arrival_time_days"].notna()]
        
        if len(arrival_data) > 0:
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=arrival_data["position_m"],
                y=arrival_data["arrival_time_days"],
                mode='lines+markers',
                name='Tiempo de llegada',
                line=dict(color='#2a5298', width=3),
                marker=dict(size=10, color='#2a5298')
            ))
            
            fig2.update_layout(
                title="Tiempo de Llegada del Contaminante por Tramo",
                xaxis_title="Distancia (m)",
                yaxis_title="Tiempo (días)",
                template='plotly_white',
                height=500
            )
            
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("El contaminante no ha llegado a ningún tramo en el tiempo simulado")
        
        st.markdown('</div>', unsafe_allow_html=True)


def advanced_3d_modeling_page():
    """Página de modelado 3D avanzado"""
    st.markdown('<h2 style="color: #1e3c72; margin-bottom: 1rem;">🌐 Modelado 3D Avanzado</h2>', unsafe_allow_html=True)
    
    if not st.session_state.selected_ucs:
        st.warning("⚠️ Primero seleccione las UCS en la pestaña 'Selección de UCS'")
        return
    
    if 'config' not in st.session_state:
        st.warning("⚠️ Primero configure el modelo en la pestaña 'Configuración del Modelo'")
        return
    
    # Selector de UCS
    active_ucs = [ucs for ucs in st.session_state.selected_ucs if st.session_state.ucs_active.get(ucs, True)]
    selected_ucs_to_view = st.selectbox(
        "UCS para modelado 3D:",
        active_ucs,
        format_func=lambda x: f"{x} - {get_ucs_parameters(x)['name']}"
    )
    
    # Configuración 3D
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #1e3c72;">🎛️ Configuración 3D</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        width_m = st.number_input("Ancho transversal (m):", min_value=1, max_value=1000, value=50)
        depth_m = st.number_input("Profundidad (m):", min_value=0.1, max_value=100, value=10)
    
    with col2:
        resolution_3d = st.slider("Resolución 3D:", min_value=20, max_value=100, value=50, step=5)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 Ejecutar Modelado 3D", type="primary", use_container_width=True):
        with st.spinner("Generando modelo 3D..."):
            # Implementar modelado 3D
            st.info("Modelado 3D en desarrollo - Se requiere implementación completa")


def comparative_analysis_page():
    """Página de análisis comparativo"""
    st.markdown('<h2 style="color: #1e3c72; margin-bottom: 1rem;">📈 Análisis Comparativo</h2>', unsafe_allow_html=True)
    
    st.info("Análisis comparativo en desarrollo")


def regulatory_page():
    """Página de normativas"""
    st.markdown('<h2 style="color: #1e3c72; margin-bottom: 1rem;">📋 Normativas y Límites Permisibles</h2>', unsafe_allow_html=True)
    
    from contaminant_catalog import CONTAMINANT_CATALOG
    
    regulatory_data = []
    for key, data in CONTAMINANT_CATALOG.items():
        regulatory_data.append({
            "Contaminante": data["name"],
            "Tipo": data["type"],
            "Límite (μg/g)": data["regulatory_limit_ug_g"],
            "Toxicidad": data["toxicity"],
            "Persistencia": data["persistence"]
        })
    
    df_reg = pd.DataFrame(regulatory_data)
    st.dataframe(df_reg, use_container_width=True, hide_index=True)


def professional_reports_page():
    """Página de reportes profesionales"""
    st.markdown('<h2 style="color: #1e3c72; margin-bottom: 1rem;">💾 Generación de Reportes Profesionales</h2>', unsafe_allow_html=True)
    
    st.info("Reportes profesionales en desarrollo")


if __name__ == "__main__":
    main()

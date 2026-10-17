"""
EDMUNDS - Modelado por Tramos (Segment Modeling)
Modela la dispersión en múltiples secciones a lo largo de la distancia total
"""

import numpy as np
from .transport_equations import ogata_banks_solution, detect_concentration_change
from .contaminant_catalog import get_contaminant_data


def calculate_segment_models(total_distance_cm, segment_spacing_cm, C0, V, DL, time_days):
    """
    Calcular modelos de concentración para cada tramo/segmento.
    
    Args:
        total_distance_cm: float - Distancia total a modelar (cm)
        segment_spacing_cm: float - Espaciado entre tramos (cm)
        C0: float - Concentración inicial (mg/L)
        V: float - Velocidad lineal (cm/d)
        DL: float - Dispersión longitudinal (cm²/d)
        time_days: float - Tiempo de simulación (días)
    
    Returns:
        dict - Diccionario con datos de cada tramo
    """
    # Calcular posiciones de los tramos
    segment_positions = np.arange(segment_spacing_cm, total_distance_cm + segment_spacing_cm, segment_spacing_cm)
    
    segment_models = {}
    
    for i, x_position in enumerate(segment_positions):
        # Calcular concentración en esta posición
        C_at_position = ogata_banks_solution(C0, x_position, time_days, V, DL)
        
        # Determinar si el contaminante ha llegado a este punto
        reached = C_at_position > 0.001 * C0  # Umbral del 0.1% de C0
        
        # Calcular tiempo de llegada (cuando C > 0.01*C0)
        arrival_time = None
        if reached:
            # Buscar el tiempo cuando la concentración supera el 1% de C0
            for t in np.linspace(1, time_days, 100):
                C_temp = ogata_banks_solution(C0, x_position, t, V, DL)
                if C_temp >= 0.01 * C0:
                    arrival_time = t
                    break
        
        segment_models[f"segment_{i+1}"] = {
            "position_cm": x_position,
            "position_m": x_position / 100,
            "concentration_mg_L": C_at_position,
            "relative_concentration": C_at_position / C0 if C0 > 0 else 0,
            "contaminant_reached": reached,
            "arrival_time_days": arrival_time,
            "distance_from_source_m": x_position / 100
        }
    
    return segment_models


def calculate_concentration_profile_by_segments(total_distance_cm, segment_spacing_cm, C0, V, DL, time_days):
    """
    Calcular perfil de concentración completo con marcadores de tramos.
    
    Args:
        total_distance_cm: float - Distancia total (cm)
        segment_spacing_cm: float - Espaciado entre tramos (cm)
        C0: float - Concentración inicial (mg/L)
        V: float - Velocidad lineal (cm/d)
        DL: float - Dispersión longitudinal (cm²/d)
        time_days: float - Tiempo (días)
    
    Returns:
        tuple: (x_array, C_array, segment_positions)
    """
    x_array = np.linspace(0, total_distance_cm, 500)
    C_array = []
    
    for x in x_array:
        C = ogata_banks_solution(C0, x, time_days, V, DL)
        C_array.append(C)
    
    segment_positions = np.arange(segment_spacing_cm, total_distance_cm + segment_spacing_cm, segment_spacing_cm)
    
    return x_array, np.array(C_array), segment_positions


def calculate_contaminant_front_progression(C0, V, DL, total_distance_cm, time_array):
    """
    Calcular la progresión del frente de contaminante en el tiempo.
    
    Args:
        C0: float - Concentración inicial (mg/L)
        V: float - Velocidad lineal (cm/d)
        DL: float - Dispersión longitudinal (cm²/d)
        total_distance_cm: float - Distancia máxima (cm)
        time_array: array - Array de tiempos (días)
    
    Returns:
        dict - Posición del frente en cada tiempo
    """
    front_progression = {}
    
    for t in time_array:
        # Calcular dónde está el frente (donde C = 0.01*C0)
        front_position = 0
        for x in np.linspace(0, total_distance_cm, 200):
            C = ogata_banks_solution(C0, x, t, V, DL)
            if C >= 0.01 * C0:
                front_position = x
            else:
                break
        
        front_progression[f"day_{int(t)}"] = {
            "time_days": t,
            "front_position_cm": front_position,
            "front_position_m": front_position / 100,
            "percentage_of_total": (front_position / total_distance_cm) * 100 if total_distance_cm > 0 else 0
        }
    
    return front_progression


def calculate_cross_section_concentration(x_position, transverse_range_cm, C0, V, DL, DT, time_days):
    """
    Calcular concentración en sección transversal (corte perpendicular al flujo).
    
    Args:
        x_position: float - Posición longitudinal (cm)
        transverse_range_cm: tuple - (min, max) rango transversal (cm)
        C0: float - Concentración inicial (mg/L)
        V: float - Velocidad lineal (cm/d)
        DL: float - Dispersión longitudinal (cm²/d)
        DT: float - Dispersión transversal (cm²/d)
        time_days: float - Tiempo (días)
    
    Returns:
        tuple: (y_array, C_transverse_array)
    """
    y_array = np.linspace(transverse_range_cm[0], transverse_range_cm[1], 100)
    C_transverse_array = []
    
    # Centro de la pluma en este tiempo
    x_center = V * time_days
    
    for y in y_array:
        # Modelo gaussiano simplificado para dispersión transversal
        sigma = np.sqrt(2 * DT * time_days)
        C = C0 * np.exp(-(y**2) / (2 * sigma**2)) * ogata_banks_solution(C0, x_position, time_days, V, DL)
        C_transverse_array.append(C)
    
    return y_array, np.array(C_transverse_array)


def calculate_3d_plume_detailed(total_distance_cm, total_width_cm, total_depth_cm, C0, V, DL, DT, time_days, resolution=50):
    """
    Calcular pluma 3D detallada con zonas de concentración.
    
    Args:
        total_distance_cm: float - Distancia longitudinal (cm)
        total_width_cm: float - Ancho transversal (cm)
        total_depth_cm: float - Profundidad (cm)
        C0: float - Concentración inicial (mg/L)
        V: float - Velocidad lineal (cm/d)
        DL: float - Dispersión longitudinal (cm²/d)
        DT: float - Dispersión transversal (cm²/d)
        time_days: float - Tiempo (días)
        resolution: int - Resolución del grid
    
    Returns:
        dict - Datos 3D completos con zonas identificadas
    """
    # Crear grid 3D
    x = np.linspace(0, total_distance_cm, resolution)
    y = np.linspace(-total_width_cm/2, total_width_cm/2, resolution)
    z = np.linspace(0, total_depth_cm, resolution//2)
    
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    
    # Calcular concentración 3D
    C_3d = np.zeros_like(X)
    
    x_center = V * time_days
    sigma_x = np.sqrt(2 * DL * time_days)
    sigma_yz = np.sqrt(2 * DT * time_days)
    
    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(len(z)):
                # Distancia radial en plano transversal
                r = np.sqrt(Y[i,j,k]**2 + Z[i,j,k]**2)
                
                # Modelo gaussian 3D
                exponent_x = -((X[i,j,k] - x_center)**2) / (2 * sigma_x**2)
                exponent_r = -(r**2) / (2 * sigma_yz**2)
                
                norm_factor = C0 / ((2 * np.pi)**(3/2) * sigma_x * sigma_yz**2)
                C_3d[i,j,k] = norm_factor * np.exp(exponent_x + exponent_r)
    
    # Identificar zonas
    high_concentration = C_3d >= (0.5 * C0)
    mixing_zone = (C_3d < (0.5 * C0)) & (C_3d >= (0.1 * C0))
    dispersion_zone = C_3d < (0.1 * C0)
    
    # Calcular estadísticas
    max_conc = np.max(C_3d)
    max_conc_location = np.unravel_index(np.argmax(C_3d), C_3d.shape)
    
    # Calcular volumen de cada zona
    volume_total = total_distance_cm * total_width_cm * total_depth_cm
    volume_high = np.sum(high_concentration) * (total_distance_cm/resolution) * (total_width_cm/resolution) * (total_depth_cm/(resolution//2))
    volume_mixing = np.sum(mixing_zone) * (total_distance_cm/resolution) * (total_width_cm/resolution) * (total_depth_cm/(resolution//2))
    volume_dispersion = np.sum(dispersion_zone) * (total_distance_cm/resolution) * (total_width_cm/resolution) * (total_depth_cm/(resolution//2))
    
    return {
        "X": X,
        "Y": Y,
        "Z": Z,
        "C_3d": C_3d,
        "high_concentration_zone": high_concentration,
        "mixing_zone": mixing_zone,
        "dispersion_zone": dispersion_zone,
        "max_concentration": max_conc,
        "max_concentration_location": {
            "x_cm": x[max_conc_location[0]],
            "y_cm": y[max_conc_location[1]],
            "z_cm": z[max_conc_location[2]]
        },
        "zone_volumes": {
            "high_cm3": volume_high,
            "mixing_cm3": volume_mixing,
            "dispersion_cm3": volume_dispersion,
            "total_cm3": volume_total
        },
        "front_position_cm": x_center + 3 * sigma_x  # Frente aprox a 3σ
    }


def calculate_attenuation(C0, C_current, contaminant_name, time_days):
    """
    Calcular atenuación natural y asistida del contaminante.
    
    Args:
        C0: float - Concentración inicial (mg/L)
        C_current: float - Concentración actual (mg/L)
        contaminant_name: str - Nombre del contaminante
        time_days: float - Tiempo transcurrido (días)
    
    Returns:
        dict - Datos de atenuación
    """
    contaminant = get_contaminant_data(contaminant_name)
    
    if contaminant is None:
        return None
    
    degradation_rate = contaminant.get("degradation_rate_d", 0.0)
    is_reactive = contaminant.get("reactive", False)
    
    # Atenuación natural
    if degradation_rate > 0:
        C_natural = C0 * np.exp(-degradation_rate * time_days)
    else:
        C_natural = C0
    
    # Atenuación por retardo (si es reactivo)
    if is_reactive:
        retardation = contaminant.get("retardation_factor", 1.0)
        C_retarded = C_current / retardation
    else:
        C_retarded = C_current
    
    # Atenuación total
    total_attenuation = (C0 - C_current) / C0 if C0 > 0 else 0
    
    # Clasificar tipo de atenuación
    if degradation_rate > 0.05:
        attenuation_type = "Atenuación natural rápida"
    elif degradation_rate > 0.01:
        attenuation_type = "Atenuación natural moderada"
    elif degradation_rate > 0:
        attenuation_type = "Atenuación natural lenta"
    else:
        attenuation_type = "No hay atenuación natural significativa"
    
    return {
        "initial_concentration": C0,
        "current_concentration": C_current,
        "natural_attenuation_concentration": C_natural,
        "retarded_concentration": C_retarded,
        "total_attenuation_percent": total_attenuation * 100,
        "attenuation_type": attenuation_type,
        "degradation_rate_d": degradation_rate,
        "is_reactive": is_reactive,
        "retardation_factor": contaminant.get("retardation_factor", 1.0) if is_reactive else 1.0,
        "persistence": contaminant.get("persistence", "Desconocido")
    }

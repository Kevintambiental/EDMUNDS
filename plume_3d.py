"""
EDMUNDS - 3D Plume Modeling Module
Modelado 3D de la pluma de contaminante
"""

import numpy as np
from .transport_equations import ogata_banks_solution, calculate_transverse_dispersion


def create_3d_grid(x_range, y_range, z_range, resolution=50):
    """
    Crear grid 3D para modelado.
    
    Args:
        x_range: tuple - (min, max) en dirección del flujo (cm)
        y_range: tuple - (min, max) dirección transversal (cm)
        z_range: tuple - (min, max) profundidad (cm)
        resolution: int - Número de puntos por dimensión
    
    Returns:
        tuple: (X, Y, Z) arrays 3D
    """
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    z = np.linspace(z_range[0], z_range[1], resolution)
    
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    return X, Y, Z


def calculate_3d_concentration(C0, X, Y, Z, t, v, DL, DT, source_point=(0, 0, 0)):
    """
    Calcular concentración en 3D usando solución advectivo-dispersiva.
    
    Modelo: C(x,y,z,t) basado en solución 3D de Ogata-Banks extendida
    
    Args:
        C0: float - Concentración inicial (mg/L)
        X, Y, Z: arrays - Grid 3D (cm)
        t: float - Tiempo (días)
        v: float - Velocidad lineal media (cm/d)
        DL: float - Dispersión longitudinal (cm²/d)
        DT: float - Dispersión transversal (cm²/d)
        source_point: tuple - (x0, y0, z0) posición de la fuente
    
    Returns:
        array - Concentración 3D (mg/L)
    """
    x0, y0, z0 = source_point
    
    # Distancias desde la fuente
    dx = X - x0
    dy = Y - y0
    dz = Z - z0
    
    # Distancia radial en el plano transversal
    r = np.sqrt(dy**2 + dz**2)
    
    # Solución 3D aproximada (Gaussian plume model)
    if t <= 0:
        return np.zeros_like(X)
    
    # Centro de la pluma
    x_center = v * t
    
    # Dispersión longitudinal
    sigma_x = np.sqrt(2 * DL * t)
    
    # Dispersión transversal
    sigma_r = np.sqrt(2 * DT * t)
    
    # Modelo Gaussian 3D
    exponent_x = -((dx - x_center)**2) / (2 * sigma_x**2)
    exponent_r = -(r**2) / (2 * sigma_r**2)
    
    # Factor de normalización
    norm_factor = C0 / ((2 * np.pi)**(3/2) * sigma_x * sigma_r**2)
    
    C = norm_factor * np.exp(exponent_x + exponent_r)
    
    return C


def identify_plume_zones(C, C0, threshold_high=0.5, threshold_low=0.01):
    """
    Identificar zonas de la pluma: alta concentración, mezcla, dispersión.
    
    Args:
        C: array - Concentración 3D (mg/L)
        C0: float - Concentración inicial (mg/L)
        threshold_high: float - Umbral zona alta (default: 50% de C0)
        threshold_low: float - Umbral zona baja (default: 1% de C0)
    
    Returns:
        dict - Diccionario con arrays booleanos para cada zona
    """
    high_zone = C >= (C0 * threshold_high)
    mixing_zone = (C < (C0 * threshold_high)) & (C >= (C0 * threshold_low))
    dispersion_zone = C < (C0 * threshold_low)
    
    return {
        "high_concentration": high_zone,
        "mixing": mixing_zone,
        "dispersion": dispersion_zone,
    }


def calculate_plume_volume(C, C_threshold, dx, dy, dz):
    """
    Calcular volumen de la pluma sobre un umbral de concentración.
    
    Args:
        C: array - Concentración 3D (mg/L)
        C_threshold: float - Umbral de concentración (mg/L)
        dx, dy, dz: float - Espaciado del grid (cm)
    
    Returns:
        float - Volumen (cm³)
    """
    above_threshold = C >= C_threshold
    n_points = np.sum(above_threshold)
    volume = n_points * dx * dy * dz
    return volume


def calculate_plume_center_of_mass(C, X, Y, Z):
    """
    Calcular centro de masa de la pluma.
    
    Args:
        C: array - Concentración 3D (mg/L)
        X, Y, Z: arrays - Grid 3D (cm)
    
    Returns:
        tuple: (x_cm, y_cm, z_cm) centro de masa (cm)
    """
    total_mass = np.sum(C)
    
    if total_mass == 0:
        return 0, 0, 0
    
    x_cm = np.sum(C * X) / total_mass
    y_cm = np.sum(C * Y) / total_mass
    z_cm = np.sum(C * Z) / total_mass
    
    return x_cm, y_cm, z_cm


def calculate_plume_statistics(C, C0):
    """
    Calcular estadísticas de la pluma.
    
    Args:
        C: array - Concentración 3D (mg/L)
        C0: float - Concentración inicial (mg/L)
    
    Returns:
        dict - Estadísticas
    """
    stats = {
        "max_concentration": np.max(C),
        "min_concentration": np.min(C),
        "mean_concentration": np.mean(C),
        "std_concentration": np.std(C),
        "total_mass": np.sum(C),
        "relative_max": np.max(C) / C0 if C0 > 0 else 0,
        "volume_above_01": np.sum(C >= 0.01 * C0),
        "volume_above_1": np.sum(C >= 0.01 * C0),
        "volume_above_10": np.sum(C >= 0.10 * C0),
        "volume_above_50": np.sum(C >= 0.50 * C0),
    }
    return stats


def export_plume_data(C, X, Y, Z, filepath):
    """
    Exportar datos de la pluma a archivo CSV.
    
    Args:
        C: array - Concentración 3D (mg/L)
        X, Y, Z: arrays - Grid 3D (cm)
        filepath: str - Ruta del archivo de salida
    """
    # Aplanar arrays
    C_flat = C.flatten()
    X_flat = X.flatten()
    Y_flat = Y.flatten()
    Z_flat = Z.flatten()
    
    # Crear DataFrame
    import pandas as pd
    df = pd.DataFrame({
        'x_cm': X_flat,
        'y_cm': Y_flat,
        'z_cm': Z_flat,
        'concentration_mg_L': C_flat,
    })
    
    # Guardar
    df.to_csv(filepath, index=False)
    return len(df)

"""
EDMUNDS - Transport Equations Module
Ecuaciones de transporte de contaminantes en suelos
Incluye: Fick, Ogata-Banks, función error complementaria
"""

import numpy as np
from scipy.special import erfc
from math import sqrt, pi, exp


def error_function(x):
    """
    Función error erf(x) usando la aproximación dada por el profesor.
    
    Fórmula: erf(x) = SIGNO(x) * sqrt(1 - exp(-x² * 4/pi + 0.147*x² / (1 + 0.147*x²)))
    
    Args:
        x: float - Argumento
    
    Returns:
        float - Valor de erf(x)
    """
    if x == 0:
        return 0.0
    
    sign = 1 if x > 0 else -1
    x_sq = x ** 2
    numerator = 4 / pi + 0.147 * x_sq
    denominator = 1 + 0.147 * x_sq
    result = sqrt(1 - exp(-x_sq * numerator / denominator))
    
    return sign * result


def ogata_banks_solution(C0, x, t, v, DL):
    """
    Solución de Ogata-Banks para transporte advectivo-dispersivo.
    
    Fórmula: C(x,t) = (C0/2) * erfc((x - vt) / (2 * sqrt(DL * t)))
    
    Args:
        C0: float - Concentración inicial (mg/L)
        x: float - Distancia (cm)
        t: float - Tiempo (días)
        v: float - Velocidad lineal media (cm/d)
        DL: float - Coeficiente de dispersión longitudinal (cm²/d)
    
    Returns:
        float - Concentración en posición x y tiempo t (mg/L)
    """
    if t <= 0:
        return 0.0
    
    argument = (x - v * t) / (2 * sqrt(DL * t))
    return (C0 / 2) * erfc(argument)


def first_fick_law(D, dC_dx):
    """
    Primera ley de Fick para difusión.
    
    Fórmula: F = -D * (dC/dx)
    
    Args:
        D: float - Coeficiente de difusión (cm²/d)
        dC_dx: float - Gradiente de concentración (mg/L·cm)
    
    Returns:
        float - Flujo de masa (mg/cm²·d)
    """
    return -D * dC_dx


def second_fick_law_derivative(C, x, t, D):
    """
    Segunda ley de Fick (ecuación diferencial parcial).
    
    Fórmula: ∂C/∂t = D * (∂²C/∂x²)
    
    Esta función calcula el lado derecho de la ecuación.
    
    Args:
        C: array - Concentración en diferentes posiciones
        x: array - Posiciones (cm)
        t: float - Tiempo (días)
        D: float - Coeficiente de difusión (cm²/d)
    
    Returns:
        float - Tasa de cambio de concentración
    """
    dx = x[1] - x[0]
    d2C_dx2 = np.gradient(np.gradient(C, dx), dx)
    return D * d2C_dx2


def diffusion_solution(C0, x, t, D_star):
    """
    Solución de difusión pura (primera ley de Fick).
    
    Fórmula: C(x,t) = C0 * erfc(x / (2 * sqrt(D* * t)))
    
    Args:
        C0: float - Concentración inicial (mg/L)
        x: float - Distancia (cm)
        t: float - Tiempo (días)
        D_star: float - Coeficiente de difusión efectiva (cm²/d)
    
    Returns:
        float - Concentración en posición x y tiempo t (mg/L)
    """
    if t <= 0:
        return 0.0
    
    argument = x / (2 * sqrt(D_star * t))
    return C0 * erfc(argument)


def calculate_dispersion_coefficient(alpha, v):
    """
    Calcular coeficiente de dispersión hidrodinámica.
    
    Fórmula: D = α * v
    
    Args:
        alpha: float - Dispersividad (cm)
        v: float - Velocidad del flujo (cm/d)
    
    Returns:
        float - Coeficiente de dispersión (cm²/d)
    """
    return alpha * v


def calculate_longitudinal_dispersion(alpha_L, v):
    """
    Calcular dispersión longitudinal.
    
    Args:
        alpha_L: float - Dispersividad longitudinal (cm)
        v: float - Velocidad del flujo (cm/d)
    
    Returns:
        float - Coeficiente de dispersión longitudinal (cm²/d)
    """
    return alpha_L * v


def calculate_transverse_dispersion(alpha_T, v):
    """
    Calcular dispersión transversal.
    
    Args:
        alpha_T: float - Dispersividad transversal (cm)
        v: float - Velocidad del flujo (cm/d)
    
    Returns:
        float - Coeficiente de dispersión transversal (cm²/d)
    """
    return alpha_T * v


def detect_concentration_change(previous_C, current_C, decimal_places=3):
    """
    Detectar cambio en concentración con precisión de n decimales.
    
    Args:
        previous_C: float - Concentración anterior
        current_C: float - Concentración actual
        decimal_places: int - Número de decimales a considerar (default: 3)
    
    Returns:
        tuple: (changed: bool, difference: float)
    """
    rounded_prev = round(previous_C, decimal_places)
    rounded_curr = round(current_C, decimal_places)
    changed = rounded_prev != rounded_curr
    difference = abs(current_C - previous_C)
    return changed, difference


def partition_equation(C_solid, C_liquid, C_gas):
    """
    Ecuación de partición de contaminante.
    
    Fórmula: CT = C_solid + C_liquid + C_gas
    
    Args:
        C_solid: float - Concentración en fase sólida (mg/kg)
        C_liquid: float - Concentración en fase líquida (mg/L)
        C_gas: float - Concentración en fase gaseosa (mg/L)
    
    Returns:
        float - Concentración total (mg/kg equivalente)
    """
    return C_solid + C_liquid + C_gas


def model_concentration_profile(C0, x_array, t, v, DL):
    """
    Modelar perfil de concentración en 1D para un tiempo dado.
    
    Args:
        C0: float - Concentración inicial (mg/L)
        x_array: array - Array de posiciones (cm)
        t: float - Tiempo (días)
        v: float - Velocidad lineal media (cm/d)
        DL: float - Coeficiente de dispersión longitudinal (cm²/d)
    
    Returns:
        array - Concentración en cada posición (mg/L)
    """
    concentrations = []
    for x in x_array:
        C = ogata_banks_solution(C0, x, t, v, DL)
        concentrations.append(C)
    return np.array(concentrations)


def calculate_plume_front(C0, threshold_ratio=0.01, t=0, v=0, DL=0):
    """
    Calcular el frente de avance de la pluma de contaminante.
    
    El frente se define como la posición donde la concentración
    cae al 1% de la concentración inicial.
    
    Args:
        C0: float - Concentración inicial (mg/L)
        threshold_ratio: float - Ratio umbral (default: 0.01 = 1%)
        t: float - Tiempo (días)
        v: float - Velocidad lineal media (cm/d)
        DL: float - Coeficiente de dispersión longitudinal (cm²/d)
    
    Returns:
        float - Posición del frente (cm)
    """
    threshold = C0 * threshold_ratio
    
    # Búsqueda binaria para encontrar el frente
    x_min = 0
    x_max = v * t + 10 * sqrt(DL * t)  # Estimación inicial
    
    for _ in range(50):  # 50 iteraciones suficientes
        x_mid = (x_min + x_max) / 2
        C_mid = ogata_banks_solution(C0, x_mid, t, v, DL)
        
        if C_mid > threshold:
            x_min = x_mid
        else:
            x_max = x_mid
    
    return x_max


def calculate_max_concentration_zone(C0, t, v, DL):
    """
    Calcular la zona de alta concentración (pico).
    
    Args:
        C0: float - Concentración inicial (mg/L)
        t: float - Tiempo (días)
        v: float - Velocidad lineal media (cm/d)
        DL: float - Coeficiente de dispersión longitudinal (cm²/d)
    
    Returns:
        tuple: (position_cm, concentration_mg_L)
    """
    # El pico ocurre en x = v * t para Ogata-Banks
    x_peak = v * t
    C_peak = ogata_banks_solution(C0, x_peak, t, v, DL)
    return x_peak, C_peak

"""
EDMUNDS - Soil Parameters Module
Parámetros de suelo basados en investigación bibliográfica
Fuentes: USDA, FAO, Rawls & Brakensiek, Cosby et al.
"""

import numpy as np

# Parámetros de suelo por textura (USDA)
# Basado en Rawls & Brakensiek (1983) y Cosby et al. (1984)
SOIL_PARAMETERS = {
    "sand": {
        "name": "Arena",
        "total_porosity": 0.437,
        "effective_porosity": 0.417,
        "hydraulic_conductivity_cm_h": 23.56,
        "hydraulic_conductivity_cm_d": 565.44,
        "field_capacity": 0.091,
        "wilting_point": 0.033,
        "bulk_density": 1.55,
        "particle_density": 2.65,
        "c_exponent": 1.3,  # Para arenas no consolidadas
    },
    "loamy_sand": {
        "name": "Arena limosa",
        "total_porosity": 0.437,
        "effective_porosity": 0.401,
        "hydraulic_conductivity_cm_h": 5.98,
        "hydraulic_conductivity_cm_d": 143.52,
        "field_capacity": 0.125,
        "wilting_point": 0.055,
        "bulk_density": 1.60,
        "particle_density": 2.65,
        "c_exponent": 1.3,
    },
    "sandy_loam": {
        "name": "Franco arenoso",
        "total_porosity": 0.453,
        "effective_porosity": 0.412,
        "hydraulic_conductivity_cm_h": 2.18,
        "hydraulic_conductivity_cm_d": 52.32,
        "field_capacity": 0.207,
        "wilting_point": 0.095,
        "bulk_density": 1.50,
        "particle_density": 2.65,
        "c_exponent": 1.3,
    },
    "loam": {
        "name": "Franco",
        "total_porosity": 0.463,
        "effective_porosity": 0.434,
        "hydraulic_conductivity_cm_h": 1.32,
        "hydraulic_conductivity_cm_d": 31.68,
        "field_capacity": 0.270,
        "wilting_point": 0.117,
        "bulk_density": 1.40,
        "particle_density": 2.65,
        "c_exponent": 1.5,
    },
    "silt_loam": {
        "name": "Franco limoso",
        "total_porosity": 0.501,
        "effective_porosity": 0.486,
        "hydraulic_conductivity_cm_h": 0.68,
        "hydraulic_conductivity_cm_d": 16.32,
        "field_capacity": 0.330,
        "wilting_point": 0.133,
        "bulk_density": 1.30,
        "particle_density": 2.65,
        "c_exponent": 1.5,
    },
    "sandy_clay_loam": {
        "name": "Franco arcilloso arenoso",
        "total_porosity": 0.398,
        "effective_porosity": 0.330,
        "hydraulic_conductivity_cm_h": 0.12,
        "hydraulic_conductivity_cm_d": 2.88,
        "field_capacity": 0.255,
        "wilting_point": 0.148,
        "bulk_density": 1.60,
        "particle_density": 2.70,
        "c_exponent": 1.8,
    },
    "clay_loam": {
        "name": "Franco arcilloso",
        "total_porosity": 0.464,
        "effective_porosity": 0.309,
        "hydraulic_conductivity_cm_h": 0.08,
        "hydraulic_conductivity_cm_d": 1.92,
        "field_capacity": 0.318,
        "wilting_point": 0.207,
        "bulk_density": 1.40,
        "particle_density": 2.70,
        "c_exponent": 1.9,
    },
    "silty_clay_loam": {
        "name": "Franco arcilloso limoso",
        "total_porosity": 0.471,
        "effective_porosity": 0.432,
        "hydraulic_conductivity_cm_h": 0.08,
        "hydraulic_conductivity_cm_d": 1.92,
        "field_capacity": 0.360,
        "wilting_point": 0.210,
        "bulk_density": 1.35,
        "particle_density": 2.70,
        "c_exponent": 1.9,
    },
    "sandy_clay": {
        "name": "Arcilloso arenoso",
        "total_porosity": 0.430,
        "effective_porosity": 0.321,
        "hydraulic_conductivity_cm_h": 0.05,
        "hydraulic_conductivity_cm_d": 1.20,
        "field_capacity": 0.310,
        "wilting_point": 0.230,
        "bulk_density": 1.55,
        "particle_density": 2.75,
        "c_exponent": 2.0,
    },
    "silty_clay": {
        "name": "Arcilloso limoso",
        "total_porosity": 0.479,
        "effective_porosity": 0.423,
        "hydraulic_conductivity_cm_h": 0.04,
        "hydraulic_conductivity_cm_d": 0.96,
        "field_capacity": 0.370,
        "wilting_point": 0.250,
        "bulk_density": 1.40,
        "particle_density": 2.75,
        "c_exponent": 2.0,
    },
    "clay": {
        "name": "Arcilla",
        "total_porosity": 0.475,
        "effective_porosity": 0.385,
        "hydraulic_conductivity_cm_h": 0.02,
        "hydraulic_conductivity_cm_d": 0.48,
        "field_capacity": 0.360,
        "wilting_point": 0.270,
        "bulk_density": 1.45,
        "particle_density": 2.75,
        "c_exponent": 2.0,
    },
}

# Coeficientes de difusión molecular en agua (25°C) para contaminantes comunes
# Basado en EPA y literatura científica
DIFFUSION_COEFFICIENTS = {
    "benzene": 1.02e-5,  # cm²/s
    "toluene": 8.60e-6,
    "ethylbenzene": 7.80e-6,
    "xylene": 7.50e-6,
    "mtbe": 9.40e-6,
    "chloroform": 1.10e-5,
    "tce": 9.20e-6,
    "pce": 8.00e-6,
    "default": 1.00e-5,  # Valor por defecto para contaminantes orgánicos
}

# Valores de dispersividad (α) según escala
# Basado en Gelhar et al. (1992) y literatura de transporte
DISPERSIVITY_VALUES = {
    "laboratory": {
        "longitudinal": 0.01,  # cm
        "transverse": 0.001,   # cm
    },
    "field_small": {
        "longitudinal": 0.1,  # m
        "transverse": 0.01,   # m
    },
    "field_large": {
        "longitudinal": 1.0,  # m
        "transverse": 0.1,    # m
    },
}

# Normativas de concentración máxima permisible (μg/g = ppm)
# Basado en EPA RSL y estándares internacionales
REGULATORY_LIMITS = {
    "arsenic": 16.0,
    "lead": 450.0,
    "cadmium": 7.5,
    "chromium_vi": 19.0,
    "mercury": 0.73,
    "nickel": 130.0,
    "copper": 1720.0,
    "zinc": 2480.0,
    "benzene": 0.23,
    "toluene": 0.69,
    "ethylbenzene": 1.7,
    "xylene": 0.19,
    "tce": 0.2,
    "pce": 2.3,
    "default": 1.0,  # Valor por defecto
}


def get_soil_parameters(soil_type):
    """
    Obtener parámetros de suelo por tipo de textura.
    
    Args:
        soil_type: str - Tipo de suelo (clave de SOIL_PARAMETERS)
    
    Returns:
        dict - Parámetros del suelo
    """
    return SOIL_PARAMETERS.get(soil_type.lower(), SOIL_PARAMETERS["loam"])


def get_diffusion_coefficient(contaminant):
    """
    Obtener coeficiente de difusión molecular para un contaminante.
    
    Args:
        contaminant: str - Nombre del contaminante
    
    Returns:
        float - Coeficiente de difusión en cm²/s
    """
    return DIFFUSION_COEFFICIENTS.get(contaminant.lower(), DIFFUSION_COEFFICIENTS["default"])


def get_dispersivity(scale="field_small"):
    """
    Obtener valores de dispersividad según escala.
    
    Args:
        scale: str - Escala del modelo (laboratory, field_small, field_large)
    
    Returns:
        dict - Dispersividad longitudinal y transversal
    """
    return DISPERSIVITY_VALUES.get(scale, DISPERSIVITY_VALUES["field_small"])


def get_regulatory_limit(contaminant):
    """
    Obtener límite regulatorio para un contaminante.
    
    Args:
        contaminant: str - Nombre del contaminante
    
    Returns:
        float - Límite máximo permisible en μg/g
    """
    return REGULATORY_LIMITS.get(contaminant.lower(), REGULATORY_LIMITS["default"])


def calculate_effective_diffusion(Dm, me, c_exponent):
    """
    Calcular coeficiente de difusión efectiva D*.
    
    Fórmula: D* = Dm * (me)^c
    
    Args:
        Dm: float - Coeficiente de difusión molecular (cm²/s)
        me: float - Porosidad efectiva
        c_exponent: float - Exponente (1.3-2.0 según tipo de suelo)
    
    Returns:
        float - Coeficiente de difusión efectiva (cm²/s)
    """
    return Dm * (me ** c_exponent)


def calculate_darcy_velocity(K, i):
    """
    Calcular velocidad de Darcy.
    
    Fórmula: Vd = K * i
    
    Args:
        K: float - Conductividad hidráulica (cm/d)
        i: float - Gradiente hidráulico (adimensional)
    
    Returns:
        float - Velocidad de Darcy (cm/d)
    """
    return K * i


def calculate_linear_velocity(Vd, me):
    """
    Calcular velocidad lineal media.
    
    Fórmula: V = Vd / me
    
    Args:
        Vd: float - Velocidad de Darcy (cm/d)
        me: float - Porosidad efectiva
    
    Returns:
        float - Velocidad lineal media (cm/d)
    """
    return Vd / me


def calculate_advective_flux(me, C, V):
    """
    Calcular flujo de masa por advección.
    
    Fórmula: J = me * C * V
    
    Args:
        me: float - Porosidad efectiva
        C: float - Concentración (mg/L)
        V: float - Velocidad lineal media (cm/d)
    
    Returns:
        float - Flujo de masa (mg/cm²·d)
    """
    return me * C * V

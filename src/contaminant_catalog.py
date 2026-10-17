"""
EDMUNDS - Catálogo Completo de Contaminantes de Suelo
Incluye hidrocarburos, metales pesados, solventes, pesticidas, etc.
Basado en EPA, ATSDR, y literatura científica
"""

import numpy as np

# Catálogo completo de contaminantes
CONTAMINANT_CATALOG = {
    # HIDROCARBUROS DEL PETRÓLEO
    
    "gasoline": {
        "name": "Gasolina",
        "type": "Hidrocarburo",
        "cas": "8006-61-9",
        "molecular_weight": 105.0,
        "state": "Líquido",
        "solubility_mg_L": 175.0,
        "diffusion_coefficient_cm2_s": 9.4e-6,
        "henry_constant": 0.28,
        "Koc_L_kg": 85.0,
        "Kd_L_kg": 2.55,
        "log_kow": 2.73,
        "density_g_cm3": 0.72,
        "viscosity_cP": 0.6,
        "regulatory_limit_ug_g": 0.5,
        "volatility": "Alta",
        "persistence": "Moderada",
        "toxicity": "Alta",
        "components": ["benceno", "tolueno", "etilbenceno", "xileno"],
        "reactive": True,
        "retardation_factor": 1.8,
        "degradation_rate_d": 0.05
    },
    
    "diesel": {
        "name": "Diésel",
        "type": "Hidrocarburo",
        "cas": "68334-30-5",
        "molecular_weight": 200.0,
        "state": "Líquido",
        "solubility_mg_L": 5.0,
        "diffusion_coefficient_cm2_s": 5.2e-6,
        "henry_constant": 0.01,
        "Koc_L_kg": 5000.0,
        "Kd_L_kg": 150.0,
        "log_kow": 5.0,
        "density_g_cm3": 0.85,
        "viscosity_cP": 3.5,
        "regulatory_limit_ug_g": 100.0,
        "volatility": "Baja",
        "persistence": "Alta",
        "toxicity": "Moderada",
        "components": ["alcanos C10-C20", "aromáticos"],
        "reactive": False,
        "retardation_factor": 5.5,
        "degradation_rate_d": 0.01
    },
    
    "crude_oil": {
        "name": "Petróleo Crudo",
        "type": "Hidrocarburo",
        "cas": "8002-05-9",
        "molecular_weight": 250.0,
        "state": "Líquido viscoso",
        "solubility_mg_L": 0.05,
        "diffusion_coefficient_cm2_s": 2.0e-6,
        "henry_constant": 0.001,
        "Koc_L_kg": 10000.0,
        "Kd_L_kg": 300.0,
        "log_kow": 6.5,
        "density_g_cm3": 0.88,
        "viscosity_cP": 50.0,
        "regulatory_limit_ug_g": 500.0,
        "volatility": "Muy baja",
        "persistence": "Muy alta",
        "toxicity": "Moderada",
        "components": ["alcanos", "cicloalcanos", "aromáticos", "resinas", "asfaltenos"],
        "reactive": False,
        "retardation_factor": 10.0,
        "degradation_rate_d": 0.005
    },
    
    "benzene": {
        "name": "Benceno",
        "type": "Hidrocarburo aromático",
        "cas": "71-43-2",
        "molecular_weight": 78.11,
        "state": "Líquido",
        "solubility_mg_L": 1790.0,
        "diffusion_coefficient_cm2_s": 1.02e-5,
        "henry_constant": 0.23,
        "Koc_L_kg": 146.0,
        "Kd_L_kg": 4.38,
        "log_kow": 2.13,
        "density_g_cm3": 0.88,
        "viscosity_cP": 0.65,
        "regulatory_limit_ug_g": 0.23,
        "volatility": "Alta",
        "persistence": "Moderada",
        "toxicity": "Muy alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 2.2,
        "degradation_rate_d": 0.08
    },
    
    "toluene": {
        "name": "Tolueno",
        "type": "Hidrocarburo aromático",
        "cas": "108-88-3",
        "molecular_weight": 92.14,
        "state": "Líquido",
        "solubility_mg_L": 526.0,
        "diffusion_coefficient_cm2_s": 8.6e-6,
        "henry_constant": 0.28,
        "Koc_L_kg": 234.0,
        "Kd_L_kg": 7.02,
        "log_kow": 2.73,
        "density_g_cm3": 0.87,
        "viscosity_cP": 0.59,
        "regulatory_limit_ug_g": 0.69,
        "volatility": "Alta",
        "persistence": "Moderada",
        "toxicity": "Alta",
        "reactive": True,
        "retardation_factor": 2.5,
        "degradation_rate_d": 0.07
    },
    
    "ethylbenzene": {
        "name": "Etilbenceno",
        "type": "Hidrocarburo aromático",
        "cas": "100-41-4",
        "molecular_weight": 106.17,
        "state": "Líquido",
        "solubility_mg_L": 152.0,
        "diffusion_coefficient_cm2_s": 7.8e-6,
        "henry_constant": 0.32,
        "Koc_L_kg": 1100.0,
        "Kd_L_kg": 33.0,
        "log_kow": 3.15,
        "density_g_cm3": 0.87,
        "viscosity_cP": 0.69,
        "regulatory_limit_ug_g": 1.7,
        "volatility": "Moderada",
        "persistence": "Moderada",
        "toxicity": "Alta",
        "reactive": True,
        "retardation_factor": 3.5,
        "degradation_rate_d": 0.06
    },
    
    "xylene": {
        "name": "Xileno (mezcla)",
        "type": "Hidrocarburo aromático",
        "cas": "1330-20-7",
        "molecular_weight": 106.17,
        "state": "Líquido",
        "solubility_mg_L": 198.0,
        "diffusion_coefficient_cm2_s": 7.5e-6,
        "henry_constant": 0.22,
        "Koc_L_kg": 300.0,
        "Kd_L_kg": 9.0,
        "log_kow": 3.2,
        "density_g_cm3": 0.86,
        "viscosity_cP": 0.81,
        "regulatory_limit_ug_g": 0.19,
        "volatility": "Moderada",
        "persistence": "Moderada",
        "toxicity": "Alta",
        "reactive": True,
        "retardation_factor": 3.0,
        "degradation_rate_d": 0.06
    },
    
    "mtbe": {
        "name": "MTBE (Metil tert-butil éter)",
        "type": "Aditivo de gasolina",
        "cas": "1634-04-4",
        "molecular_weight": 88.15,
        "state": "Líquido",
        "solubility_mg_L": 48000.0,
        "diffusion_coefficient_cm2_s": 9.4e-6,
        "henry_constant": 0.02,
        "Koc_L_kg": 12.0,
        "Kd_L_kg": 0.36,
        "log_kow": 1.45,
        "density_g_cm3": 0.74,
        "viscosity_cP": 0.4,
        "regulatory_limit_ug_g": 3.2,
        "volatility": "Alta",
        "persistence": "Alta",
        "toxicity": "Moderada",
        "reactive": False,
        "retardation_factor": 1.2,
        "degradation_rate_d": 0.02
    },
    
    # HALOGENADOS
    
    "tce": {
        "name": "TCE (Tricloroetileno)",
        "type": "Hidrocarburo halogenado",
        "cas": "79-01-6",
        "molecular_weight": 131.39,
        "state": "Líquido",
        "solubility_mg_L": 1100.0,
        "diffusion_coefficient_cm2_s": 9.2e-6,
        "henry_constant": 0.40,
        "Koc_L_kg": 126.0,
        "Kd_L_kg": 3.78,
        "log_kow": 2.42,
        "density_g_cm3": 1.46,
        "viscosity_cP": 0.55,
        "regulatory_limit_ug_g": 0.2,
        "volatility": "Alta",
        "persistence": "Alta",
        "toxicity": "Muy alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 2.0,
        "degradation_rate_d": 0.03
    },
    
    "pce": {
        "name": "PCE (Tetracloroetileno)",
        "type": "Hidrocarburo halogenado",
        "cas": "127-18-4",
        "molecular_weight": 165.83,
        "state": "Líquido",
        "solubility_mg_L": 150.0,
        "diffusion_coefficient_cm2_s": 8.0e-6,
        "henry_constant": 0.73,
        "Koc_L_kg": 364.0,
        "Kd_L_kg": 10.92,
        "log_kow": 2.88,
        "density_g_cm3": 1.62,
        "viscosity_cP": 0.89,
        "regulatory_limit_ug_g": 2.3,
        "volatility": "Alta",
        "persistence": "Muy alta",
        "toxicity": "Muy alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 3.5,
        "degradation_rate_d": 0.02
    },
    
    "chloroform": {
        "name": "Cloroformo",
        "type": "Hidrocarburo halogenado",
        "cas": "67-66-3",
        "molecular_weight": 119.38,
        "state": "Líquido",
        "solubility_mg_L": 8200.0,
        "diffusion_coefficient_cm2_s": 1.1e-5,
        "henry_constant": 0.15,
        "Koc_L_kg": 32.0,
        "Kd_L_kg": 0.96,
        "log_kow": 1.97,
        "density_g_cm3": 1.48,
        "viscosity_cP": 0.57,
        "regulatory_limit_ug_g": 70.0,
        "volatility": "Alta",
        "persistence": "Moderada",
        "toxicity": "Alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 1.5,
        "degradation_rate_d": 0.05
    },
    
    # METALES PESADOS
    
    "arsenic": {
        "name": "Arsénico",
        "type": "Metal pesado",
        "cas": "7440-38-2",
        "molecular_weight": 74.92,
        "state": "Sólido",
        "solubility_mg_L": 1000.0,
        "diffusion_coefficient_cm2_s": 5.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 5000.0,
        "Kd_L_kg": 150.0,
        "log_kow": 0.0,
        "density_g_cm3": 5.73,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 16.0,
        "volatility": "Nula",
        "persistence": "Permanente",
        "toxicity": "Muy alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 15.0,
        "degradation_rate_d": 0.0
    },
    
    "lead": {
        "name": "Plomo",
        "type": "Metal pesado",
        "cas": "7439-92-1",
        "molecular_weight": 207.2,
        "state": "Sólido",
        "solubility_mg_L": 0.05,
        "diffusion_coefficient_cm2_s": 2.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 100000.0,
        "Kd_L_kg": 3000.0,
        "log_kow": 0.0,
        "density_g_cm3": 11.34,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 450.0,
        "volatility": "Nula",
        "persistence": "Permanente",
        "toxicity": "Muy alta (neurotóxico)",
        "reactive": True,
        "retardation_factor": 50.0,
        "degradation_rate_d": 0.0
    },
    
    "cadmium": {
        "name": "Cadmio",
        "type": "Metal pesado",
        "cas": "7440-43-9",
        "molecular_weight": 112.41,
        "state": "Sólido",
        "solubility_mg_L": 50.0,
        "diffusion_coefficient_cm2_s": 3.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 50000.0,
        "Kd_L_kg": 1500.0,
        "log_kow": 0.0,
        "density_g_cm3": 8.65,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 7.5,
        "volatility": "Nula",
        "persistence": "Permanente",
        "toxicity": "Muy alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 25.0,
        "degradation_rate_d": 0.0
    },
    
    "chromium_vi": {
        "name": "Cromo VI",
        "type": "Metal pesado",
        "cas": "18540-29-9",
        "molecular_weight": 52.0,
        "state": "Sólido (en solución)",
        "solubility_mg_L": 169000.0,
        "diffusion_coefficient_cm2_s": 8.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 1000.0,
        "Kd_L_kg": 30.0,
        "log_kow": 0.0,
        "density_g_cm3": 7.19,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 19.0,
        "volatility": "Nula",
        "persistence": "Permanente",
        "toxicity": "Muy alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 8.0,
        "degradation_rate_d": 0.01
    },
    
    "mercury": {
        "name": "Mercurio",
        "type": "Metal pesado",
        "cas": "7439-97-6",
        "molecular_weight": 200.59,
        "state": "Líquido",
        "solubility_mg_L": 0.06,
        "diffusion_coefficient_cm2_s": 1.5e-6,
        "henry_constant": 0.001,
        "Koc_L_kg": 100000.0,
        "Kd_L_kg": 3000.0,
        "log_kow": 0.0,
        "density_g_cm3": 13.53,
        "viscosity_cP": 1.55,
        "regulatory_limit_ug_g": 0.73,
        "volatility": "Baja",
        "persistence": "Permanente",
        "toxicity": "Muy alta (neurotóxico)",
        "reactive": True,
        "retardation_factor": 40.0,
        "degradation_rate_d": 0.0
    },
    
    "nickel": {
        "name": "Níquel",
        "type": "Metal pesado",
        "cas": "7440-02-0",
        "molecular_weight": 58.69,
        "state": "Sólido",
        "solubility_mg_L": 10000.0,
        "diffusion_coefficient_cm2_s": 6.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 5000.0,
        "Kd_L_kg": 150.0,
        "log_kow": 0.0,
        "density_g_cm3": 8.90,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 130.0,
        "volatility": "Nula",
        "persistence": "Permanente",
        "toxicity": "Alta (carcinógeno)",
        "reactive": True,
        "retardation_factor": 12.0,
        "degradation_rate_d": 0.0
    },
    
    "copper": {
        "name": "Cobre",
        "type": "Metal pesado",
        "cas": "7440-50-8",
        "molecular_weight": 63.55,
        "state": "Sólido",
        "solubility_mg_L": 1000.0,
        "diffusion_coefficient_cm2_s": 7.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 10000.0,
        "Kd_L_kg": 300.0,
        "log_kow": 0.0,
        "density_g_cm3": 8.96,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 1720.0,
        "volatility": "Nula",
        "persistence": "Permanente",
        "toxicity": "Moderada",
        "reactive": True,
        "retardation_factor": 18.0,
        "degradation_rate_d": 0.0
    },
    
    "zinc": {
        "name": "Zinc",
        "type": "Metal pesado",
        "cas": "7440-66-6",
        "molecular_weight": 65.38,
        "state": "Sólido",
        "solubility_mg_L": 50000.0,
        "diffusion_coefficient_cm2_s": 8.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 10000.0,
        "Kd_L_kg": 300.0,
        "log_kow": 0.0,
        "density_g_cm3": 7.14,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 2480.0,
        "volatility": "Nula",
        "persistence": "Permanente",
        "toxicity": "Baja",
        "reactive": True,
        "retardation_factor": 15.0,
        "degradation_rate_d": 0.0
    },
    
    # SOLVENTES ORGÁNICOS
    
    "acetone": {
        "name": "Acetona",
        "type": "Solvente",
        "cas": "67-64-1",
        "molecular_weight": 58.08,
        "state": "Líquido",
        "solubility_mg_L": 1000000.0,
        "diffusion_coefficient_cm2_s": 1.14e-5,
        "henry_constant": 0.0016,
        "Koc_L_kg": 0.575,
        "Kd_L_kg": 0.017,
        "log_kow": -0.24,
        "density_g_cm3": 0.79,
        "viscosity_cP": 0.32,
        "regulatory_limit_ug_g": 0.5,
        "volatility": "Muy alta",
        "persistence": "Baja",
        "toxicity": "Baja",
        "reactive": True,
        "retardation_factor": 1.1,
        "degradation_rate_d": 0.15
    },
    
    "methanol": {
        "name": "Metanol",
        "type": "Solvente",
        "cas": "67-56-1",
        "molecular_weight": 32.04,
        "state": "Líquido",
        "solubility_mg_L": 1000000.0,
        "diffusion_coefficient_cm2_s": 1.5e-5,
        "henry_constant": 0.0002,
        "Koc_L_kg": 0.8,
        "Kd_L_kg": 0.024,
        "log_kow": -0.77,
        "density_g_cm3": 0.79,
        "viscosity_cP": 0.59,
        "regulatory_limit_ug_g": 100.0,
        "volatility": "Alta",
        "persistence": "Muy baja",
        "toxicity": "Moderada",
        "reactive": True,
        "retardation_factor": 1.05,
        "degradation_rate_d": 0.20
    },
    
    # PESTICIDAS
    
    "atrazine": {
        "name": "Atrazina",
        "type": "Pesticida (herbicida)",
        "cas": "1912-24-9",
        "molecular_weight": 215.73,
        "state": "Sólido",
        "solubility_mg_L": 33.0,
        "diffusion_coefficient_cm2_s": 4.5e-6,
        "henry_constant": 0.002,
        "Koc_L_kg": 100.0,
        "Kd_L_kg": 3.0,
        "log_kow": 2.5,
        "density_g_cm3": 1.19,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 2.0,
        "volatility": "Baja",
        "persistence": "Alta",
        "toxicity": "Moderada",
        "reactive": True,
        "retardation_factor": 4.0,
        "degradation_rate_d": 0.02
    },
    
    "glyphosate": {
        "name": "Glifosato",
        "type": "Pesticida (herbicida)",
        "cas": "1071-83-6",
        "molecular_weight": 169.07,
        "state": "Sólido",
        "solubility_mg_L": 12000.0,
        "diffusion_coefficient_cm2_s": 5.0e-6,
        "henry_constant": 0.0,
        "Koc_L_kg": 24000.0,
        "Kd_L_kg": 720.0,
        "log_kow": -1.7,
        "density_g_cm3": 1.70,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 200.0,
        "volatility": "Nula",
        "persistence": "Moderada",
        "toxicity": "Moderada",
        "reactive": True,
        "retardation_factor": 30.0,
        "degradation_rate_d": 0.04
    },
    
    "ddt": {
        "name": "DDT",
        "type": "Pesticida (insecticida)",
        "cas": "50-29-3",
        "molecular_weight": 354.49,
        "state": "Sólido",
        "solubility_mg_L": 0.001,
        "diffusion_coefficient_cm2_s": 2.0e-6,
        "henry_constant": 0.03,
        "Koc_L_kg": 243000.0,
        "Kd_L_kg": 7290.0,
        "log_kow": 6.91,
        "density_g_cm3": 1.53,
        "viscosity_cP": 0.0,
        "regulatory_limit_ug_g": 1.0,
        "volatility": "Baja",
        "persistence": "Muy alta",
        "toxicity": "Alta",
        "reactive": True,
        "retardation_factor": 100.0,
        "degradation_rate_d": 0.001
    }
}


def get_contaminant_data(contaminant_name):
    """
    Obtener datos completos de un contaminante.
    
    Args:
        contaminant_name: str - Nombre del contaminante (key del catálogo)
    
    Returns:
        dict - Datos completos del contaminante
    """
    return CONTAMINANT_CATALOG.get(contaminant_name.lower(), None)


def get_contaminants_by_type(contaminant_type):
    """
    Filtrar contaminantes por tipo.
    
    Args:
        contaminant_type: str - Tipo de contaminante
    
    Returns:
        list - Lista de nombres de contaminantes de ese tipo
    """
    filtered = []
    for key, data in CONTAMINANT_CATALOG.items():
        if contaminant_type.lower() in data.get("type", "").lower():
            filtered.append(key)
    return filtered


def get_all_contaminants():
    """
    Obtener lista de todos los contaminantes.
    
    Returns:
        list - Lista de nombres de contaminantes
    """
    return list(CONTAMINANT_CATALOG.keys())


def calculate_retardation_factor(Kd, bulk_density, porosity):
    """
    Calcular factor de retardo para contaminantes reactivos.
    
    Fórmula: R = 1 + (ρb * Kd) / n
    
    Args:
        Kd: float - Coeficiente de distribución suelo-agua (L/kg)
        bulk_density: float - Densidad aparente (g/cm³)
        porosity: float - Porosidad total
    
    Returns:
        float - Factor de retardo
    """
    return 1 + (bulk_density * Kd) / porosity


def calculate_effective_diffusion_contaminant(Dm, porosity, tortuosity_factor=1.5):
    """
    Calcular difusión efectiva para contaminantes específicos.
    
    Args:
        Dm: float - Coeficiente de difusión molecular (cm²/s)
        porosity: float - Porosidad efectiva
        tortuosity_factor: float - Factor de tortuosidad (1.3-2.0)
    
    Returns:
        float - Coeficiente de difusión efectiva (cm²/s)
    """
    return Dm * (porosity ** tortuosity_factor)

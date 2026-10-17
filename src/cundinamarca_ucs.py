"""
EDMUNDS - Unidades Cartográficas de Suelo de Cundinamarca
Basado en el Estudio General de Suelos del IGAC (2000)
Escalas: 1:100.000
"""

# Unidades Cartográficas de Suelo (UCS) de Cundinamarca
# Clasificación taxonómica y características físico-químicas

CUNDINAMARCA_UCS = {
    # Asociaciones de Suelos
    
    "MHV": {
        "name": "Asociación Typic Hapludands - Humic Pachic Dystrudepts - Typic Dystrudepts",
        "location": "Sabaná de Bogotá y alrededores",
        "elevation_range": "2200-2800 m.s.n.m.",
        "climate": "Frío húmedo",
        "phases": {
            "MLVd1": "Fase topográfica moderadamente quebrada con erosión ligera",
            "MLVe1": "Fase topográfica fuertemente quebrada con erosión ligera",
            "MLVf1": "Fase topográfica moderadamente escarpada con erosión ligera"
        },
        "soil_components": {
            "Typic Hapludands": 0.40,
            "Humic Pachic Dystrudepts": 0.35,
            "Typic Dystrudepts": 0.25
        },
        "texture": "Franco limoso a franco arcilloso limoso",
        "drainage": "Moderadamente bien drenado",
        "slope": "Moderadamente quebrado a fuertemente quebrado",
        "erosion": "Ligera a moderada",
        "land_use": "Pastos, cultivos de papa, maíz, hortalizas",
        "hydraulic_properties": {
            "total_porosity": 0.52,
            "effective_porosity": 0.35,
            "hydraulic_conductivity_cm_d": 8.5,
            "field_capacity": 0.35,
            "wilting_point": 0.18,
            "bulk_density": 1.25,
            "organic_matter_percent": 8.5,
            "ph": 5.2,
            "c_exponent": 1.8
        },
        "chemical_properties": {
            "CEC_cmol_kg": 18.5,
            "bases_saturation_percent": 45,
            "aluminum_saturation_percent": 30
        }
    },
    
    "MLH": {
        "name": "Consociación Fluvaquentic Humaquepts - Typic Endoaquents",
        "location": "Valles aluviales y planicies de inundación",
        "elevation_range": "200-500 m.s.n.m.",
        "climate": "Cálido húmedo",
        "phases": {
            "MMEg1": "Fase topográfica fuertemente escarpada y erosión ligera",
            "MMEg2": "Fase topográfica fuertemente escarpada y erosión moderada"
        },
        "soil_components": {
            "Fluvaquentic Humaquepts": 0.75,
            "Typic Endoaquents": 0.25
        },
        "texture": "Franco a franco limoso",
        "drainage": "Pobremente drenado",
        "slope": "Plano a ligeramente inclinado",
        "erosion": "Ligera",
        "land_use": "Pastos, cultivos de arroz, caña de azúcar",
        "hydraulic_properties": {
            "total_porosity": 0.48,
            "effective_porosity": 0.30,
            "hydraulic_conductivity_cm_d": 3.2,
            "field_capacity": 0.40,
            "wilting_point": 0.22,
            "bulk_density": 1.35,
            "organic_matter_percent": 6.2,
            "ph": 6.5,
            "c_exponent": 1.7
        },
        "chemical_properties": {
            "CEC_cmol_kg": 22.0,
            "bases_saturation_percent": 65,
            "aluminum_saturation_percent": 15
        }
    },
    
    "MMA": {
        "name": "Asociación Inceptic Haplustalfs - Lithic Ustorthents - Lithic Dystrustepts",
        "location": "Provincias Centro, Tundama, Sugamuxi, Occidente, Valderrama",
        "elevation_range": "2500-3200 m.s.n.m.",
        "climate": "Frío a muy frío",
        "parent_material": "Sedimentarias (areniscas, lutitas, arcillolitas, lodolitas, limolitas, shales)",
        "soil_components": {
            "Inceptic Haplustalfs": 0.30,
            "Lithic Ustorthents": 0.30,
            "Lithic Dystrustepts": 0.25,
            "Andic Dystrustepts": 0.10,
            "Entic Haplustolls": 0.05
        },
        "texture": "Franco arenoso a franco arcilloso arenoso",
        "drainage": "Bien drenado a excesivamente drenado",
        "slope": "Moderadamente quebrado a escarpado",
        "erosion": "Moderada a severa",
        "land_use": "Pastos, rastrojos, cultivos de cebada, maíz, trigo, papa",
        "vegetation": "Relictos de bosque primario (aliso, roble, camiseto)",
        "hydraulic_properties": {
            "total_porosity": 0.45,
            "effective_porosity": 0.32,
            "hydraulic_conductivity_cm_d": 15.8,
            "field_capacity": 0.28,
            "wilting_point": 0.15,
            "bulk_density": 1.42,
            "organic_matter_percent": 4.5,
            "ph": 5.8,
            "c_exponent": 1.5
        },
        "chemical_properties": {
            "CEC_cmol_kg": 12.5,
            "bases_saturation_percent": 55,
            "aluminum_saturation_percent": 25
        }
    },
    
    "MQC": {
        "name": "Complejo Typic Hapludox - Typic Paleudult - Typic Kandiudult",
        "location": "Región oriental de Cundinamarca",
        "elevation_range": "300-800 m.s.n.m.",
        "climate": "Cálido seco a subhúmedo",
        "soil_components": {
            "Typic Hapludox": 0.35,
            "Typic Paleudult": 0.30,
            "Typic Kandiudult": 0.35
        },
        "texture": "Arcilloso a franco arcilloso",
        "drainage": "Moderadamente bien drenado",
        "slope": "Ligeramente inclinado a moderadamente quebrado",
        "erosion": "Ligera a moderada",
        "land_use": "Cultivos de café, cacao, cítricos",
        "hydraulic_properties": {
            "total_porosity": 0.50,
            "effective_porosity": 0.28,
            "hydraulic_conductivity_cm_d": 4.5,
            "field_capacity": 0.32,
            "wilting_point": 0.20,
            "bulk_density": 1.38,
            "organic_matter_percent": 3.8,
            "ph": 5.0,
            "c_exponent": 1.9
        },
        "chemical_properties": {
            "CEC_cmol_kg": 8.5,
            "bases_saturation_percent": 35,
            "aluminum_saturation_percent": 45
        }
    },
    
    "MQCd": {
        "name": "Complejo Typic Hapludox - Typic Paleudult (fase pedregosa)",
        "location": "Región oriental de Cundinamarca",
        "elevation_range": "300-800 m.s.n.m.",
        "climate": "Cálido seco a subhúmedo",
        "special_characteristics": "Pedregosidad superficial 15-50%",
        "soil_components": {
            "Typic Hapludox": 0.40,
            "Typic Paleudult": 0.35,
            "Typic Kandiudult": 0.25
        },
        "texture": "Arcilloso con fragmentos de roca",
        "drainage": "Excesivamente drenado (por pedregosidad)",
        "slope": "Moderadamente quebrado",
        "erosion": "Moderada (por pedregosidad)",
        "land_use": "Pastos extensivos",
        "hydraulic_properties": {
            "total_porosity": 0.42,
            "effective_porosity": 0.22,
            "hydraulic_conductivity_cm_d": 25.0,
            "field_capacity": 0.25,
            "wilting_point": 0.12,
            "bulk_density": 1.55,
            "organic_matter_percent": 2.5,
            "ph": 5.2,
            "c_exponent": 1.6
        },
        "chemical_properties": {
            "CEC_cmol_kg": 6.5,
            "bases_saturation_percent": 30,
            "aluminum_saturation_percent": 50
        }
    },
    
    "MFA": {
        "name": "Asociación Fluventic Haplustolls - Typic Ustifluvents - Aquic Ustifluvents",
        "location": "Planicies aluviales del río Magdalena",
        "elevation_range": "200-400 m.s.n.m.",
        "climate": "Cálido húmedo",
        "soil_components": {
            "Fluventic Haplustolls": 0.50,
            "Typic Ustifluvents": 0.30,
            "Aquic Ustifluvents": 0.20
        },
        "texture": "Franco a franco arenoso",
        "drainage": "Bien drenado a moderadamente bien drenado",
        "slope": "Plano",
        "erosion": "Nula a ligera",
        "land_use": "Cultivos intensivos (algodón, sorgo, maíz)",
        "hydraulic_properties": {
            "total_porosity": 0.46,
            "effective_porosity": 0.38,
            "hydraulic_conductivity_cm_d": 22.5,
            "field_capacity": 0.30,
            "wilting_point": 0.14,
            "bulk_density": 1.40,
            "organic_matter_percent": 2.8,
            "ph": 6.8,
            "c_exponent": 1.4
        },
        "chemical_properties": {
            "CEC_cmol_kg": 15.0,
            "bases_saturation_percent": 75,
            "aluminum_saturation_percent": 10
        }
    },
    
    "MTH": {
        "name": "Consociación Typic Haplustalfs - Ultic Haplustalfs",
        "location": "Cordillera Oriental",
        "elevation_range": "2800-3600 m.s.n.m.",
        "climate": "Frío a muy frío",
        "parent_material": "Areniscas y lutitas",
        "soil_components": {
            "Typic Haplustalfs": 0.85,
            "Ultic Haplustalfs": 0.15
        },
        "texture": "Franco arcilloso arenoso",
        "drainage": "Bien drenado",
        "slope": "Fuertemente quebrado a escarpado",
        "erosion": "Moderada",
        "land_use": "Pastos de altura, cultivos de papa",
        "hydraulic_properties": {
            "total_porosity": 0.43,
            "effective_porosity": 0.30,
            "hydraulic_conductivity_cm_d": 12.0,
            "field_capacity": 0.26,
            "wilting_point": 0.13,
            "bulk_density": 1.45,
            "organic_matter_percent": 5.5,
            "ph": 5.5,
            "c_exponent": 1.6
        },
        "chemical_properties": {
            "CEC_cmol_kg": 14.0,
            "bases_saturation_percent": 50,
            "aluminum_saturation_percent": 30
        }
    },
    
    "MPA": {
        "name": "Asociación Andic Hapludands - Typic Hapludands - Humic Hapludands",
        "location": "Zona andina de la Sabana",
        "elevation_range": "2500-3000 m.s.n.m.",
        "climate": "Frío húmedo",
        "parent_material": "Cenizas volcánicas",
        "soil_components": {
            "Andic Hapludands": 0.45,
            "Typic Hapludands": 0.35,
            "Humic Hapludands": 0.20
        },
        "texture": "Franco limoso volcánico",
        "drainage": "Moderadamente bien drenado",
        "slope": "Ligeramente inclinado a moderadamente quebrado",
        "erosion": "Ligera",
        "land_use": "Cultivos de hortalizas, flores, pastos",
        "hydraulic_properties": {
            "total_porosity": 0.55,
            "effective_porosity": 0.38,
            "hydraulic_conductivity_cm_d": 6.8,
            "field_capacity": 0.38,
            "wilting_point": 0.20,
            "bulk_density": 1.20,
            "organic_matter_percent": 12.0,
            "ph": 5.8,
            "c_exponent": 1.8
        },
        "chemical_properties": {
            "CEC_cmol_kg": 25.0,
            "bases_saturation_percent": 60,
            "aluminum_saturation_percent": 20
        }
    },
    
    "MSL": {
        "name": "Asociación Typic Paleudults - Typic Kanhapludults - Arenic Kandiudults",
        "location": "Región del Río Negro",
        "elevation_range": "1500-2200 m.s.n.m.",
        "climate": "Subhúmedo",
        "parent_material": "Areniscas cuarzosas",
        "soil_components": {
            "Typic Paleudults": 0.40,
            "Typic Kanhapludults": 0.35,
            "Arenic Kandiudults": 0.25
        },
        "texture": "Arenoso a franco arenoso",
        "drainage": "Bien drenado a excesivamente drenado",
        "slope": "Moderadamente quebrado",
        "erosion": "Moderada",
        "land_use": "Cultivos de café, cítricos, guayaba",
        "hydraulic_properties": {
            "total_porosity": 0.40,
            "effective_porosity": 0.35,
            "hydraulic_conductivity_cm_d": 28.0,
            "field_capacity": 0.18,
            "wilting_point": 0.08,
            "bulk_density": 1.58,
            "organic_matter_percent": 1.5,
            "ph": 4.8,
            "c_exponent": 1.3
        },
        "chemical_properties": {
            "CEC_cmol_kg": 5.0,
            "bases_saturation_percent": 25,
            "aluminum_saturation_percent": 60
        }
    },
    
    "MVH": {
        "name": "Consociación Vertic Haplusterts - Typic Calciusterts",
        "location": "Valles interandinos",
        "elevation_range": "1800-2500 m.s.n.m.",
        "climate": "Subhúmedo",
        "parent_material": "Materiales calcáreos",
        "soil_components": {
            "Vertic Haplusterts": 0.70,
            "Typic Calciusterts": 0.30
        },
        "texture": "Arcilloso con grietas de contracción",
        "drainage": "Moderadamente bien drenado",
        "slope": "Plano a ligeramente inclinado",
        "erosion": "Ligera",
        "land_use": "Cultivos de caña panelera, maíz, yuca",
        "hydraulic_properties": {
            "total_porosity": 0.48,
            "effective_porosity": 0.25,
            "hydraulic_conductivity_cm_d": 5.5,
            "field_capacity": 0.35,
            "wilting_point": 0.18,
            "bulk_density": 1.42,
            "organic_matter_percent": 4.0,
            "ph": 7.2,
            "c_exponent": 1.9
        },
        "chemical_properties": {
            "CEC_cmol_kg": 20.0,
            "bases_saturation_percent": 85,
            "aluminum_saturation_percent": 5
        }
    }
}


def get_ucs_parameters(ucs_code):
    """
    Obtener parámetros de una UCS específica.
    
    Args:
        ucs_code: str - Código de la UCS (ej: "MHV", "MLH", "MMA")
    
    Returns:
        dict - Parámetros completos de la UCS
    """
    return CUNDINAMARCA_UCS.get(ucs_code.upper(), None)


def get_all_ucs_list():
    """
    Obtener lista de todas las UCS disponibles.
    
    Returns:
        list - Lista de códigos de UCS
    """
    return list(CUNDINAMARCA_UCS.keys())


def get_ucs_by_elevation(min_elev, max_elev):
    """
    Filtrar UCS por rango de elevación.
    
    Args:
        min_elev: int - Elevación mínima (m.s.n.m.)
        max_elev: int - Elevación máxima (m.s.n.m.)
    
    Returns:
        list - Lista de códigos de UCS que cumplen el criterio
    """
    filtered = []
    for code, data in CUNDINAMARCA_UCS.items():
        elev_str = data.get("elevation_range", "")
        try:
            # Extraer números del rango
            parts = elev_str.split("-")
            if len(parts) == 2:
                min_val = int(parts[0].strip().split()[0])
                max_val = int(parts[1].strip().split()[0])
                if min_val >= min_elev and max_val <= max_elev:
                    filtered.append(code)
        except:
            continue
    return filtered


def get_ucs_by_texture(texture_type):
    """
    Filtrar UCS por tipo de textura.
    
    Args:
        texture_type: str - Tipo de textura (ej: "arcilloso", "arenoso", "franco")
    
    Returns:
        list - Lista de códigos de UCS con esa textura
    """
    filtered = []
    for code, data in CUNDINAMARCA_UCS.items():
        if texture_type.lower() in data.get("texture", "").lower():
            filtered.append(code)
    return filtered

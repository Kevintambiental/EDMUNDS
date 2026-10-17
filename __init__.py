"""
EDMUNDS - Environmental Dispersion Modeling for Underground Natural Soil Systems
Paquete principal de módulos
"""

from .soil_parameters import (
    SOIL_PARAMETERS,
    DIFFUSION_COEFFICIENTS,
    DISPERSIVITY_VALUES,
    REGULATORY_LIMITS,
    get_soil_parameters,
    get_diffusion_coefficient,
    get_dispersivity,
    get_regulatory_limit,
    calculate_effective_diffusion,
    calculate_darcy_velocity,
    calculate_linear_velocity,
    calculate_advective_flux,
)

from .transport_equations import (
    error_function,
    ogata_banks_solution,
    first_fick_law,
    second_fick_law_derivative,
    diffusion_solution,
    calculate_dispersion_coefficient,
    calculate_longitudinal_dispersion,
    calculate_transverse_dispersion,
    detect_concentration_change,
    partition_equation,
    model_concentration_profile,
    calculate_plume_front,
    calculate_max_concentration_zone,
)

from .plume_3d import (
    create_3d_grid,
    calculate_3d_concentration,
    identify_plume_zones,
    calculate_plume_volume,
    calculate_plume_center_of_mass,
    calculate_plume_statistics,
    export_plume_data,
)

__version__ = "1.0.0"

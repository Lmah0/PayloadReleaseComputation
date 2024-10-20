import math

# Constants (These should be set beforehand in the flight control system)
rho = 1.225  # Air density (kg/m^3) at sea level [California Maryland]
rho_calgary = 1.067 # Air density (kg/m^3) in Calgary
C = 1.0  # Drag coefficient of the payload (example value)
A = 0.5  # Surface area of the payload (m^2) (example value)
g = 9.81  # Gravity (m/s^2)
m = 10  # Mass of the payload (kg) (example value)
delta_t = 0.02  # Time interval (s)
N = 3000  # Maximum number of iterations

def compute_air_density(altitude):
    """
    Compute the air density (ρ) at a given altitude.
    
    REQUIRES:
    - altitude: Altitude above sea level in meters (m)
    
    PROMISES: Returns the air density in kg/m³.
    """
    # Constants
    rho_0 = 1.225  # Air density at sea level (kg/m³)
    T_0 = 288.15  # Standard temperature at sea level (Kelvin)
    L = 0.0065  # Temperature lapse rate (K/m)
    g = 9.81  # Gravitational acceleration (m/s²)
    M = 0.029  # Molar mass of Earth's air (kg/mol)
    R = 8.314  # Universal gas constant (J/(mol·K))

    # Altitude in meters
    h = altitude

    # Compute temperature at the given altitude
    T = T_0 - (L * h)

    # Compute air pressure at the given altitude using the barometric formula
    P = 101325 * (T / T_0) ** (g * M / (R * L))

    # Compute air density using the ideal gas law
    rho = (P * M) / (R * T)

    return rho

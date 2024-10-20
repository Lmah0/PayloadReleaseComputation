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

# Function to compute the constant 'q'
def compute_q():
    return 0.5 * rho * C * A

def compute_drop_location(aircraft_ground_speed, agl_altitude, wind_speed, target_lat, target_long, current_lat, current_long):
    '''
    REQUIRES:
    - Aircraft speed relative to ground (m/s)
    - Above ground level (AGL) altitude (m)
    - Wind speed relative to the aircraft (m/s)
    - Target latitude and longitude (degrees)
    - Current latitude and longitude (degrees)

    PROMISES: Returns the latitude and longitude of the drop point
    '''
    
    q = compute_q()
    vx = aircraft_ground_speed - wind_speed  # Initial horizontal velocity (relative to ground)
    vy = 0  # Initial vertical velocity (payload starts with 0 vertical speed)

    x, y = 0, agl_altitude  # Initial horizontal distance (x) and vertical distance (y = altitude)
    t = 0  # Initial time

    for i in range(N):
        # Step 4a: Calculate accelerations in x and y directions
        accx = -(q / m) * vx ** 2
        accy = g - (q / m) * vy ** 2

        # Step 4b: Update velocities in x and y directions
        vx = vx + accx * delta_t
        vy = vy + accy * delta_t

        # Step 4c: Update distances in x and y directions
        x = x + vx * delta_t + 0.5 * accx * (delta_t ** 2)
        y = y + vy * delta_t + 0.5 * accy * (delta_t ** 2)

        # Update time
        t += delta_t

        # Step 4e: Check if the projectile has reached ground level (y == 0)
        if y <= 0:
            break
    
    # After the loop, we have the range x and can calculate the release point
    range_R = x

    # Calculate release point in terms of latitude and longitude
    delta_long = target_long - current_long
    delta_lat = target_lat - current_lat
    theta = math.atan2(delta_long, delta_lat)

    RPlat = target_lat - range_R * math.sin(theta)
    RPlon = target_long - range_R * math.cos(theta)

    return RPlat, RPlon

# Example call (replace with actual data)
aircraft_speed = 250  # m/s
agl_altitude = 1000  # meters above ground level
wind_speed = 10  # m/s
target_lat = 50.0  # degrees
target_long = -100.0  # degrees
current_lat = 49.0  # degrees
current_long = -99.0  # degrees

drop_lat, drop_lon = compute_drop_location(aircraft_speed, agl_altitude, wind_speed, target_lat, target_long, current_lat, current_long)

print(f"Drop location: Latitude {drop_lat}, Longitude {drop_lon}")

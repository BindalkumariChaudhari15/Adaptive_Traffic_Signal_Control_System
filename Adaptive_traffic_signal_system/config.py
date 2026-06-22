# Configuration settings for the simulation

# Simulation settings
SIMULATION_DURATION = 3600      # seconds (1 hour)
TIME_STEP = 1                   # simulation updates every second

# Traffic scenarios (vehicles/minute, pedestrians/minute)
LOW_TRAFFIC = {
    "vehicle_rate": 5,
    "pedestrian_rate": 2
}
MODERATE_TRAFFIC = {
    "vehicle_rate": 15,
    "pedestrian_rate": 8
}
PEAK_TRAFFIC = {
    "vehicle_rate": 30,
    "pedestrian_rate": 15
}

# Algorithm weights
PEDESTRIAN_QUEUE_WEIGHT = 2.0
PEDESTRIAN_WAIT_WEIGHT = 1.5
VEHICLE_QUEUE_WEIGHT = 1.0

# Decision threshold
PRIORITY_THRESHOLD = 10.0

# Service rates (entities that can pass during green signal)
VEHICLES_PER_GREEN = 5
PEDESTRIANS_PER_GREEN = 10

# Signal timing constraints
MIN_GREEN_TIME = 10     # seconds
MAX_GREEN_TIME = 60     # seconds
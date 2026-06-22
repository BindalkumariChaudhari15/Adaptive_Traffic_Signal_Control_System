# Main simulation program

import random

from config import (
    SIMULATION_DURATION,
    LOW_TRAFFIC,
    VEHICLES_PER_GREEN,
    PEDESTRIANS_PER_GREEN
)

from vehicle import Vehicle
from pedestrian import Pedestrian
from queue_manager import QueueManager
from signal_controller import SignalController
from statistics import StatisticsCollector


# Simulation Configuration

SCENARIO = LOW_TRAFFIC

vehicle_arrival_probability = (
    SCENARIO["vehicle_rate"] / 60.0
)

pedestrian_arrival_probability = (
    SCENARIO["pedestrian_rate"] / 60.0
)


# Initialize Components

queue_manager = QueueManager()
signal_controller = SignalController()
statistics = StatisticsCollector()

vehicle_counter = 0
pedestrian_counter = 0


# Main Simulation Loop

print("Starting Simulation...\n")

for current_time in range(SIMULATION_DURATION):

    # Generate new vehicle arrivals
    
    if random.random() < vehicle_arrival_probability:
        vehicle_counter += 1
        vehicle = Vehicle(
            vehicle_counter,
            current_time
        )
        queue_manager.add_vehicle(vehicle)

    # Generate new pedestrian arrivals
    
    if random.random() < pedestrian_arrival_probability:
        pedestrian_counter += 1
        pedestrian = Pedestrian(
            pedestrian_counter,
            current_time
        )
        queue_manager.add_pedestrian(pedestrian)

    # Update waiting times
    
    queue_manager.update_waiting_times(
        current_time
    )

    # Get current queue information
    
    vehicle_queue_length = (
        queue_manager.get_vehicle_queue_length()
    )

    pedestrian_queue_length = (
        queue_manager.get_pedestrian_queue_length()
    )

    if pedestrian_queue_length > 0:
        average_pedestrian_wait = (
            sum(
                p.waiting_time
                for p in queue_manager.pedestrian_queue
            )
            / pedestrian_queue_length
        )
    else:
        average_pedestrian_wait = 0

    # Adaptive signal decision
    
    current_signal, priority_score = (
        signal_controller.decide_signal(
            pedestrian_queue_length,
            average_pedestrian_wait,
            vehicle_queue_length
        )
    )

    statistics.record_priority_score(
        priority_score
    )

    # Serve entities
    
    if current_signal == "PEDESTRIAN_GREEN":

        served = (
            queue_manager.serve_pedestrians(
                PEDESTRIANS_PER_GREEN
            )
        )

        for pedestrian in served:
            statistics.record_pedestrian(
                pedestrian
            )

    else:

        served = (
            queue_manager.serve_vehicles(
                VEHICLES_PER_GREEN
            )
        )

        for vehicle in served:
            statistics.record_vehicle(
                vehicle
            )

    # Record queue lengths
    
    statistics.record_queue_lengths(
        vehicle_queue_length,
        pedestrian_queue_length
    )


# Print results

print("Simulation Complete!\n")

summary = statistics.generate_summary()

print("===== RESULTS =====")

for key, value in summary.items():
 print(f"{key}: {value}")
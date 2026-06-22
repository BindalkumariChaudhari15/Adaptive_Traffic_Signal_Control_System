# Adaptive traffic signal controller

from config import (
    PEDESTRIAN_QUEUE_WEIGHT,
    PEDESTRIAN_WAIT_WEIGHT,
    VEHICLE_QUEUE_WEIGHT,
    PRIORITY_THRESHOLD
)

class SignalController:
    """
    Implements the adaptive priority algorithm.
    """

    def __init__(self):
        self.current_signal = "VEHICLE_GREEN"

    # Calculate priority score
    
    def calculate_priority(
        self,
        pedestrian_queue_length,
        average_pedestrian_wait,
        vehicle_queue_length
    ):
        """
        Computes the adaptive priority score.
        """
        priority_score = (
            pedestrian_queue_length * PEDESTRIAN_QUEUE_WEIGHT
            + average_pedestrian_wait * PEDESTRIAN_WAIT_WEIGHT
            - vehicle_queue_length * VEHICLE_QUEUE_WEIGHT
        )

        return priority_score

    # Make signal decision
    
    def decide_signal(
        self,
        pedestrian_queue_length,
        average_pedestrian_wait,
        vehicle_queue_length
    ):
        """
        Determines which signal should be green.
        """

        score = self.calculate_priority(
            pedestrian_queue_length,
            average_pedestrian_wait,
            vehicle_queue_length
        )

        if score >= PRIORITY_THRESHOLD:
            self.current_signal = "PEDESTRIAN_GREEN"
        else:
            self.current_signal = "VEHICLE_GREEN"

        return self.current_signal, score
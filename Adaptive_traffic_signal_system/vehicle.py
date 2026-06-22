# Vehicle class for the traffic simulation

class Vehicle:
    """
    Represents a single vehicle in the simulation.
    """
    def __init__(self, vehicle_id, arrival_time):
        self.vehicle_id = vehicle_id
        self.arrival_time = arrival_time
        self.waiting_time = 0
    def update_waiting_time(self, current_time):
        """
        Updates how long the vehicle has been waiting.
        """
        self.waiting_time = current_time - self.arrival_time
    def __repr__(self):
        return (
            f"Vehicle("
            f"id={self.vehicle_id}, "
            f"arrival={self.arrival_time}, "
            f"waiting={self.waiting_time})"
        )
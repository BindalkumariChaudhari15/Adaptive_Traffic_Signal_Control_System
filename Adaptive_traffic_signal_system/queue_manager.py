# Manages vehicle and pedestrian queues

from collections import deque
class QueueManager:
    """
    Maintains separate queues for vehicles
    and pedestrians.
    """

    def __init__(self):
        self.vehicle_queue = deque()
        self.pedestrian_queue = deque()

    # Add new arrivals
    

    def add_vehicle(self, vehicle):
        """
        Adds a vehicle object to the queue.
        """
        self.vehicle_queue.append(vehicle)

    def add_pedestrian(self, pedestrian):
        """
        Adds a pedestrian object to the queue.
        """
        self.pedestrian_queue.append(pedestrian)

    # Queue information
    
    def get_vehicle_queue_length(self):
        return len(self.vehicle_queue)

    def get_pedestrian_queue_length(self):
        return len(self.pedestrian_queue)

    # Update waiting times
    
    def update_waiting_times(self, current_time):
        """
        Updates waiting times for all
        entities currently in the queues.
        """
        for vehicle in self.vehicle_queue:
            vehicle.update_waiting_time(current_time)

        for pedestrian in self.pedestrian_queue:
            pedestrian.update_waiting_time(current_time)

    # Serve traffic
    
    def serve_vehicles(self, max_count):
        """
        Removes vehicles that pass during
        a green signal.
        """
        served = []

        while self.vehicle_queue and len(served) < max_count:
            served.append(self.vehicle_queue.popleft())

        return served

    def serve_pedestrians(self, max_count):
        """
        Removes pedestrians who cross
        during a pedestrian green signal.
        """
        served = []

        while self.pedestrian_queue and len(served) < max_count:
            pedestrian = self.pedestrian_queue.popleft()
            pedestrian.serve_request()
            served.append(pedestrian)
        return served
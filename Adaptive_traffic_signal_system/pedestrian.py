# Pedestrian class for the traffic simulation

class Pedestrian:
    """
    Represents a pedestrian crossing request.
    """

    def __init__(self, pedestrian_id, arrival_time):
        self.pedestrian_id = pedestrian_id
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.request_served = False

    def update_waiting_time(self, current_time):
        """
        Updates how long the pedestrian has been waiting.
        """
        self.waiting_time = current_time - self.arrival_time

    def serve_request(self):
        """
        Marks the crossing request as completed.
        """
        self.request_served = True

    def __repr__(self):
        return (
            f"Pedestrian("
            f"id={self.pedestrian_id}, "
            f"arrival={self.arrival_time}, "
            f"waiting={self.waiting_time}, "
            f"served={self.request_served})"
        )
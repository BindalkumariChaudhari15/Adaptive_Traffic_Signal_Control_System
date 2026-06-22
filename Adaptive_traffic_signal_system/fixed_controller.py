# Traditional fixed-time traffic controller

class FixedTimeController:
    """    Simulates a conventional fixed-time
traffic signal controller. """

    def __init__(
        self,
        vehicle_green_duration=30,
        pedestrian_green_duration=15
    ):
        self.vehicle_green_duration = vehicle_green_duration
        self.pedestrian_green_duration = pedestrian_green_duration

        self.current_signal = "VEHICLE_GREEN"
        self.signal_timer = 0

    def update(self):
        """
        Updates the signal state according to
        fixed timing intervals.
        """

        self.signal_timer += 1

        if self.current_signal == "VEHICLE_GREEN":
            if self.signal_timer >= self.vehicle_green_duration:
                self.current_signal = "PEDESTRIAN_GREEN"
                self.signal_timer = 0

        else:
            if self.signal_timer >= self.pedestrian_green_duration:
                self.current_signal = "VEHICLE_GREEN"
                self.signal_timer = 0

        return self.current_signal
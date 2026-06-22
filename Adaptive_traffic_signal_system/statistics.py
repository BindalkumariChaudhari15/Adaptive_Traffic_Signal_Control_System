# Collects simulation performance metrics

class StatisticsCollector:
    """
    Stores and computes simulation statistics.
    """

    def __init__(self):
        self.vehicle_waiting_times = []
        self.pedestrian_waiting_times = []

        self.total_vehicles_served = 0
        self.total_pedestrians_served = 0

        self.vehicle_queue_history = []
        self.pedestrian_queue_history = []

        self.priority_scores = []

    # Recording methods
    
    def record_vehicle(self, vehicle):
        self.vehicle_waiting_times.append(
            vehicle.waiting_time
        )
        self.total_vehicles_served += 1

    def record_pedestrian(self, pedestrian):
        self.pedestrian_waiting_times.append(
            pedestrian.waiting_time
        )
        self.total_pedestrians_served += 1

    def record_queue_lengths(
        self,
        vehicle_queue_length,
        pedestrian_queue_length
    ):
        self.vehicle_queue_history.append(
            vehicle_queue_length
        )
        self.pedestrian_queue_history.append(
            pedestrian_queue_length
        )

    def record_priority_score(self, score):
        self.priority_scores.append(score)

    # Calculation methods
    
    def average_vehicle_delay(self):
        if not self.vehicle_waiting_times:
            return 0

        return (
            sum(self.vehicle_waiting_times)
            / len(self.vehicle_waiting_times)
        )

    def average_pedestrian_wait(self):
        if not self.pedestrian_waiting_times:
            return 0

        return (
            sum(self.pedestrian_waiting_times)
            / len(self.pedestrian_waiting_times)
        )

    def throughput(self):
        return (
            self.total_vehicles_served
            + self.total_pedestrians_served
        )

    def fairness_index(self):
        """
        Simple fairness measure.
        Value closer to 1 indicates better balance.
        """

        vehicle_delay = self.average_vehicle_delay()
        pedestrian_delay = self.average_pedestrian_wait()

        if vehicle_delay + pedestrian_delay == 0:
            return 1.0

        return (
            1
            - abs(
                vehicle_delay
                - pedestrian_delay
            )
            / (
                vehicle_delay
                + pedestrian_delay
            )
        )

    # Final report summary
    
    def generate_summary(self):
        return {
            "Average Vehicle Delay":
                round(
                    self.average_vehicle_delay(),
                    2
                ),

            "Average Pedestrian Wait":
                round(
                    self.average_pedestrian_wait(),
                    2
                ),

            "Vehicles Served":
                self.total_vehicles_served,

            "Pedestrians Served":
                self.total_pedestrians_served,

            "Throughput":
                self.throughput(),

            "Fairness Index":
                round(
                    self.fairness_index(),
                    3
                )
        }
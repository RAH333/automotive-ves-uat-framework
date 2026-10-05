"""
Simulates the Electronic Control Unit (ECU) behavior for an Autonomous Emergency Braking (AEB) system.
"""
class SimulatedECU:
    def __init__(self, critical_distance):
        self.critical_distance = critical_distance
        self.brake_actuated = False
        self.current_speed = 0.0

    def process_sensor_data(self, speed_kph, distance_to_obstacle):
        """Simulates real-time ADAS processing logic."""
        self.current_speed = speed_kph
        if distance_to_obstacle <= self.critical_distance and speed_kph > 0:
            self.brake_actuated = True
        else:
            self.brake_actuated = False
        
        return {
            "speed": self.current_speed,
            "distance": distance_to_obstacle,
            "brake_status": "ACTIVE" if self.brake_actuated else "INACTIVE"
        }
      

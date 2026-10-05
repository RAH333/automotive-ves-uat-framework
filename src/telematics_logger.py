"""
Simulates the telematics module uploading crucial safety metrics to the cloud over MQTT/HTTP.
"""
import json

class TelematicsLogger:
    def __init__(self):
        self.log_history = []

    def transmit_payload(self, ecu_status):
        """Simulates sending vehicle telemetry packets to the backend."""
        payload = {
            "event": "UAT_LOG",
            "telemetry": ecu_status,
            "status_code": 200 if ecu_status["brake_status"] == "ACTIVE" else 100
        }
        self.log_history.append(payload)
        return json.dumps(payload)
      

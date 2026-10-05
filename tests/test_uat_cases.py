"""
The heart of your framework: automated Python UAT test cases verifying critical safety conditions using pytest.
"""
import pytest
import json
from src.sim_ecu import SimulatedECU
from src.telematics_logger import TelematicsLogger

# Load Configuration
with open("config/test_config.json") as config_file:
    config = json.load(config_file)

CRITICAL_DIST = config["adas_thresholds"]["critical_distance_meters"]

def test_uat_aeb_activation_critical_zone():
    """UAT Case 01: Verify Brake activates when an obstacle is within the critical zone."""
    ecu = SimulatedECU(critical_distance=CRITICAL_DIST)
    telematics = TelematicsLogger()
    
    # Simulating vehicle moving at 50kph with an obstacle 10 meters away
    ecu_output = ecu.process_sensor_data(speed_kph=50.0, distance_to_obstacle=10.0)
    
    # Assertions for physical safety logic (ISO 26262 ASIL-D Alignment)
    assert ecu_output["brake_status"] == "ACTIVE"
    
    # Telematics verification
    telemetry_packet = json.loads(telematics.transmit_payload(ecu_output))
    assert telemetry_packet["status_code"] == 200

def test_uat_aeb_inactive_safe_zone():
    """UAT Case 02: Verify Brake remains inactive when obstacle is far away."""
    ecu = SimulatedECU(critical_distance=CRITICAL_DIST)
    ecu_output = ecu.process_sensor_data(speed_kph=60.0, distance_to_obstacle=40.0)
    
    assert ecu_output["brake_status"] == "INACTIVE"
  

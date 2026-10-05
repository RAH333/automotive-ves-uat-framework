# automotive-ves-uat-framework


# Automotive VES UAT Framework

An automated User Acceptance Testing (UAT) harness simulating Vehicle Electronic Systems (VES). This project targets functional validation of ADAS Braking loops and Telematics cloud pipelines under **ISO 26262 (ASIL-D)** and **ASPICE** paradigms.

## Core Features Implemented
- **ADAS Simulation**: Simulates real-world sensor processing loops for critical emergency braking criteria.
- **Telematics Data Pipeline**: Validation of cloud-transmitted status payloads during critical safety events.
- **Automated Test Automation Harness**: PyTest execution layer verifying vehicle compliance boundaries.

## Quick Start
1. Install testing dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute the validation/UAT suite:
   ```bash
   pytest -v --cov=src
   ```

   
Automotive Hardware-in-the-Loop (HIL) Test Automation Framework simulating UAT for an ADAS Emergency Braking & Telematics system.

# Repository Description:

End-to-end UAT and test automation framework for Vehicle Electronic Systems (VES) simulating ADAS (AEB) and Telematics compliance under ISO 26262 and ASPICE guidelines.
```
automotive-ves-uat-framework/
├── config/
│   └── test_config.json
├── src/
│   ├── sim_ecu.py
│   └── telematics_logger.py
├── tests/
│   └── test_uat_cases.py
├── requirements.txt
└── README.md
```

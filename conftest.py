"""Pytest configuration file to set up the test environment."""

import sys
import os

# Add the src directory to Python path so tests can import mqtt_logger
src_path = os.path.join(os.path.dirname(__file__), "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Add the path to the external mqtt-connector module
mqtt_connector_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../mqtt-connector/src")
)
if os.path.exists(mqtt_connector_path):
    sys.path.insert(0, mqtt_connector_path)
else:
    raise ImportError(f"mqtt_connector path not found: {mqtt_connector_path}")

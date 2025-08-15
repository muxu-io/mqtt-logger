"""Pytest configuration file to set up the test environment."""

import sys
import os

# Add the src directory to Python path so tests can import mqtt_logger
src_path = os.path.join(os.path.dirname(__file__), "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

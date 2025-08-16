# This file marks the directory as a Python package.
# It can be used to define what is exported when the package is imported.

from .logger import MqttLogger

__version__ = "1.0.0"
__author__ = "Alex Gonzalez"
__email__ = "alex@muxu.io"
__description__ = "MQTT-enabled logging with systemd journal integration"
__license__ = "MIT"

__all__ = ["MqttLogger", "__version__"]

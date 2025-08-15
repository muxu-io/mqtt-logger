# Basic usage example of the MqttLogger

import asyncio
import logging

from mqtt_logger import MqttLogger


async def main():
    # Initialize the logger
    logger = MqttLogger(
        log_file="app.log",  # Optional, can be None to disable file logging
        mqtt_broker="mqtt.example.com",
        mqtt_port=1883,
        mqtt_topic="logs/myapp",
        log_level=logging.INFO,
        batch_size=20,
        batch_interval=5.0,
        max_buffer_size=500,
    )

    # Connect to MQTT
    await logger.connect_mqtt()

    # Log some messages
    logger.info("Application started")
    logger.warning("This is a warning", {"error_code": 123})

    # Use structured logging - this will also go to systemd journal
    logger.info(
        "User login",
        {"user_id": "user123", "source_ip": "192.168.1.1", "session_id": "abc123"},
    )

    # Check logger status
    status = logger.get_status()
    print(f"Buffer utilization: {status['buffer_utilization']:.2f}")

    # Flush logs explicitly if needed
    await logger.flush_logs()

    # Shut down gracefully
    await logger.shutdown()


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

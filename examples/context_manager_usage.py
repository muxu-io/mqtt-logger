# filepath: /mqtt-logger/mqtt-logger/examples/context_manager_usage.py

import asyncio

from mqtt_logger import MqttLogger


async def main():
    async with MqttLogger(
        mqtt_broker="mqtt.example.com",
        mqtt_port=1883,
        mqtt_topic="logs/myapp",
        log_file="app.log",  # Optional, can be None to disable file logging
    ) as logger:
        logger.info("In context manager")
        logger.warning("This is a warning", {"error_code": 123})

        # Use structured logging
        logger.info(
            "User login",
            {"user_id": "user123", "source_ip": "192.168.1.1", "session_id": "abc123"},
        )

        # Check logger status
        status = logger.get_status()
        print(f"Buffer utilization: {status['buffer_utilization']:.2f}")


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

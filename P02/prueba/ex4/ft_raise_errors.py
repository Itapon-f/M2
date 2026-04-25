class Plant:
    """Basic plant class with growth capabilities for analytics."""

    def __init__(self, name: str, condition: str, level: int):
        """Initialize a basic plant."""
        self.name = name
        self.condition = condition
        self.level = level


def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!\n")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)\n")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)\n")
    else:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values")
    try:
        check_plant_health("Tomato", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad water level...")
    try:
        check_plant_health("Tomato", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("testing bad sunlight hours...")
    try:
        check_plant_health("Tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

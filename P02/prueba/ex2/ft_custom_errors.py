class Plant:
    """Basic plant class with growth capabilities for analytics."""

    def __init__(self, name: str, days:int, level: int):
        """Initialize a basic plant."""
        self.name = name
        self.days = days
        self.level = level


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def raise_error(plant: str, days: int, level: int):
    if days > 15:
        raise PlantError(f"The {plant} plant is wilting!")
    if level < 3:
        raise WaterError("Not enough water in the water tank!")


def test_errors(plant: Plant):
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise_error(plant.name, plant.days, 5)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise_error(plant.name, 7, plant.level)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        raise_error(plant.name, plant.days, 5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise_error(plant.name, 7, plant.level)
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    tomato: Plant = Plant("Tomato", 17, 2)
    test_errors(tomato)

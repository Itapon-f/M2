class Plant:
    """Basic plant class with growth capabilities for analytics."""

    def __init__(self, name: str, water: int, sun: int):
        """Initialize a basic plant."""
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    pass


class TankError(GardenError):
    pass


class PlantError(Exception):
    pass


class WaterError(PlantError):
    pass


class AddError(PlantError):
    pass


class SunError(PlantError):
    pass


class GardenManager():
    def __init__(self, water_tank):
        self.water_tank = water_tank
        self.plants = []

    def add_plant(self, plant: Plant):
        if plant.name == "":
            raise AddError("Plant name cannot be empty!")
        elif not plant.water:
            raise AddError("Plant is dry and DEAD!!!")
        elif not plant.sun:
            raise AddError("Plant has no sun...It's sad")
        else:
            self.plants.append(plant)
            print(f"Added {plant.name} plant succesfully!")

    def add_plants(self, plant: Plant):
        self.add_plant(plant)

    def water_plants(self, plant:Plant):
        if self.water_tank < 1:
            raise WaterError("No water in the tank")
        else:
            plant.water += 1
            self.water_tank -= 1
            if plant.water <= 0:
                raise ValueError(f"Water level {plant.water} cannot be negative, you erased matter from this world!")
            elif plant.water > 10:
                raise WaterError(f"Water level {plant.water} is too high (max 10)")
            else:
                pass

    def check_plant_health(self, plant:Plant):
        if plant.water < 1:
            raise PlantError(f"Water level {plant.water} is too low")
        elif plant.water > 10:
            raise WaterError(f"Water level {plant.water} is too high (max 10)")
        elif plant.sun < 2:
            raise SunError((f"Sunlight hours {plant.sun}"
                           " is too low (min 2)"))
        elif plant.sun > 12:
            raise SunError((f"Sunligt hours {plant.sun}"
                            " is too high (max 12)"))


def test_management() -> None:
    print("=== Garden Management System ===")
    print("Adding plant to garden...")
    water_tank = 0
    try:
        water_tank: int = int(input("Water tank level: "))
    except ValueError:
        print("Not a valid value!!! Default value = 0.")
    garden = GardenManager(water_tank)
    try:
        name: str = input("Plant name: ")
        water: int = int(input("Water level: "))
        sun: int = int(input("Sun hours: "))
        plant1: Plant = Plant(name, water, sun)
        garden.add_plant(plant1)
    except (ValueError, AddError) as e:
        print(f"Error adding plant: {e}") # PROBAR LLAMANDO AL NOMBRE DE LA PLANTA
    try:
        name: str = input("Plant name: ")
        water: int = int(input("Water level: "))
        sun: int = int(input("Sun hours: "))
        plant2: Plant = Plant(name, water, sun)
        garden.add_plant(plant2)
    except (ValueError, AddError) as e:
        print(f"Error adding plant: {e}") # PROBAR LLAMANDO AL NOMBRE DE LA PLANTA
        
    ask1: str = input("Water the plants? (yes/no)")
    if ask1 == "yes":
        print("\nWatering the plants...")
        try:
            for plant in garden.plants:
                try:
                    print(f"Watering {plant.name}")
                    garden.water_plants(plant)
                except WaterError as e:
                    print(f"Watering error: {e}")
        except GardenError as e:
            print(f"Caught a GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)\n")
    else:
        pass

    ask2: str = input("Check plants health? (yes/no)")
    if ask2 == "yes":
        print("\nChecking plant health...")
        for plant in garden.plants:
            try:
                garden.check_plant_health(plant)
                print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sun})")
            except PlantError as e:
                print(f"Caught GardenError in {plant.name}: {e}")
        print("System recovered and continuing...")
    else:
        pass
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_management()
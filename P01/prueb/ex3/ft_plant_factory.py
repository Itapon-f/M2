class Plant:
    """Represents a plant in the garden factory system."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a new plant for factory production."""
        self.name = name
        self.height = height
        self.age = age

    def getinfo(self):
        """Display plant creation information."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plants(plant_list):
    """Factory function to create and add multiple plants."""
    sample: Plant = Plant("Rose", 25, 30)
    sample.getinfo()
    plant_list.append(sample)
    sample: Plant = Plant("Oak", 200, 365)
    sample.getinfo()
    plant_list.append(sample)
    sample: Plant = Plant("Dandelion", 5, 9)
    sample.getinfo()
    plant_list.append(sample)
    sample: Plant = Plant("Sunflower", 80, 45)
    sample.getinfo()
    plant_list.append(sample)
    sample: Plant = Plant("Fern", 15, 120)
    sample.getinfo()
    plant_list.append(sample)


if __name__ == "__main__":
    plant_list = []
    plant_number: int = 0

    print("== Plant Factory Output ==")
    ft_plants(plant_list)
    plant_number = len(plant_list)
    print("\n")
    print(f"Total plants created: {plant_number}")

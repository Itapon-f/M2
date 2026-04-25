class Plant:
    """Represents a basic plant with name, height, and age attributes."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a new plant."""
        self.name = name
        self.height = height
        self.age = age

    def getinfo(self):
        """Display the plant's information in a formatted string."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    """Demonstrate the plant registry system."""
    print("== Garden Plant Registry ==")
    sample = Plant("Rose", 25, 30)
    sample.getinfo()
    sample = Plant("Sunflower", 80, 45)
    sample.getinfo()
    sample = Plant("Cactus", 15, 120)
    sample.getinfo()


if __name__ == "__main__":
    ft_garden_data()

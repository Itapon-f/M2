class Plant:
    """Base plant class for the garden type system."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a basic plant."""
        self.name = name
        self.height = height
        self.age = age

    def getinfo(self):
        """Display basic plant creation information."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


class Flower(Plant):
    """Represents flowering plants with color attributes."""

    def __init__(self, name, height, age, color):
        """Initialize a flowering plant."""
        super().__init__(name, height, age)
        self.color = color

    def Bloom(self):
        """Display the flower's blooming information."""
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """Represents trees with trunk diameter and shade production."""

    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a tree."""
        super().__init__(name, height, age)
        self.diameter = trunk_diameter
        self.shade = 50 + trunk_diameter/2

    def produce_shade(self):
        """Display the tree's shade production information."""
        print(f"{self.name} (Tree): {self.height}cm,"
              f" {self.age} days, {self.diameter}cm diameter")
        print(f"{self.name} provides {self.shade} square meters of shade\n")


class Vegetable(Plant):
    """Represents edible plants with harvest and nutritional information."""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize a vegetable plant."""
        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutritional = nutritional_value

    def veggie_info(self):
        """Display the vegetable's information."""
        print(f"{self.name} (Vegetable): {self.height}cm,"
              f" {self.age} days, {self.season} harvest")
        print(f"{self.name} is rich in {self.nutritional}\n")


if __name__ == "__main__":
    sample = Flower("Carnation", 25, 30, "pink")
    print("=== Garden Plant Types ===\n")
    sample.Bloom()
    sample = Tree("Oak", 500, 1825, 50)
    sample.produce_shade()
    sample = Vegetable("Carrot", 80, 90, "Summer", "vitamin C")
    sample.veggie_info()

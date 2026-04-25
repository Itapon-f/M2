class Plant:
    """Basic plant class with growth capabilities for analytics."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a basic plant."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Simulate plant growth by increasing height."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self):
        """Return string representation of the plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Represents a flowering plant with color attributes. """

    def __init__(self, name, height, age, color):
        """Initialize a flowering plant."""
        super().__init__(name, height, age)
        self.color = color

    def __str__(self):
        """Return string representation of the flowering plant."""
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Represents a prize-winning flowering plant with point values."""

    def __init__(self, name, height, age, color, points):
        """Initialize a prize flower."""
        super().__init__(name, height, age, color)
        self.points = points

    def __str__(self):
        """Return string representation of the prize flower."""
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Price points: {self.points}")


class Garden:
    """Basic garden container for plants and gardener information."""

    def __init__(self, gardener, plant_list):
        """Initialize a garden."""
        self.gardener = gardener
        self.plant_list = plant_list


class GardenManager:
    """Advanced garden management system with analytics and reporting"""

    total_gardens: int = 0

    def __init__(self, gardener, plant_list):
        """Initialize a garden manager."""
        self.gardener = gardener
        self.plant_list = plant_list if plant_list else []
        self.total_grow = 0
        GardenManager.total_gardens += 1

    # Añade plantas a la lista de plantas
    def add_plant(self, plant):
        """Add a plant to the garden."""
        self.plant_list.append(plant)
        print(f"Added {Plant.name} to {self.gardener}'s garden")

    # Aquí hay un error????
    def manage_grow(self):
        """Manage the growth of all plants in the garden."""
        print(f"{self.gardener} is helping all plants grow...")
        for plant in self.plant_list:
            plant.grow()
            self.total_grow += 1

    # 1. Imprime la lista de plantas y sus características
    # 2. Cuenta el número de plantas de cada tipo
    # 3. Imprime las plantas añadidas y el num de cada tipo
    def report(self):
        """Generate a comprehensive garden report."""
        print("\n")
        print(f"=== {self.gardener}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plant_list:
            print(f"- {plant}")
        print("\n")

        regular: int = sum(1 for p in self.plant_list
                           if type(p).__name__ == "Plant")
        flowering: int = sum(1 for p in self.plant_list
                             if type(p).__name__ == "FloweringPlant")
        prize: int = sum(1 for p in self.plant_list
                         if type(p).__name__ == "PrizeFlower")

        print(f"Plants added: {len(self.plant_list)},"
              f" Total growth: {self.total_grow}cm")
        print(f"Plant types: {regular} regular, {flowering}"
              f" flowering, {prize} prize flowers")
        print("\n")

    @classmethod
    def create_garden_network(cls):
        """Create a network of sample gardens for testing and demonstration."""
        # create Alice's garden
        a_list = []
        a_list.append(Plant("Oak Tree", 101, 20))
        a_list.append(FloweringPlant("Carnation", 26, 10, "pink"))
        a_list.append(PrizeFlower("Dandelion", 30, 25, "white", 22))
        alice = cls("Alice", a_list)

        # create Thomas' garden
        t_list = []
        t_list.append(Plant("Oak Tree", 101, 20))
        t_list.append(FloweringPlant("Carnation", 26, 10, "pink"))
        t_list.append(PrizeFlower("Rose", 30, 25, "white", 14))
        thomas = cls("Thomas", t_list)

        return [alice, thomas]

    @staticmethod
    class GardenStats:
        """Statistical analysis class for garden data."""

        def __init__(self, plant_list):
            """Initialize garden statistics."""
            self.plant_list = plant_list
            self.score: int

        def height_validation(self):
            """Validate that all plants have positive heights."""
            if (p.height > 0 for p in self.plant_list):
                print("Height validation test: True")
            else:
                print("Height validation test: False")

        def total(self):
            """Display the total number of managed gardens."""
            print(f"Total gardens managed: {GardenManager.total_gardens}")

        def score(self):
            """Calculate the total height score for the garden."""
            return sum(p.height for p in self.plant_list)

        def print_scores(self):
            """Print comparative scores for Alice's and Thomas's gardens."""
            print(f"Garden Scores - Alice: "
                  f"{sum(p.height for p in gardens[0].plant_list)}"
                  f", Thomas: "
                  f"{sum(p.height for p in gardens[1].plant_list)}")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    print("\n")
    gardens = GardenManager.create_garden_network()

    alice = gardens[0]
    alice.manage_grow()
    alice.report()

    stats = GardenManager.GardenStats(alice.plant_list)
    stats.height_validation()
    stats.print_scores()
    stats.total()

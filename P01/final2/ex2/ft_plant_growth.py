class Plant:
    """Represents a plant with growth capabilities."""

    def __init__(self, name, height, h_growth, age, a_growth):
        """Initialize a plant with growth parameters."""
        self.name = name
        self.height = height
        self.h_growth = h_growth
        self.age = age
        self.a_growth = a_growth

    def grow(self):
        """Simulate one growth cycle for the plant."""
        self.height += self.h_growth
        self.age += self.a_growth

    def getinfo(self):
        """Display the plant's current information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    lilly = Plant("Lilly of the valley", 3, 2, 2, 1)
    total_growth = 0
    initial_growth = lilly.height
    print("== Day 1 ==")
    lilly.getinfo()
    for i in range(1, 8):
        lilly.grow()
    final_growth = lilly.height
    print("== Day 7 ==")
    lilly.getinfo()
    print(f"Growth this week: +{final_growth-initial_growth}cm")

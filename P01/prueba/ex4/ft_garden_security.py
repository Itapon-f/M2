class Plant:
    """Represents a plant with security validation for attribute changes."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with security monitoring."""
        self.name = name
        self.height = height
        self.age = age

    def set_height(self, new_height):
        """Securely set the plant's height with validation."""
        if new_height < 0:
            print(f"Invalid operation attempted: height"
                  f" {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age):
        """Securely set the plant's age with validation."""
        if new_age < 0:
            print(f"Invalid operation attempted: {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def getinfo(self):
        """Display the current plant information."""
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    sample: Plant = Plant("Rose", 0, 0)
    print("=== Garden Security System ===")
    print(f"Plant created: {sample.name}")
    sample.set_height(25)
    sample.set_age(30)
    print("\n")
    sample.set_height(-5)
    print("\n")
    sample.getinfo()

def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        10/0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: So such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        crop_temperatures = {"tomato": 22, "lettuce": 18}
        crop_temperatures["corn"]
    except KeyError:
        print("Caught KeyError: 'missing_crop'\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, FileNotFoundError, ZeroDivisionError, KeyError):
        print("Caught an error but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()

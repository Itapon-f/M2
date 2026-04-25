def watering_system(plant: str):
    print(f"Watering {plant}")


def normal_test(normal_list):
    print("Testing normal watering...")
    print("Opening watering system")
    try:
        for p in normal_list:
            watering_system(p)
    except Exception:
        print(f"Error: cannot water {p} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed succesfully!\n")


def error_test(error_list: str):
    print("Testing with error...")
    print("Opening watering system")
    try:
        for p in error_list:
            if p is None:
                raise ValueError("Invalid plant")
            watering_system(p)
    except Exception:
        print(f"Error: cannot water {p} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    print("\n")


if __name__ == "__main__":
    normal_list = ["tomato", "lettuce", "carrots"]
    error_list = ["tomato", "lettuce", None]
    print("=== Garden Watering System ===\n")

    normal_test(normal_list)
    error_test(error_list)
    print("Cleanup always happens, even with errors!")

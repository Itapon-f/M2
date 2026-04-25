
def check_temperature(temp):
    try:
        # risky code
        t_input = int(temp)
        if t_input < 0:
            print(f"Error: {t_input} is too cold for plants (min 0ºC)\n")
        elif t_input > 40:
            print(f"Error: {t_input} is too hot for plants (max 40ºC)\n")
        else:
            print(f"Temperature {t_input}ºC is perfect for plants!\n")
    except Exception:
        print(f"Error: '{temp}' is not a valid number")
        # handling code so that the program does not crash


""" def check_temperature_input():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing Temperature: 25")
    check_temperature("25")
    print("Testing Temperature: abc")
    check_temperature("abc")
    print("Testing Temperature: 100")
    check_temperature("100")
    print("Testing Temperature: 0")
    check_temperature("-50")
    print("All tests are completed - program didn't crash!")


if __name__ == "__main__":
    check_temperature_input() """

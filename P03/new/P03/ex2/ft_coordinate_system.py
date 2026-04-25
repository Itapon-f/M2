import math


def get_player_pos() -> None:
    origin: tuple[
        float, float, float
        ] = (
            0.0, 0.0, 0.0
            )

    # First coordinates
    xyz: str = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        xyz_splitted: list[str] = xyz.split(",")
        x = float(xyz_splitted[0])
        y = float(xyz_splitted[1])
        z = float(xyz_splitted[2])
    except ValueError as e:
        print(f"Error on parameter: {e}")
        xyz = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            xyz_splitted: list[str] = xyz.split(",")
            x = float(xyz_splitted[0])
            y = float(xyz_splitted[1])
            z = float(xyz_splitted[2])
        except ValueError:
            print("Invalid syntax, again!")
            return

    position: tuple[float, float, float] = (x, y, z)
    print(f"Got a first tuple: ({x:.1f}, {y:.1f}, {z:.1f})")
    print(f"It includes: X={x:.1f}, Y={y:.1f}, Z={z:.1f}")
    distance = math.sqrt(
        (position[0]-origin[0])**2 +
        (position[1]-origin[1])**2 +
        (position[2]-origin[2])**2)
    print(f"Distance to the center: {distance:.2f}\n")

    # Second coordinates
    print("Get a second set of coordinates")
    xyz2: str = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        xyz_splitted2: list[str] = xyz2.split(",")
        x2 = float(xyz_splitted2[0])
        y2 = float(xyz_splitted2[1])
        z2 = float(xyz_splitted2[2])
    except ValueError as e:
        print(f"Error on parameter: {e}")
        xyz2 = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            xyz_splitted2: list[str] = xyz2.split(",")
            x2 = float(xyz_splitted2[0])
            y2 = float(xyz_splitted2[1])
            z2 = float(xyz_splitted2[2])
        except ValueError:
            print("Invalid syntax, again!")
            return

    position2: tuple[float, float, float] = (x2, y2, z2)
    distance = math.sqrt((position2[0]-position[0])**2 +
                         (position2[1]-position[1])**2 +
                         (position2[2]-position[2])**2)
    print(f"Distance between first and second position: {distance:.2f}\n")


if __name__ == "__main__":
    get_player_pos()


""" def ft_test_tracker():
    print("=== Game Coordinate System ===\n")

    origin: tuple[int, int, int] = (0, 0, 0)
    position: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {position}")
    distance = math.sqrt((position[0]-origin[0])**2 +
      (position[1]-origin[1])**2 +
      (position[2]-origin[2])**2)
    print(f"Distance between {origin} and {position}: {distance:.2f}\n")

    coordinates = "3,4,0"
    print(f'Parsing coordinates: ''"'f'{coordinates}''"')
    xyz = coordinates.split(",")
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    parsed_position = (x, y, z)
    print(f"Parsed position: {parsed_position}")
    distance = math.sqrt((x)**2 + (y)**2 + (z)**2)
    print(f"Distance between {origin} and {parsed_position}: {distance:.1f}\n")

    inv_coordinates = "abc,def,ghi"
    xyz = inv_coordinates.split(",")
    try:
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
    except ValueError as e:
        message = "Parsing invalid coordinates: "
        "invalid literal for int() with base 10: ""'"f"{xyz[0]}""'"
        print(f"{message}")
        print(f'Error details - Type: "
        "ValueError, Args: ''"'f'({message},)''"\n')

    print("Unpacking demonstration")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: x={x}, y={y}, z={z}") """

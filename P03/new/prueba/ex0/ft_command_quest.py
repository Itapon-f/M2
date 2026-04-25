import sys


def ft_command_quest(args: list[str]) -> None:
    """Receives arguments and gives information about them"""
    index: int = 0

    print("=== Command Quest ===")

    num: int = len(args)
    if len(args) == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {num - 1}")
        for arg in args[1:]:
            index += 1
            print(f"Argument {index}: {arg}")
    print(f"Total arguments: {num}")


if __name__ == "__main__":
    ft_command_quest(sys.argv)

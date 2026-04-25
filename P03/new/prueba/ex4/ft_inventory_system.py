import sys


def ft_inventory_system(args: list[str]) -> None:
    print("=== Inventory System Analysis ===\n")

    inventory: dict[str, int] = {}
    # separate the name from the value and add a quantity to each item
    for arg in args[1:]:
        if ":" not in arg:
            print(f"Error - imvalid parameter '{arg}'")
            continue
        item, quantity = arg.split(":")

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = int(qty)

    items = list(inventory.keys())
    total = sum(inventory.values())
    if total == 0:
        print("Inventory is empty!")
        return
    print(f"\nGot inventory: {inventory}")
    print(f"Item list: {items}")
    print(f"Total quantity of {len(items)}: {sum(inventory.values())}\n")

    # === Current Inventory ===
    for item, quantity in inventory.items():
        percentage = quantity / total * 100
        print(f"{item}: represents ({percentage:.1f}%)")

    # === Inventory Statistics ===
    most_abundant = None
    least_abundant = None
    max_qty = -1
    min_qty = float("inf")
    for item, quantity in inventory.items():
        if quantity > max_qty:
            most_abundant = item
            max_qty = quantity
    print(f"\n Item most abundant: {most_abundant} ({max_qty} units)")

    for item, quantity in inventory.items():
        if quantity < min_qty:
            least_abundant = item
            min_qty = quantity
    print(f"Item least abundant: {least_abundant} ({min_qty} units)")

    # === Management Suggestions ===
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system(sys.argv)

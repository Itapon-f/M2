import sys


def ft_inventory_system(args: list[str])->None:
    print("=== Inventory System Analysis ===")
    """     catalog = {'pixel_sword': {'type': 'weapon', 'value': 150, 'rarity': 'common'}, 
                    'quantum_ring': {'type': 'accessory', 'value': 500, 'rarity': 'rare'}, 
                    'health_byte': {'type': 'consumable', 'value': 25, 'rarity': 'common'}, 
                    'data_crystal': {'type': 'material', 'value': 1000, 'rarity': 'legendary'}, 
                    'code_bow': {'type': 'weapon', 'value': 200, 'rarity': 'uncommon'}}
    """
    inventory = {}
    # separate the name from the value and add a quantity to each item
    for arg in sys.argv[1:]:
        item, quantity = arg.split(":")
        inventory[item] = int(quantity)

    total = sum(inventory.values())
    if total == 0:
        print("Inventory is empty!")
        return
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for item, quantity in inventory.items():
        percentage = quantity/total*100
        if quantity > 1:
            print(f"{item}: {quantity} units ({percentage:.1f}%)")
        else:
            print(f"{item}: {quantity} unit ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_abundant = None
    least_abundant = None
    max_qty = -1
    min_qty = float("inf") # Positive infinity, larger than any number
    for item, quantity in inventory.items():
        if quantity >  max_qty:
            most_abundant = item
            max_qty = quantity
    print(f"Most abundant: {most_abundant} ({max_qty} units)")

    for item, quantity in inventory.items():
        if quantity <  min_qty:
            least_abundant = item
            min_qty = quantity
    print(f"Least abundant: {least_abundant} ({min_qty} units)")

    print("\n=== Item Categories ===")
    moderate = []
    scarce = []
    for item, quantity in inventory.items():
        if quantity >= 5:
            moderate.append(item)
        else:
            scarce.append(item)
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    catalog_items = set(catalog.keys())
    inventory_items = set(inventory.keys())
    to_restock = catalog_items.difference(inventory_items)
    print(f"Restock needed: {to_restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys = inventory.keys()
    print(f"Dictionary keys: {keys}")
    values = inventory.values()
    print(f"Dictionary values: {values}")


if __name__ == "__main__":
    ft_inventory_system(sys.argv)




"""
In the terminal you give the information about the items in the inventory. Examples:
   players = {'alice': {'items': {'pixel_sword': 1, 'code_bow': 1, 'health_byte': 1, 'quantum_ring': 3, 'data_crystal': 2}, 'total_value': 1875, 'item_count': 6}, 
                'bob': {'items': {'code_bow': 3, 'pixel_sword': 2}, 'total_value': 900, 'item_count': 5}, 
                'charlie': {'items': {'pixel_sword': 1, 'code_bow': 1}, 'total_value': 350, 'item_count': 2}, 
                'diana': {'items': {'code_bow': 3, 'pixel_sword': 3, 'health_byte': 3, 'data_crystal': 3}, 'total_value': 4125, 'item_count': 12}}
 """

"""     legendary = 0
    for item, quantity in inventory.items():
        if catalog[item]["rarity"] == "legendary":
            legendary += quantity
    print(f"Legendary item number = {legendary}") """
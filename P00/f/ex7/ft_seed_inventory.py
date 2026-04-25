def ft_seed_inventory(vegetable, nbr, unit):
    if unit == "packets":
        print(f"{vegetable} seeds: {nbr} packets available")
    if unit == "grams":
        print(f"{vegetable} seeds: {nbr} grams total")
    if unit == "area":
        print(f"{vegetable} seeds: {nbr} square meters")


""" if __name__ == "__main__":
    ft_seed_inventory("Tomato", 15, "packets")
    ft_seed_inventory("Carrot", 15, "grams")
    ft_seed_inventory("Lettuce", 15, "area")
 """

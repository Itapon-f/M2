def ft_count_harvest_recursive(total_days=None, day=1):
    if total_days is None:
        total_days: int = int(input("Days until harvest: "))
    if day <= total_days:
        print(f"Day {day}")
        ft_count_harvest_recursive(total_days, day+1)
    else:
        print("Harvest time!")


"""
if __name__ == "__main__":
    ft_count_harvest_recursive()
 """

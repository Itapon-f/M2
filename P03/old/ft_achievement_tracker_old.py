def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")
    alice = {'first_blood', 'pixel_perfect', 'speed_runner', 'first_blood', 'first_blood', 'best_tracker'}
    bob = {'level_master', 'boss_hunter', 'treasure_seeker', 'level_master', 'level_master', 'best_tracker'}
    charlie = {'treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood', 'boss_hunter', 'first_blood', 'best_tracker', 'boss_hunter', 'first_blood'}
    diana = {'first_blood', 'combo_king', 'level_master', 'treasure_seeker', 'speed_runner', 'best_tracker', 'combo_king', 'combo_king', 'level_master'}
    eve = {'level_master', 'treasure_seeker', 'first_blood', 'treasure_seeker', 'first_blood', 'best_tracker', 'treasure_seeker'}
    frank = {'explorer', 'boss_hunter', 'first_blood', 'explorer', 'first_blood', 'boss_hunter', 'best_tracker'}
    players = {"alice": alice, "bob": bob, "charlie": charlie, "diana":diana, "eve": eve, "frank": frank}

    for player, achievements in players.items():
        print(f"Player {player} achievements: {achievements}")
    print("\n")
    
    print("=== Achievement Analytics ===")
    all_achievements = alice.union(bob).union(charlie).union(diana).union(eve).union(frank)
    print(f"All unique achievemnts: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_achievement = alice.intersection(bob).intersection(charlie).intersection(diana).intersection(eve).intersection(frank)
    print(f"Common to all players: {common_achievement}")

    alice_rare = alice.difference(bob.union(charlie).union(diana).union(eve).union(frank))
    bob_rare = bob.difference(alice.union(charlie).union(diana).union(eve).union(frank))
    charlie_rare = charlie.difference(alice.union(bob).union(diana).union(eve).union(frank))
    diana_rare = diana.difference(alice.union(bob).union(charlie).union(eve).union(frank))
    eve_rare = eve.difference(alice.union(bob).union(charlie).union(diana).union(frank))
    frank_rare = frank.difference(alice.union(bob).union(charlie).union(diana).union(eve))

    rare_achievements = alice_rare.union(bob_rare).union(charlie_rare).union(diana_rare).union(eve_rare).union(frank_rare)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    alice_bob = alice.intersection(bob)
    print(f"Alive vs Bob common: {alice_bob}")
    only_alice = alice.difference(bob)
    print(f"Alice unique: {only_alice}")
    only_bob = bob.difference(alice)
    print(f"Bob unique: {only_bob}")


if __name__ == "__main__":
    ft_achievement_tracker()
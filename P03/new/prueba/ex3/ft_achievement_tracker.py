def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")
    alice = {'first_blood', 'pixel_perfect',
             'speed_runner', 'first_blood',
             'first_blood', 'best_tracker'}
    bob = {'level_master', 'boss_hunter',
           'treasure_seeker', 'level_master',
           'level_master', 'best_tracker'}
    charlie = {'treasure_seeker', 'boss_hunter',
               'combo_king', 'first_blood',
               'boss_hunter', 'first_blood',
               'best_tracker', 'boss_hunter', 'first_blood'}
    diana = {'first_blood', 'combo_king', 'level_master',
             'treasure_seeker', 'speed_runner', 'best_tracker',
             'combo_king', 'combo_king', 'level_master'}
    eve = {'level_master', 'treasure_seeker', 'first_blood',
           'treasure_seeker', 'first_blood', 'best_tracker',
           'treasure_seeker'}
    frank = {'explorer', 'boss_hunter', 'first_blood',
             'explorer', 'first_blood', 'boss_hunter',
             'best_tracker'}
    players = {"alice": alice,
               "bob": bob,
               "charlie": charlie,
               "diana": diana,
               "eve": eve,
               "frank": frank}

    for player, achievements in players.items():
        print(f"Player {player} {achievements}")
    print("\n")

    all_achievements = alice.union(
        bob).union(charlie).union(diana).union(eve).union(frank)
    print(f"All distinct achievemnts: {all_achievements}\n")

    common_achievement = alice.intersection(
        bob).intersection(charlie).intersection(
            diana).intersection(eve).intersection(frank)
    print(f"Common achievements: {common_achievement}\n")

    alice_rare = alice.difference(
        bob.union(charlie).union(diana).union(eve).union(frank))
    print(f"Only Alice has: {alice_rare}")
    bob_rare = bob.difference(
        alice.union(charlie).union(diana).union(eve).union(frank))
    print(f"Only Bob has: {bob_rare}")
    charlie_rare = charlie.difference(
        alice.union(bob).union(diana).union(eve).union(frank))
    print(f"Only Charlie has: {charlie_rare}")
    diana_rare = diana.difference(
        alice.union(bob).union(charlie).union(eve).union(frank))
    print(f"Only Diana has: {diana_rare}")

    alice_missing = all_achievements.difference(alice)
    print(f"\nAlice is missing: {alice_missing}")
    bob_missing = all_achievements.difference(bob)
    print(f"Bob is missing: {bob_missing}")
    charlie_missing = all_achievements.difference(charlie)
    print(f"Charlie is missing: {charlie_missing}")
    diana_missing = all_achievements.difference(diana)
    print(f"Diana is missing: {diana_missing}")


if __name__ == "__main__":
    ft_achievement_tracker()

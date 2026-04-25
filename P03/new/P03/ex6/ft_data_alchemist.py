import random


def ft_scores(capitalized_list: list[str]) -> None:
    score_dict: dict[str, int] = {player:
                                  random.randint(0, 1000)
                                  for player in capitalized_list}
    print(f"Score dict: {score_dict}")
    score_average: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {score_average:.2f}")
    high_scores: dict[str, int] = {player:
                                   score for player, score
                                   in score_dict.items()
                                   if score > score_average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    player_list: list[str] = ['Alice', 'bob', 'Charlie',
                              'dylan', 'Emma', 'Gregory',
                              'john', 'kevin', 'Liam']
    print(f"Initial list of players: {player_list}")
    capitalized_list: list[str] = [player.capitalize()
                                   for player in player_list]
    print(f"New list with all names capitalized: {capitalized_list}")
    selectioned_list: list[str] = [player for player
                                   in player_list
                                   if player[0].isupper()]
    print(f"New list of capitalized names only: {selectioned_list}\n")

    ft_scores(capitalized_list)

import sys


def ft_score_analytics(scores: list[str]) -> None:
    """Manages received scores"""
    print("=== Player Score Analytics ===")
    intscores: list[int] = []
    try:
        for score in scores[1:]:
            intscores.append(int(score))
    except ValueError:
        for score in scores[1:]:
            print(f"Invalid parameter: {score}")
    else:
        if not intscores:
            print("No scores provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2>...")
            return
        print(f"Scores processed: {scores[1:]}")
        total_players: int = len(intscores)
        print(f"Total players: {total_players}")
        total_score = sum(intscores)
        print(f"Total score: {total_score}")
        average: float = sum(intscores) / len(intscores)
        print(f"Average score: {average}")
        high: int = max(intscores)
        print(f"High score: {high}")
        low: int = min(intscores)
        print(f"Low score: {low}")
        srange: int = high - low
        print(f"Score range: {srange}")


if __name__ == "__main__":
    ft_score_analytics(sys.argv)

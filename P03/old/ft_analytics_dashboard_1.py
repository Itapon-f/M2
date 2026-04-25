# What is a comprehension? A concise way to create collections using iteration, filtering, and transformation in one expression.

def ft_list_comprehension(data: dict): # data is a dictionary with nested dicts
    print ("=== List Comprehension Examples ===")
    high_scorers: list[str] = [name for player, stats in data["players"].items() 
                                if stats["total_score"] >= 2000]
    print(f"High scorers (<2000): {high_scorers}")
    scores_doubled: list[int] = [player["total_score"]*2 for player in data["players"].values()]
    # According to the data inside ["palyers"] the items are each player with its own data and 
    # to acces the values inside each plare you need to do ["palyers"].item() and for each go:
    # "name" -> "stat": value || change "stat" "player" -> values, then you are taking each name 
    # with its points
    print(f"Scores doubled: {scores_doubled}")
    # active_players: list[str] = [name for player in data["sessions"].items()] 
    # session is a list, not a dictionary!!!
    # better: introducing a set comprehension inside (as if it were a dictionary with objects) ->
    active_players: list({session["player"] for session in data["sessions"]})
    print(f"Active players: {active_players}")

        # dict: Tells Python this variable is a dictionary.
        # [ ... ]: These brackets contain the "sub-types."
        # str: The first type inside the brackets always represents the Key.
        # ,: Separates the key type from the value type.
        # int: The second type represents the Value.

def ft_dict_comprehension(data: ):
    print("\n=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {name: value["level"] for name, value in data["players"].items()}
    print(f"Player scores: {player_scores}")
    score_categories: dict[str, int] = {categories: value("score_categories") for score, value in data["score_categories"].items()}
    print(f"Score categories: {score_categories}")
    achievements_counts: dict[str, int] = {name: value("achievements_count") for name, value in data["players"].items()}
    print(f"Achievement counts: {achievements_counts}")

def ft_set_comprehension(data: ):
    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: ")
    print(f"unique achievements: ")
    game_modes: dict[str] = {mode for mode in data["game_modes"]}
    print(f"Game modes: {game_modes}")


def ft_combined_analysis(data: ):
    print("\n=== Combined analysis ===")
    print(f"Total players: {len(data["players"])}")
    print(f"Total unique achiements: {total_un_achievements}")
    print(f"Average score: {average}")
    print(f"Top performer: {}")


if __name__ == "__main__":
    print("=== List Comprehension Examples ===\n")

    data = {
            "players":{
                "alice":{
                    "level":41,
                    "total_score":2824,
                    "sessions_played":13,
                    "favorite_mode":"ranked",
                    "achievements_count":5
                },
                "bob":{
                    "level":16,
                    "total_score":4657,
                    "sessions_played":27,
                    "favorite_mode":"ranked",
                    "achievements_count":2
                },
                "charlie":{
                    "level":44,
                    "total_score":9935,
                    "sessions_played":21,
                    "favorite_mode":"ranked",
                    "achievements_count":7
                },
                "diana":{
                    "level":3,
                    "total_score":1488,
                    "sessions_played":21,
                    "favorite_mode":"casual",
                    "achievements_count":4
                },
                "eve":{
                    "level":33,
                    "total_score":1434,
                    "sessions_played":81,
                    "favorite_mode":"casual",
                    "achievements_count":7
                },
                "frank":{
                    "level":15,
                    "total_score":8359,
                    "sessions_played":85,
                    "favorite_mode":"competitive",
                    "achievements_count":1
                }
            },
            "sessions":[
                {
                    "player":"bob",
                    "duration_minutes":94,
                    "score":1831,
                    "mode":"competitive",
                    "completed":False
                },
                {
                    "player":"bob",
                    "duration_minutes":32,
                    "score":1478,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"diana",
                    "duration_minutes":17,
                    "score":1570,
                    "mode":"competitive",
                    "completed":False
                },
                {
                    "player":"alice",
                    "duration_minutes":98,
                    "score":1981,
                    "mode":"ranked",
                    "completed":True
                },
                {
                    "player":"diana",
                    "duration_minutes":15,
                    "score":2361,
                    "mode":"competitive",
                    "completed":False
                },
                {
                    "player":"eve",
                    "duration_minutes":29,
                    "score":2985,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"frank",
                    "duration_minutes":34,
                    "score":1285,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"alice",
                    "duration_minutes":53,
                    "score":1238,
                    "mode":"competitive",
                    "completed":False
                },
                {
                    "player":"bob",
                    "duration_minutes":52,
                    "score":1555,
                    "mode":"casual",
                    "completed":False
                },
                {
                    "player":"frank",
                    "duration_minutes":92,
                    "score":2754,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"eve",
                    "duration_minutes":98,
                    "score":1102,
                    "mode":"casual",
                    "completed":False
                },
                {
                    "player":"diana",
                    "duration_minutes":39,
                    "score":2721,
                    "mode":"ranked",
                    "completed":True
                },
                {
                    "player":"frank",
                    "duration_minutes":46,
                    "score":329,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"charlie",
                    "duration_minutes":56,
                    "score":1196,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"eve",
                    "duration_minutes":117,
                    "score":1388,
                    "mode":"casual",
                    "completed":False
                },
                {
                    "player":"diana",
                    "duration_minutes":118,
                    "score":2733,
                    "mode":"competitive",
                    "completed":True
                },
                {
                    "player":"charlie",
                    "duration_minutes":22,
                    "score":1110,
                    "mode":"ranked",
                    "completed":False
                },
                {
                    "player":"frank",
                    "duration_minutes":79,
                    "score":1854,
                    "mode":"ranked",
                    "completed":False
                },
                {
                    "player":"charlie",
                    "duration_minutes":33,
                    "score":666,
                    "mode":"ranked",
                    "completed":False
                },
                {
                    "player":"alice",
                    "duration_minutes":101,
                    "score":292,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"frank",
                    "duration_minutes":25,
                    "score":2887,
                    "mode":"competitive",
                    "completed":True
                },
                {
                    "player":"diana",
                    "duration_minutes":53,
                    "score":2540,
                    "mode":"competitive",
                    "completed":False
                },
                {
                    "player":"eve",
                    "duration_minutes":115,
                    "score":147,
                    "mode":"ranked",
                    "completed":True
                },
                {
                    "player":"frank",
                    "duration_minutes":118,
                    "score":2299,
                    "mode":"competitive",
                    "completed":False
                },
                {
                    "player":"alice",
                    "duration_minutes":42,
                    "score":1880,
                    "mode":"casual",
                    "completed":False
                },
                {
                    "player":"alice",
                    "duration_minutes":97,
                    "score":1178,
                    "mode":"ranked",
                    "completed":True
                },
                {
                    "player":"eve",
                    "duration_minutes":18,
                    "score":2661,
                    "mode":"competitive",
                    "completed":True
                },
                {
                    "player":"bob",
                    "duration_minutes":52,
                    "score":761,
                    "mode":"ranked",
                    "completed":True
                },
                {
                    "player":"eve",
                    "duration_minutes":46,
                    "score":2101,
                    "mode":"casual",
                    "completed":True
                },
                {
                    "player":"charlie",
                    "duration_minutes":117,
                    "score":1359,
                    "mode":"casual",
                    "completed":True
                }
                ],
                "game_modes":[
                    "casual",
                    "competitive",
                    "ranked"
                ],
                "score_categories":[
                    "low":1000,
                    "medium":2000,
                    "high":3000
                ]
                "achievements":[
                    "first_blood",
                    "level_master",
                    "speed_runner",
                    "treasure_seeker",
                    "boss_hunter",
                    "pixel_perfect",
                    "combo_king",
                    "explorer"
                ]
            }

    ft_list_comprehension(data)
    ft_dict_comprehension()
    ft_set_comprehension()
    ft_combined_analysis()

import random
from collections.abc import Generator


def gen_event() -> Generator[tuple[str, str]]:
    """ Generates an event with a random mix of a name and an action"""
    players: list = ["alice", "bob", "charlie", "diana"]
    actions: list = ["jump", "run", "attack", "defend",
                     "eat", "sleep", "swim", "climb"]

    while True:  # endless loop
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(ten_list: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """ prints an event and return the list without the printed event"""
    index = random.randrange(len(ten_list))
    event = ten_list.pop(index)
    print(f"Got event from list: {event}")
    print(f"Remains in list: {ten_list}")
    return ten_list


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    id = 0
    event_gen = gen_event()
    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_list: list[tuple[str, str]] = [next(event_gen) for j in range(10)]
    print(f"Built list of 10 events: {ten_list}")

    for event in ten_list:
        consume_event(ten_list)

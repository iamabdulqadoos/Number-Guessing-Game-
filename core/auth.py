from utils.file_utils import read_file, append_file, PLAYERS_FILE


def load_players():
    return read_file(PLAYERS_FILE)


def save_player(name):
    players = load_players()

    if name not in players:
        append_file(PLAYERS_FILE, name)


def login():
    while True:
        name = input("Enter your name: ").strip()

        if name == "":
            print("Name cannot be empty!")
            continue

        if name in load_players():
            print(f"\nWelcome back, {name}! 🎮")
        else:
            print(f"\nNew Player Registered: {name} 🎉")
            save_player(name)

        return name
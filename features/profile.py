from utils.file_utils import read_file, HISTORY_FILE


def my_profile(name):
    games = 0
    best_attempts = None
    best_time = None
    last_date = "N/A"

    data = read_file(HISTORY_FILE)

    for line in data:
        d = line.split(",")

        if d[0] == name:
            games += 1

            a = int(d[2])
            t = float(d[3])

            if best_attempts is None or a < best_attempts:
                best_attempts = a

            if best_time is None or t < best_time:
                best_time = t

            last_date = d[4]

    print("\n===== MY PROFILE =====")
    print(f"Name: {name}")
    print(f"Games Played: {games}")
    print(f"Best Attempts: {best_attempts}")
    print(f"Best Time: {best_time}")
    print(f"Last Played: {last_date}")
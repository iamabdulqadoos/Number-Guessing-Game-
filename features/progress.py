from utils.file_utils import read_file, HISTORY_FILE


def track_progress(name):
    attempts = []
    times = []

    data = read_file(HISTORY_FILE)

    for line in data:
        d = line.split(",")

        if d[0] == name:
            attempts.append(int(d[2]))
            times.append(float(d[3]))

    if not attempts:
        print("No games found!")
        return

    print("\n===== PROGRESS =====")
    print(f"Total Games: {len(attempts)}")
    print(f"Best Attempts: {min(attempts)}")
    print(f"Worst Attempts: {max(attempts)}")
    print(f"Average Attempts: {sum(attempts)/len(attempts):.2f}")
    print(f"Best Time: {min(times)}")
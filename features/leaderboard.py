from utils.file_utils import read_file, HISTORY_FILE


def leaderboard():
    print("\n===== LEADERBOARD =====")

    data = read_file(HISTORY_FILE)

    records = []

    for line in data:
        name, level, attempts, time_taken, date = line.split(",")
        records.append((name, int(attempts), float(time_taken)))

    records.sort(key=lambda x: (x[1], x[2]))

    for i, r in enumerate(records[:10], 1):
        print(f"{i}. {r[0]} | Attempts: {r[1]} | Time: {r[2]}")
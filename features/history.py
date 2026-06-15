from utils.file_utils import read_file, HISTORY_FILE


def view_history(name):
    print("\n===== YOUR HISTORY =====")

    data = read_file(HISTORY_FILE)

    found = False

    for line in data:
        d = line.split(",")

        if d[0] == name:
            print(f"{d[4]} | {d[1]} | Attempts: {d[2]} | Time: {d[3]}")
            found = True

    if not found:
        print("No history found!")
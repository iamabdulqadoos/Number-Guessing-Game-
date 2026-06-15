import os

# ==================================================
# SAFE BASE DIRECTORY (IMPORTANT FIX)
# ==================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

PLAYERS_FILE = os.path.join(DATA_DIR, "players.txt")
HISTORY_FILE = os.path.join(DATA_DIR, "history.txt")
REVIEWS_FILE = os.path.join(DATA_DIR, "reviews.txt")


# ==================================================
# CREATE DATA FOLDER AUTOMATICALLY
# ==================================================

os.makedirs(DATA_DIR, exist_ok=True)


# ==================================================
# FILE HELPERS
# ==================================================

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except:
        return []


def append_file(file_path, data):
    with open(file_path, "a") as file:
        file.write(data + "\n")
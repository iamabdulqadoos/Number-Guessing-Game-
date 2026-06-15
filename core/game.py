import random
import time
from datetime import datetime
from utils.file_utils import append_file, HISTORY_FILE


def save_history(name, level, attempts, time_taken):
    date = datetime.now().strftime("%Y-%m-%d")
    append_file(HISTORY_FILE, f"{name},{level},{attempts},{time_taken},{date}")


def play_game(name):

    while True:
        print("\nSelect Level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-500)")

        choice = input("Enter choice: ")

        if choice == "1":
            max_num = 50
            level = "Easy"
        elif choice == "2":
            max_num = 100
            level = "Medium"
        elif choice == "3":
            max_num = 500
            level = "Hard"
        else:
            print("Invalid choice!")
            continue

        secret = random.randint(1, max_num)
        attempts = 0
        start_time = time.time()

        print(f"\nGuess number between 1 and {max_num}")

        while True:
            try:
                guess = int(input("Enter guess: "))

                if guess < 1 or guess > max_num:
                    print("Out of range!")
                    continue

            except:
                print("Invalid input!")
                continue

            attempts += 1

            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")
            else:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)

                print("\n🎉 YOU WON!")
                print(f"Attempts: {attempts}")
                print(f"Time: {total_time}")

                save_history(name, level, attempts, total_time)

                while True:
                    print("\n1. Play Again")
                    print("2. Menu")

                    r = input("Choose: ")

                    if r == "1":
                        break
                    elif r == "2":
                        return
                    else:
                        print("Invalid choice!")

                break
from core.auth import login
from core.game import play_game
from features.history import view_history
from features.leaderboard import leaderboard
from features.profile import my_profile
from features.progress import track_progress
from features.reviews import add_review, view_reviews


def menu(name):

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Play Game")
        print("2. History")
        print("3. Leaderboard")
        print("4. Profile")
        print("5. Progress")
        print("6. Add Review")
        print("7. View Reviews")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_game(name)
        elif choice == "2":
            view_history(name)
        elif choice == "3":
            leaderboard()
        elif choice == "4":
            my_profile(name)
        elif choice == "5":
            track_progress(name)
        elif choice == "6":
            add_review(name)
        elif choice == "7":
            view_reviews()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


def main():
    print("====================================")
    print("   NUMBER GUESSING GAME PROJECT     ")
    print("====================================")

    name = login()
    menu(name)


main()
from utils.file_utils import append_file, REVIEWS_FILE


def add_review(name):
    rating = input("Rate (1-5): ")
    review = input("Write review: ")

    append_file(REVIEWS_FILE, f"{name},{rating},{review}")

    print("Thanks for feedback!")


def view_reviews():
    print("\n===== REVIEWS =====")

    try:
        with open(REVIEWS_FILE, "r") as file:
            for line in file:
                name, rating, review = line.strip().split(",", 2)
                print(f"\n{name} ({rating}/5)")
                print(review)
    except:
        print("No reviews yet!")
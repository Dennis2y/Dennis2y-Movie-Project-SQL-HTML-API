import random
import statistics
import movie_storage
from movie_storage import get_movies
from web_generator import generate_website
from omdb_api import get_movie_data  

def list_movies(movies):
    """Displays all movies in the database."""
    if not movies:
        print("\nNo movies found.")
        return
    print("\nMovies List:")
    for title, info in movies.items():
        print(f"{title} ({info['year']}): {info['rating']}")

def get_valid_input(prompt, input_type=str, validation=None, error_message="Invalid input!"):
    """Handles user input validation."""
    while True:
        user_input = input(prompt).strip()
        if input_type == str and not user_input:
            print("Input cannot be empty. Try again.")
            continue
        try:
            value = input_type(user_input)
            if validation and not validation(value):
                print(error_message)
            return value
        except ValueError:
            print(error_message)

def add_movie(movies):
    """Adds a new movie using OMDb API and updates the JSON file."""
    title = get_valid_input("Enter movie title: ", str)

    if title in movies:
        print(f"Movie '{title}' already exists!")
        return

    # Trying to get movie data from the OMDb API
    movie_data = get_movie_data(title)

    if movie_data:
        year = movie_data["year"]
        rating = movie_data["rating"]

        # If rating from API is missing or zero, ask the user
        if rating == 0:
            rating = get_valid_input("Enter movie rating (0-10): ", float, lambda r: 0 <= r <= 10, "Enter a valid rating (0-10).")

        movies[title] = {"year": year, "rating": rating}
        movie_storage.add_movie(title, year, rating)
        print(f"✅ Movie '{title}' added successfully!")
    else:
        print("❌ Could not add movie due to missing API data.")

def delete_movie(movies):
    """Deletes a movie from the database and updates the JSON file."""
    if not movies:
        print("No movies available to delete.")
        return
    title = get_valid_input("Enter movie title to delete: ", str)
    if title in movies:
        del movies[title]
        movie_storage.delete_movie(title)
        print(f"Movie '{title}' deleted.")
    else:
        print("Movie not found.")

def update_movie(movies):
    """Updates a movie's rating and saves the change."""
    if not movies:
        print("No movies available to update.")
        return
    title = get_valid_input("Enter movie title to update: ", str)
    if title in movies:
        rating = get_valid_input("Enter new rating (0-10): ", float, lambda r: 0 <= r <= 10, "Enter a valid rating (0-10).")
        movies[title]["rating"] = rating
        movie_storage.update_movie(title, rating)
        print(f"Movie '{title}' updated.")
    else:
        print("Movie not found.")

def stats(movies):
    """Displays statistics about movie ratings."""
    if not movies:
        print("No movies available.")
        return
    ratings = [info["rating"] for info in movies.values()]
    print("\nStatistics:")
    print(f"Average Rating: {statistics.mean(ratings):.1f}")
    print(f"Highest Rated Movie: {max(movies, key=lambda x: movies[x]['rating'])}")
    print(f"Lowest Rated Movie: {min(movies, key=lambda x: movies[x]['rating'])}")

def random_movie(movies):
    """Picks a random movie."""
    if not movies:
        print("No movies available.")
        return
    title = random.choice(list(movies.keys()))
    print(f"\nRandom Movie Pick: {title} ({movies[title]['year']}) - {movies[title]['rating']}")

def search_movie(movies):
    """Searches for movies by title."""
    search = get_valid_input("Enter part of movie title: ", str).lower()
    found = {title: info for title, info in movies.items() if search in title.lower()}
    if found:
        list_movies(found)
    else:
        print("No matching movies found.")

def movies_sorted_by_rating(movies):
    """Lists movies sorted by rating (highest to lowest)."""
    if not movies:
        print("No movies available.")
        return
    sorted_movies = dict(sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True))
    list_movies(sorted_movies)

def main():
    # Get the list of movies from the storage (e.g., database or JSON)
    movies = get_movies()
    if movies is None:
        movies = {}  # If no movies, initialize an empty dictionary

    while True:
        print("\nMenu:")
        print("0. Exit")
        print("1. List Movies")
        print("2. Add Movie")
        print("3. Delete Movie")
        print("4. Update Movie")
        print("5. Stats")
        print("6. Random Movie")
        print("7. Search Movie")
        print("8. Movies Sorted by Rating")
        print("9. Generate Website") 
        choice = input("Enter your choice (0-9): ").strip()
        if choice == "0":
            print("Bye!")
            break
        elif choice == "1":
            list_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            update_movie(movies)
        elif choice == "5":
            stats(movies)
        elif choice == "6":
            random_movie(movies)
        elif choice == "7":
            search_movie(movies)
        elif choice == "8":
            movies_sorted_by_rating(movies)
        elif choice == "9":
            generate_website()  # Call the function to generate the website
        else:
            print("Invalid choice. Please enter a number from 0 to 9.")

if __name__ == "__main__":
    main()

import random
import statistics
import movie_storage
from movie_storage import get_movies
from jinja2 import Template  # Importing jinja2 for template rendering
import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
OMDB_API_KEY = os.getenv('OMDB_API_KEY')


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
                continue
            return value
        except ValueError:
            print(error_message)


def add_movie(movies):
    """Adds a new movie and updates the JSON file."""
    title = get_valid_input("Enter movie title: ", str)
    # Checking for duplicate movie title, case-insensitive
    if any(existing_title.lower() == title.lower() for existing_title in movies):
        print(f"Movie '{title}' already exists!")
        return
    year = get_valid_input("Enter year of release: ",int, lambda y: 1800 <= y <= 2100,
                           "Enter a valid year (1800-2100).")
    rating = get_valid_input("Enter movie rating (0-10): ", float, lambda r: 0 <= r <= 10,
                             "Enter a valid rating (0-10).")

    # Fetching poster URL from OMDb API
    poster_url = fetch_poster_url(title)

    if not poster_url:
        print(f"Could not fetch poster for {title}. Please provide a poster URL manually.")
        poster_url = get_valid_input("Enter movie poster URL: ", str)  # Fall back to manual input if no poster is found

    # Passing title, year, rating, and poster URL when calling add_movie
    movie_storage.add_movie(title, year, rating, poster_url)

    print(f"Movie '{title}' added.")


def fetch_poster_url(title):
    """Fetches the movie poster URL from OMDb API."""
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Checking if the movie was found and if it has a poster
    if data.get("Response") == "True" and data.get("Poster") != "N/A":
        return data.get("Poster")
    else:
        print(f"Could not find a poster for the movie: {title}")
        return None


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
        rating = get_valid_input("Enter new rating (0-10): ", float, lambda r: 0 <= r <= 10,
                                 "Enter a valid rating (0-10).")
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


def generate_website(movies):
    """Generates a static website based on the movie data."""
    # Remove duplicate movies based on title (case-insensitive)
    unique_movies = {}
    for title, info in movies.items():
        normalized_title = title.lower()
        if normalized_title not in unique_movies:
            unique_movies[normalized_title] = info

    # Load the HTML template file
    with open("static/index_template.html", "r") as file:
        template_content = file.read()

    # Create the movie grid HTML with posters
    movie_grid = ""
    for title, info in unique_movies.items():
        poster_url = info.get("poster", "")
        movie_grid += f"<div class='movie-item'><h3>{title}</h3><p>{info['year']} | Rating: {info['rating']}</p><img src='{poster_url}' alt='{title} poster' class='movie-poster'></div>\n"

    # Replace placeholders in the template
    template = Template(template_content)
    rendered_html = template.render(
        TEMPLATE_TITLE="My Movie Collection",
        TEMPLATE_MOVIE_GRID=movie_grid
    )

    # Write the rendered HTML to a file
    with open("index.html", "w") as output_file:
        output_file.write(rendered_html)

    print("Website was generated successfully.")


def main():
    movies = get_movies()
    if movies is None:
        movies = {}

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
        print("9. Generate Website")  # New menu option
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
        elif choice == "9":  # Call the website generation function
            generate_website(movies)
        else:
            print("Invalid choice. Please enter a number from 0 to 9.")


if __name__ == "__main__":
     main()

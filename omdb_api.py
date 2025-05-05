import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
API_KEY = os.getenv("OMDB_API_KEY")

# Check if the API key is loaded correctly
if not API_KEY:
    print("❌ API Key not found in .env file!")
    exit(1)  # Exit if the key is missing

def get_movie_data(title):
    """
    Fetches movie data from OMDb API using the movie title.
    Returns a dictionary with title, year, rating, and poster URL.
    """
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            return {
                "title": data["Title"],
                "year": int(data["Year"]),
                "rating": float(data["imdbRating"]) if data["imdbRating"] != "N/A" else 0,
                "poster": data["Poster"]
            }
        else:
            print(f"❌ Movie not found: {data.get('Error')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"⚠️ API request failed: {e}")
        return None

# ✅ TEST
if __name__ == "__main__":
    movie_title = input("Enter a movie title: ")
    result = get_movie_data(movie_title)
    if result:
        print("✅ API Works!")
        print(result)

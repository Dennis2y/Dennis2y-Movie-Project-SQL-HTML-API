import requests
import os
from dotenv import load_dotenv

# Loading variables from .env
load_dotenv()

# Getting the API key from the environment
API_KEY = os.getenv("OMDB_API_KEY")

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

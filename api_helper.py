import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

def get_movie_data(title):
    """Fetch movie data from OMDb API."""
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return {
                'year': int(data['Year']),
                'rating': float(data['imdbRating']) if data['imdbRating'] != 'N/A' else 0,
                'poster_url': data['Poster'] if data['Poster'] != 'N/A' else None
            }
        else:
            print(f"Movie '{title}' not found.")
    else:
        print("Error fetching movie data.")
    return None

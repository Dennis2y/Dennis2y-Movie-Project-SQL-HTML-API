import requests

#  activated OMDb API key
API_KEY = "de2d5522-5af4-4d95-8acb-68eac2a0cb07"

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

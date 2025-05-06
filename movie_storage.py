from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Movie  # Importing the Movie model from database.py

# Setting up the engine and session
DATABASE_URL = "sqlite:///movies.db"  # Database path
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_movie(title, year, rating, poster):
    """Adds a movie to the database."""
    new_movie = Movie(title=title, year=year, rating=rating, poster=poster)
    session.add(new_movie)
    session.commit()
    print(f"Movie '{title}' added to the database.")

def get_movies():
    """Fetches all movies from the database."""
    movies = {}
    for movie in session.query(Movie).all():
        movies[movie.title] = {"year": movie.year, "rating": movie.rating, "poster": movie.poster}
    return movies

def delete_movie(title):
    """Deletes a movie from the database."""
    movie = session.query(Movie).filter(Movie.title == title).first()
    if movie:
        session.delete(movie)
        session.commit()
        print(f"Movie '{title}' deleted from the database.")
    else:
        print(f"Movie '{title}' not found.")

def update_movie(title, rating):
    """Updates the rating of an existing movie."""
    movie = session.query(Movie).filter(Movie.title == title).first()
    if movie:
        movie.rating = rating
        session.commit()
        print(f"Movie '{title}' updated.")
    else:
        print(f"Movie '{title}' not found.")

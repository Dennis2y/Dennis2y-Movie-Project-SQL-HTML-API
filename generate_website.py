from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
engine = create_engine('sqlite:///movies.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Movie(Base):
    __tablename__ = 'movies'
    title = Column(String, primary_key=True)
    year = Column(Integer)
    rating = Column(Float)
    poster = Column(String)  # <- Add poster column

# Create the updated table
Base.metadata.drop_all(engine)  # Clear old structure
Base.metadata.create_all(engine)

def get_movies():
    movies = session.query(Movie).all()
    return {movie.title: {
        "year": movie.year,
        "rating": movie.rating,
        "poster": movie.poster
    } for movie in movies}

def add_movie(title, year, rating, poster_url):
    movie = Movie(title=title, year=year, rating=rating, poster=poster_url)
    session.add(movie)
    session.commit()

def delete_movie(title):
    movie = session.query(Movie).filter_by(title=title).first()
    if movie:
        session.delete(movie)
        session.commit()

def update_movie(title, rating):
    movie = session.query(Movie).filter_by(title=title).first()
    if movie:
        movie.rating = rating
        session.commit()

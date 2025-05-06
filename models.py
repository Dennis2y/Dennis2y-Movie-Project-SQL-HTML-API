from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize SQLAlchemy for database handling

class Movie(db.Model):  # Movie table in the database
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each movie
    title = db.Column(db.String(100), nullable=False, unique=True)  # Movie title (must be unique)
    year = db.Column(db.String(4), nullable=False)  # Release year (4 characters)
    plot = db.Column(db.String(500))  # Plot summary of the movie
    poster_url = db.Column(db.String(200))  # URL of the movie's poster
    imdb_id = db.Column(db.String(20), nullable=False, unique=True)  # Unique IMDb ID for the movie

    def __repr__(self):
        return f"<Movie {self.title}>"  # String representation of the movie (for debugging)

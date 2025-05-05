import sqlite3

def connect_db():
    """Connects to the SQLite database."""
    return sqlite3.connect("movies.db")

def create_table():
    """Creates the movie table in the database if it doesn't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        title TEXT PRIMARY KEY,
        year INTEGER,
        rating REAL
    )
    ''')
    conn.commit()
    conn.close()

def add_movie(title, year, rating):
    """Adds a new movie to the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO movies (title, year, rating)
    VALUES (?, ?, ?)
    ''', (title, year, rating))
    conn.commit()
    conn.close()

def delete_movie(title):
    """Deletes a movie from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM movies WHERE title = ?
    ''', (title,))
    conn.commit()
    conn.close()

def update_movie(title, rating):
    """Updates a movie's rating in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE movies SET rating = ? WHERE title = ?
    ''', (rating, title))
    conn.commit()
    conn.close()

def get_movies():
    """Fetches all movies from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT title, year, rating FROM movies')
    movies = {title: {'year': year, 'rating': rating} for title, year, rating in cursor.fetchall()}
    conn.close()
    return movies

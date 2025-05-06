class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to reduce overhead
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'  # SQLite database URI (stored in movies.db)

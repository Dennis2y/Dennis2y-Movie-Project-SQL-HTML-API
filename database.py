from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base  # Updated import
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    rating = Column(Float)
    poster = Column(String)

    def __repr__(self):
        return f"<Movie(title={self.title}, year={self.year}, rating={self.rating})>"

# Database setup
DATABASE_URL = 'sqlite:///movies.db'  # SQLite file location
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Creating all tables in the database (if they don't exist already)
Base.metadata.create_all(engine)

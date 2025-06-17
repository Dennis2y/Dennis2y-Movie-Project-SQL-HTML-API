# 🎬 Movie Project - SQL + HTML + API

A beginner-friendly Python project that allows users to manage a movie collection using a SQLite database. It fetches movie data from the OMDb API and generates a static HTML website with movie posters.

---

## 📦 Features

- 🎥 Add movies by title (fetches year, rating, and poster from OMDb)
- 💾 Store movie data in a SQLite database using SQLAlchemy ORM
- 🌐 Generate a static `index.html` with movie posters and details
- 🔍 Search and display individual movie information
- ⚠️ Handles missing data and OMDb API errors

---

## 🛠️ Technologies Used

- Python 3  
- SQLAlchemy (ORM)  
- SQLite  
- OMDb API  
- HTML (Jinja2-style template)  
- Git + GitHub  

---

## 🚀 How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Dennis2y/Movie-Project-SQL-HTML-API.git
   cd Movie-Project-SQL-HTML-API
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set Up OMDb API Key

Create a .env file in the project root.

Add your API key:

ini
Copy
Edit
OMDB_API_KEY=your_api_key_here
Run the App

bash
Copy
Edit
python app.py
View Website

After adding movies, open index.html in your browser.

📁 Project Structure
bash
Copy
Edit
Movie-Project-SQL-HTML-API/
│
├── .codio/                   # Codio config files
├── .guides/                  # Codio guides (if used)
├── .settings/                # Editor settings (Codio or others)
├── __pycache__/              # Python cache
├── _static/                  # Static assets (if any)
│
├── .gitignore                # Files excluded from Git
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
│
├── app.py                    # Main app logic
├── config.py                 # Configuration file (API key, constants)
├── database.py               # DB session and setup
├── models.py                 # SQLAlchemy models
├── movie_storage.py          # Movie-related DB operations
├── generate_website.py       # HTML generation logic
│
├── index_templates.html      # Jinja2-style HTML template
├── movie_details.html        # Extra movie display page
│
├── movies.db                 # SQLite database
└── movies.json               # (Optional) movie data in JSON
🔐 Notes
Get your free OMDb API key at: https://www.omdbapi.com/apikey.aspx

The .env file is ignored by Git and must be created locally.

🌍 GitHub Pages (Optional Hosting)
You can move the generated index.html to a /docs folder and host it using GitHub Pages:

Go to Repository Settings > Pages

Set source to main branch, /docs folder

Access your site at:
https://dennis2y.github.io/Movie-Project-SQL-HTML-API/

🤝 Contributions
Contributions are welcome!
Feel free to fork the repo, improve features, and create pull requests.

📄 License
This project is open source and free to use for educational purposes.

yaml
Copy
Edit

---

### ✅ Final Step: Push the update to GitHub

If the updated README is saved, run this in your terminal:

```bash
git add README.md
git commit -m "Update README with complete project structure and instructions"
git push

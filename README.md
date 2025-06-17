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

pip install -r requirements.txt
Set Up OMDb API Key



📁 Project Structure

Movie-Project-SQL-HTML-API/
│
├── .codio/      
├── .guides/       
├── .settings/      
├── __pycache__/            
│
├── .gitignore      
├── README.md         
├── requirements.txt     
│
├── app.py         
├── config.py    
├── database.py               
├── models.py          
├── movie_storage.py 
├── generate_website.py 
│
├── index_templates.html     
├── movie_details.html       
│
├── movies.db              
└── movies.json               

🔐 Notes
Got my free OMDb API key at: https://www.omdbapi.com/apikey.aspx

The .env file is ignored by Git and must be created locally.

🌍 GitHub Pages (Optional Hosting)
I  moved the generated index.html to a /docs folder and host it using GitHub Pages:
 Repository Settings > Pages


Set source to main branch, /docs folder:

🤝 Contributions
Contributions are welcome!
Feel free to fork the repo, improve features, and create pull requests.

📄 License
This project is open source and free to use for educational purposes.




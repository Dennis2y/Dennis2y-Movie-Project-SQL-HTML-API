from jinja2 import Template
import movie_storage

def generate_website():
    """Generates an HTML file from the movie data."""
    movies = movie_storage.get_movies()
    with open("index_template.html", "r") as template_file:
        template_content = template_file.read()
        template = Template(template_content)
        html_content = template.render(movies=movies)
    
    with open("index.html", "w") as output_file:
        output_file.write(html_content)
    print("Website generated successfully! Check index.html.")

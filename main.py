from flask import Flask, render_template
import requests
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=34b3fbd4dbabd957d6d90c188a2273ef")
    movies = response.json()
    ids = []
    titles = []
    posters = []
    for i in range(8):
        randomNumber = random.randint(0, 19)
        while movies['results'][randomNumber]['id'] in ids:
            randomNumber = random.randint(0, 19)
        ids.append(movies['results'][randomNumber]['id'])
        titles.append(movies['results'][randomNumber]['title'])
        posters.append(movies['results'][randomNumber]['poster_path'])
    return render_template("index.html", ids = ids, titles = titles, posters = posters)


if __name__ == '__main__':
    app.run(debug=True)

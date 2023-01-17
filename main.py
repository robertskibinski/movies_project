from flask import Flask, render_template, request

import client

app = Flask(__name__)


@app.route('/')
def homepage():
    lists = ["popular", "top_rated", "upcoming", "now_playing"]
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in lists:
        selected_list = "popular"
    movies = client.get_movies(list_type=selected_list)

    return render_template("homepage.html", movies=movies, current_list=selected_list)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = client.get_movie(movie_id)
    return render_template("movie_details.html", movie=details)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size="w780"):
        return client.get_poster_url(path, size)

    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)

import requests
import random

from movie import Movie


def get_movies():
    response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=34b3fbd4dbabd957d6d90c188a2273ef")
    json_response = response.json()
    movies = []
    ids = []
    for i in range(8):
        randomNumber = random.randint(0, 19)
        while randomNumber in ids:
            randomNumber = random.randint(0, 19)
        ids.append(randomNumber)
        movies.append(Movie(json_response['results'][randomNumber]['id'],
                            json_response['results'][randomNumber]['title'],
                            json_response['results'][randomNumber]['poster_path']))
    return movies


def get_poster_url(path, size):
    return "https://image.tmdb.org/t/p/" + size + path
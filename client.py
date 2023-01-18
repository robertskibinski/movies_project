import requests
import random

from movie import Movie
from cast import Cast


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


def get_movies(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}?api_key=34b3fbd4dbabd957d6d90c188a2273ef"
    response = requests.get(endpoint)
    response.raise_for_status()
    json_response = response.json()
    movies = []
    ids = []
    for i in range(8):
        randomNumber = random.randint(0, 19)
        while randomNumber in ids:
            randomNumber = random.randint(0, 19)
        ids.append(randomNumber)
        data = json_response['results'][randomNumber]
        movie = Movie(id=data["id"],title=data["title"], poster=data["poster_path"])
        movies.append(movie)
        # movies.append(Movie(json_response['results'][randomNumber]['id'],
        #                     json_response['results'][randomNumber]['title'],
        #                     json_response['results'][randomNumber]['poster_path']))
    return movies


def get_poster_url(path, size):
    return "https://image.tmdb.org/t/p/" + size + path


def get_movie(id):
    response = requests.get("https://api.themoviedb.org/3/movie/" + id + "?api_key=34b3fbd4dbabd957d6d90c188a2273ef")
    json_response = response.json()
    genres = [entry["name"] for entry in json_response["genres"]]
    movie = Movie(
        id=json_response["id"],
        title=json_response["title"],
        poster=json_response["backdrop_path"],
        overview=json_response["overview"],
        genere=genres,
        budget=json_response["budget"],
        cast=get_cast(id)
    )
    return movie


def get_cast(id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/" + id + "/credits?api_key=34b3fbd4dbabd957d6d90c188a2273ef")
    json_response = response.json()
    cast = json_response["cast"]
    cast_with_profile_path = list(filter(lambda cast: cast["profile_path"] is not None, cast))
    casts = []
    for entry in cast_with_profile_path[:4]:
        cast = Cast(id=entry["id"],name=entry["name"], profile=entry["profile_path"])
        casts.append(cast)
    return casts

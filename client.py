import requests
import random

from movie import Movie
from cast import Cast



def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer "
    }
    response = requests.get(endpoint, headers=headers)
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
        movies.append(Movie(json_response['results'][randomNumber]['id'],
                            json_response['results'][randomNumber]['title'],
                            json_response['results'][randomNumber]['poster_path']))
    return movies


def get_poster_url(path, size):
    return "https://image.tmdb.org/t/p/" + size + path


def get_movie(id):
    response = requests.get("https://api.themoviedb.org/3/movie/" + id + "?api_key=34b3fbd4dbabd957d6d90c188a2273ef")
    json_response = response.json()
    genres = []
    for i in json_response['genres']:
        genres.append(i['name'])
    movie = Movie(json_response['id'],
                  json_response['title'],
                  json_response['backdrop_path'],
                  json_response['overview'],
                  genres,
                  json_response['budget'],
                  get_cast(id))
    return movie


def get_cast(id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/" + id + "/credits?api_key=34b3fbd4dbabd957d6d90c188a2273ef")
    json_response = response.json()
    casts = []
    i = 0
    for j in json_response['cast']:
        if type(json_response['cast'][i]['profile_path'])==str :
            if i <4:
                casts.append(Cast(json_response['cast'][i]['id'],
                                  json_response['cast'][i]['name'],
                                  json_response['cast'][i]['profile_path']))
            else:
                break
            i += 1
    return casts

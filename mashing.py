import requests_with_caching
import json

def get_movies_from_tastedive(movie_name):
    parameters = {"q": movie_name, "type": "movies", "limit": "5"}
    tastedive = requests_with_caching.get("https://tastedive.com/api/similar", params = parameters)
    # print(tastedive["Similar"])
    return tastedive.json()

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")

print(get_movies_from_tastedive("Tony Bennett")) 

def extract_movie_titles(queryResult):
    list = []
    for d in queryResult['Similar']['Results']:
        list.append(d['Name'])
    return list
print(list)

extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))


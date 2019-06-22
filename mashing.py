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

def get_related_titles(list):
    final_list = []
    for title in list:
        for item in extract_movie_titles(get_movies_from_tastedive(title)):
            final_list.append(item)
    print(final_list)               
    
    return_list = []
    for item in final_list:
        if item not in return_list:
            return_list.append(item)
    return return_list
    
get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])

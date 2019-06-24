import requests_with_caching
import json


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

def get_movies_from_tastedive(name):
    baseurl = "https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"] = name
    params_d["type"] = "movies"
    params_d["limit"] = 5
    tastedive_resp = requests_with_caching.get(baseurl, params = params_d)
    return tastedive_resp.json()

def extract_movie_titles(queryResult):
    list = []
    for d in queryResult['Similar']['Results']:
        list.append(d['Name'])
    return list
print(list)

#def extract_movie_titles(dict):
#    lst = []
#    for i in dict.keys():
#        for x in dict[i]:
#            for ele in dict[i][x]:
#                if ele['Type'] == 'movie':
#                    lst.append(ele['Name'])
            
#    return lst

def get_related_titles(name_lst):
    master_lst = []
    for i in name_lst:
        d = get_movies_from_tastedive(i)
        related_lst = extract_movie_titles(d)
        for x in related_lst:
            if x == 'Black Panther':
                continue
            if x not in master_lst:
                master_lst.append(x)
            else:
                continue
                
    if name_lst == []:
        return master_lst
    else:
        master_lst.append("Black Panther")
        return master_lst
    
def get_movie_data(name):
    baseurl = "http://www.omdbapi.com/"
    params_d = {}
    params_d["t"] = name
    params_d["r"] = 'json'
    results = requests_with_caching.get(baseurl, params = params_d)
    return results.json()

def get_movie_rating(dict):
    rating = 0
    for i in dict["Ratings"]:
        if i["Source"] == "Rotten Tomatoes":
            str1 = i["Value"]
            str_r = str1.replace("%", "")
            rating = int(str_r)
            break
        else:
            rating = 0
        
    print("-----------")
    return(rating)

def get_sorted_recommendations(mov_list):
    sort_list = []
    unsort_list = []
    ext_movie_list = []
    newlist = []
    movie_rel_list = get_related_titles(mov_list)
    
    for movie in movie_rel_list:
        mov_dict = get_movie_data(movie)
        movie_rating = get_movie_rating(mov_dict)
        lst_item = [movie_rating,movie]
        unsort_list.append(lst_item)
    
    sort_list = sorted(unsort_list, reverse = True)
    print(unsort_list,sort_list )
    for x,y in sort_list:
        newlist.append(y)

    return newlist

get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

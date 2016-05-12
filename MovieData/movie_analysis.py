import json
import operator
import time
from urllib.request import urlopen

api_key = "API_KEY"


def parse_json(url):
    """Parse Json on the given url and return json object"""
    response = urlopen(url).read().decode('utf8')
    return json.loads(response)


# Best (Worst) 10 Movies
# Criterion: Vote Count 300+


def print_best_worst(json_obj):
    count = 1
    for mov in json_obj['results']:
        if count == 11:
            break
        print(mov['original_title'])
        count += 1


def build_bw_url(best, pg=1, genre=0):
    return "http://api.themoviedb.org/3/discover/movie?page=" + str(pg) + \
           (("&with_genres=" + str(genre)) if genre is not 0 else "") + \
           "&sort_by=vote_average." + ("de" if best else "a") + \
           "sc&vote_count.gte=300&api_key=" + api_key


print("------------")
print("Best 10 Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(True)))

print("------------")
print("Worst 10 Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(False)))


# Best (Worst) 100 Movies
# Histogram based on Release Year and Production Company


def print_year_company(pairs):
    for pair in sorted(pairs.items(), reverse=True, key=operator.itemgetter(1)):
        print(pair[0], pair[1])


# Based on Release Year

best_years = {}
worst_years = {}
best_ids = []
worst_ids = []


def get_years_ids(best, years, ids):
    for page in range(1, 6):
        json_object = parse_json(build_bw_url(best, page))
        for movie in json_object['results']:
            ids.append(movie['id'])
            year = str(movie['release_date'])[0:4]
            if year in years:
                years[year] += 1
            else:
                years[year] = 1


get_years_ids(True, best_years, best_ids)
get_years_ids(False, worst_years, worst_ids)

print("------------")
print("Best Years")
print("------------")
print_year_company(best_years)

print("------------")
print("Worst Years")
print("------------")
print_year_company(worst_years)

# Based on Production Company
best_companies = {}
worst_companies = {}


def add_partial_list(partial, companies):
    for mov in partial:
        movie_url = "http://api.themoviedb.org/3/movie/" + str(mov) + "?api_key=" + api_key
        movie_json = parse_json(movie_url)
        company = movie_json['production_companies'][0]["name"]
        if company in companies:
            companies[company] += 1
        else:
            companies[company] = 1


for n in range(0, 5):
    add_partial_list(best_ids[n * 20:(n + 1) * 20], best_companies)
    time.sleep(10)
    add_partial_list(worst_ids[n * 20:(n + 1) * 20], worst_companies)
    time.sleep(10)

print("------------")
print("Best Companies")
print("------------")
print_year_company(best_companies)

print("------------")
print("Worst Companies")
print("------------")
print_year_company(worst_companies)

# Best (Worst) 10 Horror (Romance) Movies
# Horror Genre ID: 27
# Romance Genre ID: 10749

horror = 27
romance = 10749

print("------------")
print("Best 10 Horror Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(True, 1, horror)))

print("------------")
print("Worst 10 Horror Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(False, 1, horror)))

print("------------")
print("Best 10 Romance Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(True, 1, romance)))

print("------------")
print("Worst 10 Romance Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(False, 1, romance)))

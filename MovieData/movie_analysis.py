import json
import operator
import time
from urllib.request import urlopen

from xlwt import Workbook

api_key = "API_KEY"
wb = Workbook()


def parse_json(url):
    """Parse Json on the given url and return json object"""
    response = urlopen(url).read().decode('utf8')
    return json.loads(response)


def prepare_sheet(sheet_name, col_one, col_two):
    """Initiate new sheet with header ready"""
    sheet = wb.add_sheet(sheet_name)
    sheet.write(0, 0, col_one)
    sheet.write(0, 1, col_two)
    return sheet


# Best (Worst) 10 Movies
# Criterion: Vote Count 300+


def print_best_worst(json_obj, sheet):
    """Print out (Export to Excel) Best/Worst 10"""
    count = 1
    for mov in json_obj['results']:
        if count == 11:
            break
        print(mov['original_title'])
        sheet.write(count, 0, count)
        sheet.write(count, 1, mov['original_title'])
        count += 1


def build_bw_url(best, pg=1, genre=0):
    """Build api query url"""
    return "http://api.themoviedb.org/3/discover/movie?page=" + str(pg) + \
           (("&with_genres=" + str(genre)) if genre is not 0 else "") + \
           "&sort_by=vote_average." + ("de" if best else "a") + \
           "sc&vote_count.gte=300&api_key=" + api_key


print("------------")
print("Best 10 Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(True)), prepare_sheet('Best10', "No.", "Best 10 Movies"))

print("------------")
print("Worst 10 Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(False)), prepare_sheet('Worst10', "No.", "Worst 10 Movies"))


# Best (Worst) 100 Movies
# Histogram based on Release Year and Production Company


def print_year_company(pairs, sheet):
    """Print out (Export to Excel) Count Info based on criteria"""
    count = 1
    for pair in sorted(pairs.items(), reverse=True, key=operator.itemgetter(1)):
        print(pair[0], pair[1])
        sheet.write(count, 0, pair[0])
        sheet.write(count, 1, pair[1])
        count += 1


# Based on Release Year

best_years = {}
worst_years = {}
best_ids = []
worst_ids = []


def get_years_ids(best, years, ids):
    """Save years and ids to the according dict and list"""
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
print_year_company(best_years, prepare_sheet('BestYears', "Year", "Count"))

print("------------")
print("Worst Years")
print("------------")
print_year_company(worst_years, prepare_sheet('WorstYears', "Year", "Count"))

# Based on Production Company
best_companies = {}
worst_companies = {}


def add_partial_list(partial, companies):
    """Query api based on id in a list"""
    for mov in partial:
        movie_url = "http://api.themoviedb.org/3/movie/" + str(mov) + "?api_key=" + api_key
        movie_json = parse_json(movie_url)
        company = movie_json['production_companies'][0]["name"]
        if company in companies:
            companies[company] += 1
        else:
            companies[company] = 1


# Need to do the query with intervals so as to prevent HTTP Error 429
# 10 seconds every 20 queries
for n in range(0, 5):
    add_partial_list(best_ids[n * 20:(n + 1) * 20], best_companies)
    time.sleep(10)
    add_partial_list(worst_ids[n * 20:(n + 1) * 20], worst_companies)
    time.sleep(10)

print("------------")
print("Best Companies")
print("------------")
print_year_company(best_companies, prepare_sheet('BestCompanies', "Company", "Count"))

print("------------")
print("Worst Companies")
print("------------")
print_year_company(worst_companies, prepare_sheet('WorstCompanies', "Company", "Count"))

# Best (Worst) 10 Horror (Romance) Movies
# Horror Genre ID: 27
# Romance Genre ID: 10749

horror = 27
romance = 10749

print("------------")
print("Best 10 Horror Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(True, 1, horror)), prepare_sheet('BestHorror', "No.", "Best 10 Horror"))

print("------------")
print("Worst 10 Horror Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(False, 1, horror)), prepare_sheet('WorstHorror', "No.", "Worst 10 Horror"))

print("------------")
print("Best 10 Romance Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(True, 1, romance)), prepare_sheet('BestRomance', "No.", "Best 10 Romance"))

print("------------")
print("Worst 10 Romance Movies")
print("------------")
print_best_worst(parse_json(build_bw_url(False, 1, romance)), prepare_sheet('WorstRomance', "No.", "Worst 10 Romance"))

wb.save('data.xls')

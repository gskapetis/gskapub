import requests
import json
import os
import sys
import datetime

my_countries_list = ["Greece", "Spain", "Uk", "Italy", "Netherlands","Usa","Turkey","France","Sweden","Germany", "Portugal", "All"]
my_colors_list = ["blue", "yellow", "indigo", "lime", "orange", "magenta", "red", "navy", "cyan", "green", "tomato","black"]
# my_obsolete_path = "/mnt/c/Users/user/PycharmProjects/GeoSkapRepo/MyProjects/CoronaVirus/"
my_obsolete_path = ""

def return_virus_results(mycountry, mydate):
    '''
    Function which resturns a json dictionary with the results of specific country on specific date
    :param mycountry: conutry
    :param mydate: date
    :return: corona virus result dictionary
    '''
    url = "https://covid-193.p.rapidapi.com/history"
    querystring = {"day": mydate, "country": mycountry}
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "811d0d04ebmshe3a0af52ecc2cc7p137404jsn0d808175d0f3"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    mydata = response.json()
    current_date = mydata["response"][0]["day"]
    country = mydata["response"][0]["country"]
    total_cases = mydata["response"][0]["cases"]["total"]
    total_recovered = mydata["response"][0]["cases"]["recovered"]
    total_deaths = mydata["response"][0]["deaths"]["total"]
    myentry = {"date": current_date,
               "country": country,
               "total_cases": total_cases,
               "total_deaths": total_deaths,
               "total_recovered": total_recovered
               }
    # print("Corona virus results for country {} on {}: ".format(mycountry, mydate))
    # print(myentry)
    return (myentry)


def add_info_to_file(myfile, myentry, per_country=True):
    '''
    :param myfile: file where we want to add info
    :param myentry: the info that we want to add to file
    :param per_country: per_country=True is used for creating file per country and per_country=False is used
                        for estimation of the total_values file.
    :return: nothing
    '''

    # Create directory countries (in case it does not exist) in order to store all the data for each country
    path = my_obsolete_path + "countries"
    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.exists(myfile) == False:
        with open(myfile, 'w+') as f:
            print("File {} is empty and is going to be created and filled accordingly".format(myfile))
            data = []
    elif os.path.getsize(myfile) == 0:
        with open(myfile, 'w+') as f:
            print("File {} is empty and is going to be created and filled accordingly".format(myfile))
            data = []
    else:
        with open(myfile, 'r') as f:
            data = json.load(f)

    if myentry["date"] not in str(data):
        print(">>> Adding entry {} to file {}".format(myentry, myfile))
        data.append(myentry)
    elif myentry["date"] in str(data) and per_country == False:
        print(">>> Adding entry {} to file {}".format(myentry, myfile))
        data.append(myentry)
    else:
        print("Results of date {} exists already in {}".format(myentry["date"], myfile))
    f.close()

    with open(myfile, 'w+') as f:
        json.dump(data, f, indent=4)
    f.close()

def load_json_from_file (filename):
    if os.path.exists(filename) == False:
        sys.exit("Error in parsing file {}. File does not exist!".format(filename))
    with open(filename, 'r') as f:
        data = json.load(f)
    return(data)



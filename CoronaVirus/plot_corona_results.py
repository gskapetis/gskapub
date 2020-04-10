######################################################
#
# Author:   George Skapetis (geoskapetis@gmail.com)
#
# Description:
# ############
# Script that creates json files with the corona virus results (<Country>.json) for each
# country inside folder countries.
#
# How to run:
# ###########
# #> python plot_corona_results.py <country> <type_of_case>
#
# Examples:
# #########
# Create 3 graphs (saved as images) for each case for the specific country
# #> python plot_corona_results.py Greece cases
# #> python plot_corona_results.py Greece deaths
# #> python plot_corona_results.py Greece recovered
#
# World Wide Results
# #> python plot_corona_results.py All cases
# #> python plot_corona_results.py All deaths
# #> python plot_corona_results.py All recovered
#
# Create 1 graph (saved as image) with all the countries results for the specific type of case in same graph (for
# comparison)
# #> plot_corona_results.py total cases
# #> plot_corona_results.py total deaths
# #> plot_corona_results.py total recovered
#
#


import matplotlib.pyplot as plt
from coronautils import *
import sys
import datetime


type_of_instance = ""
country_selection = ""
if len(sys.argv) <= 2:
    sys.exit("Please select a country and an instance between cases, deaths and recovered. \nExample: # python "
             "plot_corona_results.py cases")

if sys.argv[2].upper() == "CASES":
    type_of_instance = "total_cases"
elif sys.argv[2].upper() == "DEATHS":
    type_of_instance = "total_deaths"
elif sys.argv[2].upper() == "RECOVERED":
    type_of_instance = "total_recovered"
else:
    sys.exit("Print select between cases, deaths and recovered")


country_selection = sys.argv[1]

path = my_obsolete_path + "results"
if not os.path.exists(path):
    os.makedirs(path)


if country_selection.upper() != "TOTAL":
    country_selection = sys.argv[1].capitalize()
    myfile_list = my_obsolete_path + "countries/" + country_selection + ".json"
    print(myfile_list)
    cases = []
    dates = []
    temp_data = load_json_from_file(myfile_list)
    for entry in temp_data:
        cases.append(entry[type_of_instance])
        dates.append(entry["date"])
    my_countries_list
    plt.figure(figsize=(10, 6))
    plt.plot(dates, cases, color=my_colors_list[my_countries_list.index(country_selection)], linewidth=2, label=country_selection)
    plt.xlabel('Date')
    plt.xticks(dates, rotation='vertical')
    plt.ylabel('Total-Cases')
    plt.title(type_of_instance + ' during last days')
    plt.legend()
    # plt.show()
    figure_filename = my_obsolete_path + "results/" + sys.argv[1].capitalize() + "_" + type_of_instance + ".png"
    plt.savefig(figure_filename)

if country_selection.upper() == "TOTAL":
    myfile_list = []
    for name in my_countries_list[:-1]:
        myfile_list.append(my_obsolete_path + "countries/" + name + ".json")

    print(myfile_list)
    cases = []
    dates = []
    for file in myfile_list:
        temp_data = load_json_from_file(file)
        cases_per_country = []
        dates_per_country = []
        for entry in temp_data:
            cases_per_country.append(entry[type_of_instance])
            dates_per_country.append(entry["date"])
        cases.append(cases_per_country)
        dates.append(dates_per_country)
    # print(cases)

    dictionary_of_countries = {}
    i = 0
    for mycountry in my_countries_list[:-1]:
        dictionary_of_countries[mycountry] = [my_colors_list[i], dates[i], cases[i]]
        i = i + 1

    # print(dictionary_of_countries)

    plt.figure(figsize=(10, 6))
    for key in dictionary_of_countries.keys():
        # print("Key: {}".format(key))
        # print("Color: {}".format(dictionary_of_countries[key][0]))
        # print("Dates: {}".format(dictionary_of_countries[key][1]))
        # print("Values: {}".format(dictionary_of_countries[key][2]))
        plt.plot(dictionary_of_countries[key][1], dictionary_of_countries[key][2], color=dictionary_of_countries[key][0], linewidth=2, label=key)

    plt.xlabel('Date')
    plt.xticks(dictionary_of_countries[key][1], rotation='vertical')
    plt.ylabel('Total-Cases')
    plt.title(type_of_instance + ' during last days')
    plt.legend()
    # plt.show()
    figure_filename = my_obsolete_path + "results/World_" + type_of_instance + ".png"
    plt.savefig(figure_filename)


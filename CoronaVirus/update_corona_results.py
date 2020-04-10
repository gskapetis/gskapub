######################################################
#
# Author:   George Skapetis (geoskapetis@gmail.com)
#
# Description:
# ############
# Script that creates json files with the corona virus results (<Country>.json) for each country inside
# folder countries.
#
# How to run:
# ###########
# #> python update_corona_results.py Greece 2020-03-21
# #> python update_corona_results.py All 2020-03-21
#
# Add results in Italy.json for the current date of script's execution
# #> python update_corona_results.py Italy
#
#
# Available countries:
# ####################
# Greece, Spain, Uk, Italy, Netherlands, Usa, Turkey, France, Sweden, Germany, All (World Wide results)
#
# Sources:
# ########
# https://documenter.getpostman.com/view/4074074/SzS7Pkup?version=latest#63cbe0bc-5664-48da-96f5-e750e8cac566
# Various requests using the API:
# https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?order=total_deaths
# https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?order=total_recovered&how=asc
# https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?limit=8&page=1&search=ke&order=total_cases&how=asc
# https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?search=Greece
#
#

import sys
import datetime
from coronautils import *

if len(sys.argv) == 1:
    mycountry = "All"
    mydate = datetime.date.today()
elif len(sys.argv) == 2:
    mycountry = sys.argv[1].capitalize()
    mydate = datetime.date.today()
elif len(sys.argv) == 3:
    mycountry = sys.argv[1].capitalize()
    mydate = sys.argv[2]
else:
    sys.exit("Error1! Exiting ...")

if mycountry.upper() == "WORLD":
    mycountry = "All"

if mycountry not in my_countries_list:
    sys.exit("The country {} does not belongs to the existing countries list. Exiting ...".format(mycountry))

myfile = my_obsolete_path + "countries/" + mycountry + ".json"
mynewentry = return_virus_results(mycountry, mydate)
add_info_to_file(myfile,mynewentry)
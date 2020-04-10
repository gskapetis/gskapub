import sys
import datetime
from coronautils import *
import os

total_values_file = my_obsolete_path + "results/total_values.json"
mydate = datetime.date.today()

if os.path.exists(total_values_file) != False:
    print(">>>Removing old file {}".format(total_values_file))
    os.remove(total_values_file)

print(">>> Creating new file with latest total values...")
for country in my_countries_list:
    myresult = return_virus_results(country, mydate)
    add_info_to_file(total_values_file, myresult, False)
print(">>> File created!")
"""
This file contains the functions that will call instances of the get_data classes
"""

from Modules.fields import *
from Modules.get_data import *
from Modules.wb_indicators import *
import datetime
import csv

"""
def set_args() -> tuple:
    the_date = datetime.datetime(2019, 1, 1), datetime.datetime(2018, 1, 1)
    the_indicator = Africa_development_indicators.gdp_per_capita_annual_growth
    the_country = Country.kenya

    return the_date, the_indicator, the_country
"""

# date format: from x year to y year
final_dates = datetime.datetime(2019, 1, 1), datetime.datetime(2014, 1, 1)

# multiple indicators should be a dictionary
final_indicators = []

# multiple countries should be in a list, each element is the country's code
final_countries = [Country.chad, Country.zimbabwe, Country.south_africa]


# appends lis of indicators from the gui
def gen_final_indicators(kpi):
    final_indicators.append(kpi)
    print("Final indicators: ", final_indicators)


def gen_final_date():
    pass


def gen_final_countries():
    pass


def get_data_result():
    complete_data = []
    i = 0
    while i < len(final_indicators):
        country_result_list = Get_wb_data(final_indicators[i], final_countries,
                                          final_dates)  # create an instance of get Get_wb_data

        result_data = country_result_list.get_the_data
        complete_data += result_data
        i += 1

    print(complete_data)
    return complete_data


def create_csv():
    # generate fields for the csv file
    field_names = list(create_fields())

    with open('bccm_file.csv', 'w', newline='') as csvfile:
        bccmwriter = csv.DictWriter(csvfile, fieldnames=field_names)
        bccmwriter.writeheader()
        data_list = get_data_result()  # data row is a list of dictionaries that contains yearly data

        j = 0
        while j < len(data_list):
            bccmwriter.writerow(data_list[j])
            j += 1

        print(f"csv generated")



"""
def get_data_result():
    complete_data = [None]*100
    i = 0
    while i < len(indicators):
        country_result_list = Get_wb_data(indicators[i], countries, dates)      # create an instance of get Get_wb_data

        result_data = country_result_list.get_the_data
        complete_data += result_data
        i += 1
    country_result_list.create_csv()
    print(complete_data)
    return complete_data        # complete_data is a list of dictionaries
"""

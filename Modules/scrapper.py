"""
This file contains the functions that will call instances of the get_data classes
"""

from Modules.get_data import *
from Modules.wb_indicators import *
import datetime

"""
def set_args() -> tuple:
    the_date = datetime.datetime(2019, 1, 1), datetime.datetime(2018, 1, 1)
    the_indicator = Africa_development_indicators.gdp_per_capita_annual_growth
    the_country = Country.kenya

    return the_date, the_indicator, the_country
"""

dates = datetime.datetime(2019, 1, 1), datetime.datetime(2014, 1, 1)
# multiple indicators should be a dictionary
indicators = Africa_development_indicators.current_account_balance

# multiple countries should be in a list, each element is the country's code
countries = [Country.chad, Country.zimbabwe, Country.south_africa]


# generating an iterable for countries
# nations = iter(countries)


def get_data_result():
    country_result_list = Get_wb_data(indicators, countries, dates)  # create an instance of get Get_wb_data
    result_data = country_result_list.get_the_data
    country_result_list.create_csv()

    return result_data

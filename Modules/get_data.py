"""
This file contains the main classes for accessing data from the various API's and modules
"""
from Modules.fields import *
import wbdata as wb
import datetime
from Modules.wb_indicators import *


class Get_wb_data:
    def __init__(self, the_indicator, the_nation, the_date):
        self.the_indicators = the_indicator
        self.the_countries = the_nation
        self.the_dates = the_date

    @property
    def get_the_data(self) -> dict:
        # generate fields for the csv file
        field_names = list(create_fields())

        # using the wbdata api to access the data
        the_data = wb.get_data(self.the_indicators, self.the_countries, self.the_dates)

        data_dict = [None]*len(the_data)        # a list of data dictionaries, holds whole data set

        i = 0
        while i < len(the_data):                    # year_data is a dictionary for year's stats, the_data is a list of dicts
            year_dict = {}                          # holds yearly data
            for key in the_data[i]:
                if key in field_names:               # if the field exists in the list of desired fields
                    index_value = the_data[i][key]  # returns a values for the year's data
                    check_index_value = isinstance(index_value, dict)
                    if check_index_value:
                        if index_value['value']:
                            year_dict.update({key: index_value['value']})
                    else:
                        year_dict.update({key: index_value})
            data_dict[i] = year_dict
            i += 1
        return data_dict








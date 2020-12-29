"""
This file contains the main classes for accessing data from the various API's and modules
"""
from Modules.fields import *
import wbdata as wb
import csv
import datetime
from Modules.wb_indicators import *


class Get_wb_data:
    def __init__(self, indicators, countries, dates):
        self.the_indicator = indicators
        self.the_countries = countries
        self.the_date = dates

    # generated fields for the csv file
    global fieldnames
    fieldnames = list(create_fields())

    @property
    def get_the_data(self) -> dict:
        # using the wbdata api to access the data
        the_data = wb.get_data(self.the_indicator, self.the_countries, self.the_date)

        data_dict = [None]*len(the_data)        # holds whole data set, a list of data dicts

        list_of_field_names = list(fieldnames)

        i = 0
        while i < len(the_data):                    # year_data is a dictionary for year's stats, the_data is a list of dicts
            year_dict = {}                          # holds yearly data
            for key in the_data[i]:
                if key in fieldnames:               # if the field exists in the list of desired fields
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

    def create_csv(self):
        with open('bccm_file.csv', 'w', newline='') as csvfile:
            bccmwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            bccmwriter.writeheader()
            data_list = self.get_the_data  # data row is a list of dictionaries that contains yearly data

            j = 0
            while j < len(data_list):
                bccmwriter.writerow(data_list[j])
                j += 1

            print(f"csv generated")
            """
            # bccm writer works with dictionaries
            bccmwriter.writerow({fieldnames[0]: 'Value', fieldnames[1]: 'Chain'})
            """




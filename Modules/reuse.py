# source
from Modules.get_data import Get_wb_data

'''
if len(self.the_indicator) == 1:
    i = 0
    while i < len(the_data):  # year_data is a dictionary for year's stats, the_data is a list of dicts
        year_dict = {}  # holds yearly data
        for key in the_data[i]:
            if key in fieldnames:  # if the field exists in the list of desired fields
                index_value = the_data[i][key]  # returns a values for the year's data
                check_index_value = isinstance(index_value, dict)
                if check_index_value:
                    if index_value['value']:
                        year_dict.update({key: index_value['value']})
                else:
                    year_dict.update({key: index_value})
        data_dict[i] = year_dict
        i += 1
    print("THE LIST OF DICTIONARIES")
    print(data_dict)
    return data_dict
'''


=======================================
Macroeconomic Data Miner and Analyser
=======================================

.. A comment has two dot before it (unless there is a special command that follows the two dots)

An Introduction
-----------------
The program utilizes various API's and packages to access African socioeconomic data and statistics from trusted sources around the globe. These include the **World Bank**'s *wbdata* and a Python package named *BS4* (Beautiful Soup 4).


wbdata
-------
This is the World Banks API that allows programmers access to a wide range of socioeconomic data points for virtually every nation in the world.
My program is specifically for African nations.

**AN EXAMPLE**

The simplest way to gather data is through using the ``get_data`` function which returns a list of dictionaries which we can then parse.
Here is an example call of ``get_data`` for Kenya's total female population statistics:

====================================================          ===========================================================================================================================================================================================================================================================
Function call:                                                  Returns:
====================================================          ===========================================================================================================================================================================================================================================================
 ``wb_data.get_data("SP.POP.TOTL.FE.IN", "KEN")``               ``[{'indicator': {'id': 'NY.GDP.PCAP.KD.ZG', 'value': 'GDP per capita growth (annual %)'}, 'country': {'id': 'KE', 'value': 'Kenya'}, 'countryiso3code': 'KEN', 'date': '2019', 'value': 2.99893048296214, 'unit': '', 'obs_status': '', 'decimal': 1}]``
====================================================          ===========================================================================================================================================================================================================================================================


This list of dictionaries can now be parsed in order to use the data however we choose.

Later, we would like to make a csv file comprising of this data every time a user utilizes this program.


**DATES**

The ``wb_data.get_data`` function has a date argument which allows for access to data from specific time periods:

    ``the_date = datetime.datetime(2019, 1, 1), datetime.datetime(2014, 1, 1)``
    ``the_indicator = africa_development_indicators.gdp_per_capita_annual_growth``
    ``the_country = country.kenya``
    ``the_data = wb.get_data(the_indicator, the_country, the_date)``

Each item in the list represents data from a single year and is a dictionary of dictionaries
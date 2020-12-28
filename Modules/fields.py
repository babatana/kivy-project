"""
    creating our own field since not all the fields from wbdata are useful to us
"""


def create_fields() -> tuple:
    field1 = 'country'
    field2 = 'countryiso3code'
    field3 = 'indicator'
    field4 = 'date'
    field5 = 'value'

    return field1, field2, field3, field4, field5

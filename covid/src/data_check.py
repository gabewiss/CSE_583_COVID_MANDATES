"""This module is used to checks the reponse request for
   the data sources and found at:

   https://data.cdc.gov/api/views/9mfq-cb36
   /rows.csv?accessType=DOWNLOAD

   and

   https://healthdata.gov/node/
   3281076/download
   ________________________________________
   Author: Gabriel Wisswaesser
   """

import pandas as pd
from urllib import request


def count_data_vet_import():
    """

    Import of state count data from cdc.gov
    Uses urlib request to determine if there are any access issues to
    data repos AND

    Args: none
    Returns: state_count a pandas df OR a string notifying user
             URL is not working

    """
    # store URL request code in resp1
    resp1 = request.urlopen('https://data.cdc.gov/api/views/9mfq-cb36/'
                            'rows.csv?accessType=DOWNLOAD')
    # if resp1.code is 200, then the URL is open for business
    # otherwise cursory URl issue is printed
    if resp1.code == 200:
        state_count = pd.read_csv('https://data.cdc.gov/api/views/9mfq-cb36'
                                  '/rows.csv?accessType=DOWNLOAD')
        return state_count
    else:
        return print('URL issues. Check data source availability')


def mandate_data_vet_import():
    """
    Import of state count data from cdc.gov
    Uses urlib request to determine if there are any access issues to
    data repos AND

    Args: none
    Returns: state_count a pandas df OR a string notifying user
             URL is not working
    """

    # store URL request code in resp1
    resp1 = request.urlopen('https://healthdata.gov/node/3281076/download')

    # if resp1.code is 200, then the URL is open for business
    # otherwise cursory URl issue is printed
    if resp1.code == 200:
        state_mandate = pd.read_csv('https://healthdata.gov/node/'
                                    '3281076/download')
        return state_mandate
    else:
        return print('URL issues. check data source avalability')

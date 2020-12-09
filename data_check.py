"""This module is used to checks the reponse request for
   the data sources and found at:

   https://raw.githubusercontent.com/nytimes/
   covid-19-data/master/us-states.csvv

   and

   https://healthdata.gov/sites/default/files/
   state_policy_updates_20201202_0721.csv
   ________________________________________
   Author: Gabriel Wisswaesser
   """

from urllib import request


def repo_check():

    """Uses urlib request to determine if there are any access issues to
    data repos

    HTTP Status Codes: 200: OK, 400: Bad Request, 403: Forbidden,
                       404: Not Found

    Args: none
    Returns: resp1.code and resp2.code status codes"""

    resp1 = request.urlopen('https://raw.githubusercontent.com/nytimes/covid-'
                            '19-data/master/us-states.csv')
    resp2 = request.urlopen('https://healthdata.gov/sites/default/files/'
                            'state_policy_updates_20201202_0721.csv')

    return resp1.code, resp2.code

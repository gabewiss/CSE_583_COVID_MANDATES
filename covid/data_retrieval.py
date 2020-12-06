"""data_retrieval is a function that pulls fresh data for covid.py.

data_retrieval

Exceptions -- ParserError is a check on the csv files (line 16)

Args: no arguments

"""

import pandas as pd


def data_retrieval():

    """This is a function to pull fresh csv data from two servers"""

    """importing newest data from nytimes repo and healthdata.gov"""
    states = pd.read_csv('https://raw.githubusercontent'  # noqa: F841
                         '.com/nytimes/covid-19-data/master/us-states.csv')
    mandates = pd.read_csv('https://healthdata.gov'  # noqa: F841
                           '/sites/default/files/'
                           'state_policy_updates_20201202_0721.csv')

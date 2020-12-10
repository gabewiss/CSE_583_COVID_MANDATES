"""
This module is used to process the case count dataset everytime
it is downloaded from the github site
"""

import pandas as pd


def count_processing(case_df, pop_df):
    '''
    Function used to process the case count dataset downloaded from github.

    Argument:
    case_count_df -- The original dataset

    Return:
    case_count_monthly --
    The result dataframe has the monthly case count and death count
    for each state per hundred thousand of state population size
    '''
    try:
        case_df = case_df[['state', 'submission_date', 'new_case',
                          'new_death']]
    except KeyError:
        print("The dataset is from different data source")
    case_df = pd.merge(case_df, pop_df)
    case_df['new_case'] = case_df['new_case'] / \
        case_df['population'] * 100000
    case_df['new_death'] = case_df['new_death'] / \
        case_df['population'] * 100000
    case_df = case_df.rename(columns={'submission_date': 'date'})
    case_df['date'] = pd.to_datetime(case_df['date'])
    case_df['month'] = pd.to_datetime(case_df['date']).dt.month
    case_count_monthly = case_df.groupby(['state',
                                          'month']).sum().reset_index()
    return case_count_monthly

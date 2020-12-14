"""
This module is used to process the case count dataset everytime
it is downloaded from the github site

Function --
count_processing: Process the case count dataset into the format we
                  we want.
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
    # try:
    #     case_df = case_df[['state', 'submission_date', 'new_case',
    #                       'new_death']]
    # except KeyError:
    #     print("The dataset is from different data source")
    if 'state' not in case_df.keys():
        raise KeyError("The input dataframe is not from the same source")
    if 'submission_date' not in case_df.keys():
        raise KeyError("The input dataframe is not from the same source")
    if 'new_case' not in case_df.keys():
        raise KeyError("The input dataframe is not from the same source")
    if 'new_death' not in case_df.keys():
        raise KeyError("The input dataframe is not from the same source")
    case_df = case_df[['state', 'submission_date', 'new_case',
                       'new_death']]
    case_count_df = pd.merge(case_df, pop_df,
                             left_on="state",
                             right_on="state_id")
    case_count_df['new_case'] = case_count_df['new_case'] / \
        case_count_df['population'] * 100000
    case_count_df['new_death'] = case_count_df['new_death'] / \
        case_count_df['population'] * 100000
    case_count_df = case_count_df.rename(columns={'submission_date': 'date',
                                                  'state_x': 'state'})
    case_count_df['date'] = pd.to_datetime(case_count_df['date'])
    case_count_df['month'] = pd.to_datetime(case_count_df['date']).dt.month
    case_count_monthly = case_count_df.groupby(['state',
                                                'month']).sum().reset_index()
    return case_count_df, case_count_monthly

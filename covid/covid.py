"""
Function to get tavisci.yml working. Not working yet. Not working yet.
how about now. 4th attempt?
"""
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State
# from jupyter_dash import JupyterDash
import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go


def covid(not_important):
    """
    Function to get tavisci.yml working. Not working yet. Not working yet.
    how about now. 4th attempt?
    """

    not_important1 = not_important
    return not_important1


state_count = pd.read_csv("data/state_case.csv", index_col=False)
# The file for state_mandate is not correct. Double check with Zhaowen
state_mandate = pd.read_csv("data/state_mandate.csv", index_col=False)
states_population = pd.read_csv("data/states_population.csv", index_col=False)


def case_count_processing(case_count_df):
    '''
    Function used to process the case count dataset downloaded from github.

    Argument:
    case_count_df -- The original dataset

    Return:
    case_count_monthly -- Return the selected fields, change the date column
    datatype to match the mandate dataset, add month column, and group the
    dataframe on state and month. The result dataframe has the monthly
    case count and death count for each state per hundred thousand of state
    population size
    '''
    if 'state' not in case_count_df.keys():
        raise IOError("The input dataframe is not from the same source")
    if 'submission_date' not in case_count_df.keys():
        raise IOError("The input dataframe is not from the same source")
    if 'new_case' not in case_count_df.keys():
        raise IOError("The input dataframe is not from the same source")
    if 'new_death' not in case_count_df.keys():
        raise IOError("The input dataframe is not from the same source")
    case_count_df = case_count_df[['state', 'submission_date', 'new_case',
                                   'new_death']]
    case_count_df = pd.merge(case_count_df, states_population)
    case_count_df['new_case'] = case_count_df['new_case'] / \
        case_count_df['population'] * 100000
    case_count_df['new_death'] = case_count_df['new_death'] / \
        case_count_df['population']*100000
    case_count_df = case_count_df.rename(columns={'submission_date': 'date'})
    case_count_df['date'] = pd.to_datetime(case_count_df['date'])
    case_count_df['month'] = pd.to_datetime(case_count_df['date']).dt.month
    case_count_monthly = case_count_df.groupby(['state',
                                                'month']).sum().reset_index()
    return case_count_monthly


def mandate_processing(mandate_df):
    '''
    Function used to process the mandate dataset downloaded from github site.

    Argument:
    mandate_df -- The original mandate dataset

    Return:
    mandate_df -- Five most common mandates announced throughout the states,
    and drop the duplicate rows in the dataframe.
    '''
    # Zhaowen could you please add your processing code over here.
    # The below several lines are what I used to process for the data you've
    # already cleaned. Thank you!

    policy_mandates = ["Shelter in Place",
                       "Food and Drink",
                       "Non-Essential Businesses",
                       "Outdoor and Recreation",
                       "Mandate Face Mask Use By All Individuals In Public"
                       " Facing Businesses",
                       "Mask Requirement",
                       "Mandate Face Mask Use By All Individuals In Public"
                       " Spaces"]

    mandate_columns = mandate_df[["state_id",
                                  "policy_level",
                                  "date",
                                  "policy_type",
                                  "start_stop"]]

    mandate_rows = mandate_columns[(mandate_columns["start_stop"] == "start")
                                   & (mandate_columns["policy_level"] ==
                                   "state")
                                   & (mandate_columns["policy_type"].
                                   isin(policy_mandates))]

    mandate_all = pd.merge(mandate_rows, states_population)
    mandate_all.drop(["policy_level"], axis=1)
    mandate_all.loc[mandate_all["policy_type"]
                    .str.contains("Mask"), "policy_type"] = "Mask Wearing"

    if 'state' not in mandate_df.keys():
        raise IOError("The input dataframe is not from the same source")
    if 'state_id' not in mandate_df.keys():
        raise IOError("The input dataframe is not from the same source")
    mandate_df = mandate_df.rename(columns={'state': 'state_fullname',
                                            'state_id': 'state'})
    mandate_df.drop_duplicates(inplace=True)
    return mandate_all


state_count_monthly = case_count_processing(state_count)
state_mandate = mandate_processing(state_mandate)

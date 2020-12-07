"""
Function to get tavisci.yml working. Not working yet. Not working yet.
how about now. 4th attempt?
"""
import datetime
import json
from urllib.request import urlopen

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from jupyter_dash import JupyterDash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

state_count = pd.read_csv("data/state_case.csv")
state_mandate = pd.read_csv("data/state_mandate.csv")

def case_count_processing(case_count_df):
	'''
	Function used to process the case count dataset downloaded from github site.

	Argument:
	case_count_df -- The original dataset

	Return:
	case_count_monthly -- Return the selected fields, change the date column datatype
	to match the mandate dataset, add month column, and group the dataframe on state and
	month. The result dataframe has the monthly case count and death count for each state
	'''
	if 'state' not in case_count_df.keys():
		raise IOError("The input dataframe is not from the same source")
	if 'submission_date' not in case_count_df.keys():
		raise IOError("The input dataframe is not from the same source")
	if 'new_case' not in case_count_df.keys():
		raise IOError("The input dataframe is not from the same source")
	if 'new_death' not in case_count_df.keys():
		raise IOError("The input dataframe is not from the same source")
	case_count_df = case_count_df[['state','submission_date','new_case','new_death']]
	case_count_df = case_count_df.rename(columns = {'submission_date':'date'})
	case_count_df['date'] = pd.to_datetime(case_count_df['date'])
	case_count_df['month'] = pd.to_datetime(case_count_df['date']).dt.month
	case_count_monthly = case_count_df.groupby(['state','month']).sum().reset_index() 
	return case_count_monthly

def mandate_processing(mandate_df):
	## Zhaowen could you please add your processing code over here.
	## The above two lines are what I used to process for the data you've
	## already cleaned. Thank you!
	if 'state' not in mandate_df.keys():
		raise IOError("The input dataframe is not from the same source")
	if 'state_id' not in mandate_df.keys():
		raise IOError("The input dataframe is not from the same source")
	mandate_df = mandate_df.rename(columns = {'state':'state_fullname', 'state_id':'state'})
	mandate_df.drop_duplicates(inplace=True)

state_count_monthly = case_count_processing(state_count)
state_mandate = mandate_df(state_mandate)


def covid(not_important):
    """
    Function to get tavisci.yml working. Not working yet. Not working yet.
    how about now. 4th attempt?
    """

    not_important1 = not_important
    return not_important1

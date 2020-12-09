"""
Function to get tavisci.yml working. Not working yet. Not working yet.
how about now. 4th attempt?
"""


def test(not_important):
    """
    Function to get tavisci.yml working.?
    """

    not_important1 = not_important
    return not_important1

# def case_count_processing(case_count_df):
#     '''
#     Function used to process the case count dataset downloaded from github.

#     Argument:
#     case_count_df -- The original dataset

#     Return:
#     case_count_monthly --  The result dataframe has the monthly case count
#     and death count for each state per hundred thousand of state population
#     size
#     '''
#     try:
#     case_count_df = case_count_df[['state', 'submission_date', 'new_case',
#                                    'new_death']]
#     except KeyError:
#         print("The input dataframe is not from the same source")
#     case_count_df = pd.merge(case_count_df, states_population)
#     case_count_df['new_case'] = case_count_df['new_case'] / \
#         case_count_df['population'] * 100000
#     case_count_df['new_death'] = case_count_df['new_death'] / \
#         case_count_df['population']*100000
#     case_count_df = case_count_df.rename(columns={'submission_date': 'date'})
#     case_count_df['date'] = pd.to_datetime(case_count_df['date'])
#     case_count_df['month'] = pd.to_datetime(case_count_df['date']).dt.month
#     case_count_monthly = case_count_df.groupby(['state',
#                                                 'month']).sum().reset_index()
#     return case_count_monthly

"""
Function to process covid mandates at the state level.
"""


def mandate_processing(mandate_df):
    '''
    Function used to process the mandate dataset downloaded from healthdata.gov

    Argument:
    mandate_df -- The original mandate dataset

    Return:
    mandate_df -- Five most common mandates announced throughout the states,
    and drop the duplicate rows in the dataframe.
    '''
    if 'state_id' not in mandate_df.keys():
        raise KeyError("The input dataframe is not from the same source")

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

    mandate_rows.loc[mandate_rows["policy_type"]
                     .str.contains("Mask"), "policy_type"] = "Mask Wearing"

    mandate_rows = mandate_rows.drop(['policy_level', 'start_stop'], axis=1)

    mandate_rows = mandate_rows.rename(columns={'state_id': 'state'})
    mandate_rows.drop_duplicates(inplace=True)
    return mandate_rows

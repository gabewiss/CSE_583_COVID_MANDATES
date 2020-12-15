"""
Function to get plotly and dash to work normally
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from count_processing import count_processing
from mandate_processing import mandate_processing

state_mandate = pd.read_csv(
    "https://healthdata.gov/node/3281076/download",
    index_col=False)

state_count = pd.read_csv(
    "https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD",
    index_col=False)

state_population = pd.read_csv(
    "../data/states_population.csv",
    index_col=False)
state_mandate = mandate_processing(state_mandate)
state_count, state_count_monthly =\
    count_processing(state_count, state_population)

# activate dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# dash layout
app.layout = html.Div([

    html.H1("Covid-policy Visualization", style={'text-align': 'center'}),

    html.Div([
        dcc.Slider(id="slct_month",
                   min=state_count_monthly['month'].min(),
                   max=state_count_monthly['month'].max(),
                   value=state_count_monthly['month'].min(),
                   marks={i: '{}'.format(i) for i in range(1, 13)}
                   ),
        dcc.RadioItems(id='choro_case_death',
                       options=[{'label': i, 'value': i}
                                for i in ['new_case', 'new_death']],
                       value='new_case',
                       labelStyle={'display': 'inline-block'}
                       )
    ]),

    html.Div([
        dcc.Graph(id='state_choropleth')
    ]),

    html.Label("Line plot for the chosen states"),

    html.Div(["User's input: ",
              dcc.Input(id="state_input_1", type='text', value='CA'),
              dcc.Input(id="state_input_2", type='text', value='TX'),
              html.Button(id='submit_button', n_clicks=0, children='Submit'),
              html.Br(),
              dcc.RadioItems(id='line_case_death',
                             options=[{'label': i, 'value': i}
                                      for i in ['new_case_norm',
                                      'new_death_norm']],
                             value='new_case_norm',
                             labelStyle={'display': 'inline-block'}
                             )
              ],
             style={
                 'borderBottom': 'thin lightgrey solid',
                 'backgroundColor': 'rgb(250, 250, 250)',
                 'padding': '10px 5px'}),

    html.Div([
        dcc.Graph(id='line_plot_1')
    ],
             style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='line_plot_2')
    ],
             style={'width': '49%',
                    'display': 'inline-block',
                    'float': 'right'})

])


@app.callback(
    Output(component_id='state_choropleth', component_property='figure'),
    Input(component_id='slct_month', component_property='value'),
    Input(component_id='choro_case_death', component_property='value')
)
def update_choropleth_graph(option_slctd, click):

    state_count_monthly_cp = state_count_monthly.copy()
    state_count_monthly_cp =\
        state_count_monthly_cp[state_count_monthly_cp['month'] == option_slctd]

    fig = px.choropleth(state_count_monthly_cp,
                        color=click,
                        locations='state',
                        locationmode="USA-states",
                        scope="usa",
                        range_color=[0, state_count_monthly_cp[click].max()])

    fig.update_layout(transition_duration=500)

    return fig


# dash callback function
@app.callback(
    Output(component_id='line_plot_1', component_property='figure'),
    Output(component_id='line_plot_2', component_property='figure'),
    Input(component_id='line_case_death', component_property='value'),
    Input(component_id='submit_button', component_property='n_clicks'),
    State(component_id='state_input_1', component_property='value'),
    State(component_id='state_input_2', component_property='value')
)
def update_lineplot_graph(click, n_clicks, input1, input2):
    color = ['black', 'brown', 'aqua', 'green', 'grey', 'yellowgreen', 'red']

    state_count_cp = state_count.copy()
    state_count_cp_1 = state_count_cp[state_count_cp["state"] == input1]
    state_count_cp_2 = state_count_cp[state_count_cp["state"] == input2]

    state_mandate_cp = state_mandate.copy()
    state_mandate_cp_1 = state_mandate_cp[state_mandate_cp["state"] == input1]
    state_mandate_cp_2 = state_mandate_cp[state_mandate_cp["state"] == input2]

    fig1 = go.Figure()
    fig1.add_traces(go.Scatter(
        x=state_count_cp_1['date'],
        y=state_count_cp_1[click],
        mode='lines',
        name=click + " count"))

    i = 0
    count = state_count_cp_1[click].tolist()
    count.sort()
    for date, mandate in\
            zip(state_mandate_cp_1['date'], state_mandate_cp_1['policy_type']):
        fig1.add_traces(go.Scatter(
            x=[date, date],
            y=[0, count[-1]],
            line={
                'color': color[i],
                'width': 2,
                'dash': 'dashdot',
            },
            name=mandate
        ))
        i += 1

    fig2 = go.Figure()
    fig2.add_traces(go.Scatter(
        x=state_count_cp_2['date'],
        y=state_count_cp_2[click],
        mode='lines',
        name=click + " count"))

    i = 0
    count = state_count_cp_2[click].tolist()
    count.sort()
    for date, mandate in\
            zip(state_mandate_cp_2['date'], state_mandate_cp_2['policy_type']):
        fig2.add_traces(go.Scatter(
            x=[date, date],
            y=[0, count[-1]],
            line={
                'color': color[i],
                'width': 2,
                'dash': 'dashdot',
            },
            name=mandate
        ))
        i += 1

    return fig1, fig2


if __name__ == '__main__':
    app.run_server(debug=True)

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:59:57 2019

@author: Kevin Zhang
"""

import dash
import pandas as pd

from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

import dash_html_components as html
import dash_core_components as dcc
import dash_table

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

app = dash.Dash(__name__)
application = app.server
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

continents = set(df['continent'])
years = df['year'].unique()

## Design your App ##
app.layout = html.Div([
        html.Div([
                dcc.Graph(id = 'select-graph'),
                dcc.Slider(id = 'select-year',
                   min = 0,
                   max = years.shape[0]-1,
                   marks={i: 'Year {}'.format(years[i]) for i in range(years.shape[0])},
                   value = years[0]
                )
        ])
])
                
@app.callback(
        dash.dependencies.Output('select-graph', 'figure'),
        [dash.dependencies.Input('select-year', 'value')])
def set_graph(select_year):
    sub_df = df[df['year'] == years[select_year]]
    
    draw = {
            'data': [
                go.Scatter(
                    x=sub_df[sub_df['continent'] == i]['gdpPercap'],
                    y=sub_df[sub_df['continent'] == i]['lifeExp'],
                    text=sub_df[sub_df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in sub_df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    return draw
    
if __name__ == '__main__':
    application.run(debug=True)
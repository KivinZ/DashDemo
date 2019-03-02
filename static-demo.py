# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:48:11 2019

@author: Kevin Zhang
"""

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
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

countries = set(df['country'])


## Design your App ##
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdpPercap'],
                    y=df[df['continent'] == i]['lifeExp'],
                    text=df[df['continent'] == i]['country'] + " " + df[df['continent'] == i]['year'].apply(str),
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
    
if __name__ == '__main__':
    app.run_server(debug=True)
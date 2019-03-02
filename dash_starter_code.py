# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:48:11 2019

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

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    
if __name__ == '__main__':
    app.run_server(debug=True)

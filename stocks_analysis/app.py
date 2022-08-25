from datetime import date, timedelta
import sys
import numpy as np
import pandas as pd
import plotly.express as px
import yfinance as yf
from dash import Dash, html, dcc, Input, Output, State
from math import factorial
from time import sleep


app = Dash(__name__)
stocks_options = ['AAPL', 'MSFT', 'ADBE']
#maxsize = sum of permutations of stocks_options when s=3 + s=2 + s=1
#permutation = n!/(n-s)! -> n = len(stocks_options), s = number of stocks choosen
def get_data(symbols: list, start: str|None, end: str|None):
    print('Dados coletados')
    today = date.today()
    # start and end must be in "YYYY-MM-DD" format
    end = f"{today.year}-{f'0{today.month}' if len(str(today.month))==1 else today.month}-{today.day}" if end==None else end
    start = f"{today.year}-01-01" if start==None else start
    print(f"{start} <-> {end} {type(end)}")
    if len(symbols)==0:
        return None
    elif len(symbols)==1:
        data = yf.Ticker(symbols[0]).history(start=start, end=end).Close
    else:
        data = yf.Tickers(symbols).history(start=start, end=end).Close
    return data

def return_of(data):
    percentage_return_of_data = data/data.iloc[0]-1
    return percentage_return_of_data

def plot_(data, _format=None):
    fig = px.line(data)
    if _format=='%':
        fig.layout.yaxis = dict(tickformat=".2%")
    return fig

@app.callback(
    Output("graph", "figure"),
    inputs=Input("refresh-graph", "n_clicks"),
    state=[
        State("dropdown-symbols", "value"),
        State("interval-date", "start_date"),
        State("interval-date", "end_date"),
    ]
)
def update_graph(n_clicks, symbols, start_date, end_date):
    print(n_clicks)
    data = get_data(symbols, start=start_date, end=end_date)
    percentage_return = return_of(data)
    fig = plot_(percentage_return, _format='%')
    return fig

app.layout = html.Div([
    html.H4('Analysis of stocks collected from yahoo finance'),
    html.P('Select the stock'),
    dcc.Dropdown(
        id="dropdown-symbols",
        options=stocks_options,
        value=stocks_options[0],
        multi=True
    ),
    html.P('Select the interval'),
    dcc.DatePickerRange(
        id="interval-date",
        month_format='MMMM Y',
        display_format='DD/MM/YYYY',
        start_date_placeholder_text='Start date',
        end_date_placeholder_text='End date',
        max_date_allowed=date.today(),
    ),
    dcc.Graph(id="graph", figure=update_graph(None, ['MSFT'], None, None)),
    html.Button("Refresh", id='refresh-graph')
])
if __name__ == "__main__":
    app.run_server(debug=True)

from dash import Dash, html, dcc, Input, Output
import datetime as dt
import pandas as pd
import numpy as np
from flask_caching import Cache

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

cache = Cache(app.server, config = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'temp/dataset-caching-directory'
})

TIMEOUT = 60

@cache.memoize(timeout = TIMEOUT)
def query_data():
    np.random.seed(0)
    df = pd.DataFrame(
        np.random.randint(0, 100, size = (100, 4)),
        columns = list('ABCD')
    )
    now = dt.datetime.now()
    df['time'] = [now - dt.timedelta(seconds = 5*i) for i in range(100)]
    return df.to_json(date_format='iso', orient='split')

def dataframe():
    return pd.read_json(query_data(), orient='split')

app.layout = html.Div([
    html.Div('Data was updated within the last {} seconds'.format(TIMEOUT)),
    dcc.Dropdown(dataframe().columns, 'A', id='live-dropdown'),
    dcc.Graph(id='live-graph')
])

@app.callback(
    Output('live-graph', 'figure'),
    Input('live-dropdown', 'value')
)
def update_live_graph(value):
    df = dataframe()
    now = dt.datetime.now()
    
    fig = {
        'data': [{
            'x':df['time'],
            'y':df[value],
            'line': {
                'width':1,
                'color':'#0074d9',
                'shape': 'spline'
            }
        }],
        'layout': {
            'shapes': [{
                'type': 'line',
                'xref': 'x', 'x0': now, 'x1': now,
                'yref': 'paper', 'y0':0, 'y1':1,
                'line':{'color': 'darkgrey', 'width':1}
            }],
            'annotations': [{
                'showarrow':False,
                'xref': 'x', 'x':now,'xanchor':'right',
                'yref':'paper','y':0.95, 'yanchor':'top',
                'text': 'Current time ({}:{}:{})'.format(now.hour, now.minute, now.second),
                'bgcolor': 'rgba(255,255,255,0.8)'
            }],
            'margin': {'l': 40, 'b': 40, 'r': 20, 't': 10},
            'xaxis': {'showgrid': False, 'zeroline': False},
            'yaxis': {'showgrid': False, 'zeroline': False}
        }
    }

    return fig

if __name__ == '__main__':
    app.run(debug=True)
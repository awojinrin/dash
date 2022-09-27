from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import numpy as np
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Creating a sample dataframe with 6 columns
np.random.seed(0)
df = pd.DataFrame({'Col ' + str(i+1): np.random.randn(30) for i in range(6)})

app.layout = html.Div([
    html.Div(
        dcc.Graph(id = 'graph1', config = {'displayModeBar':False}),
        className='four columns'
    ),
    html.Div(
        dcc.Graph(id = 'graph2', config = {'displayModeBar':False}),
        className='four columns'
    ),
    html.Div(
        dcc.Graph(id = 'graph3', config = {'displayModeBar':False}),
        className='four columns'
    )
], className='row')

def get_figure(df, x_col, y_col, selectedpoints, selectedpoints_local):

    if selectedpoints_local and selectedpoints_local['range']:
        ranges = selectedpoints_local['range']
        selection_bounds = {'x0': ranges['x'][0], 'x1': ranges['x'][1],
            'y0': ranges['y'][0], 'y1': ranges['y'][1]}
    else:
        selection_bounds = {
            'x0': np.min(df[x_col]), 'x1':np.max(df[x_col]), 
            'y0': np.min(df[y_col]), 'y1': np.max(df[y_col])
        }
    
    fig = px.scatter(df, x = x_col, y = y_col, text = df.index)
    fig.update_traces(selectedpoints = selectedpoints,
        customdata = df.index,
        mode = 'markers+text',
        marker = { 'color':'rgba(0,116,217,0.7)', 'size':20},
        unselected = {'marker': {'opacity': 0.3}, 'textfont':{'color':'rgba(0,0,0,0)'}})
    fig.update_layout(margin = {'l': 20, 'r': 0, 'b': 15, 't': 5}, dragmode='select', hovermode=False)
    fig.add_shape(dict({'type':'rect',
        'line': {'width':1, 'dash': 'dot', 'color': 'darkgrey'}},
        **selection_bounds))

    return fig

@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('graph3', 'figure'),
    Input('graph1', 'selectedData'),
    Input('graph2', 'selectedData'),
    Input('graph3', 'selectedData')
)
def callback(selection1, selection2, selection3):
    selectedpoints = df.index
    for selected_data in [selection1, selection2, selection3]:
        if selected_data and selected_data['points']:
            selectedpoints = np.intersect1d(selectedpoints, [p['customdata'] for p in selected_data['points']])
    
    return [get_figure(df, 'Col 1', 'Col 2', selectedpoints, selection1),
        get_figure(df, 'Col 3', 'Col 4', selectedpoints, selection2),
        get_figure(df, 'Col 5', 'Col 6', selectedpoints, selection3)]

if __name__ == '__main__':
    app.run(debug=True)
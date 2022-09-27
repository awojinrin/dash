# Button
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

external_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    html.Div(dcc.Input(id = 'input-box', type='text')),
    html.Button('Submit', id='button-example'),
    html.Div(id='output-container-button',
        children='Enter a value and press submit')
])

@app.callback(
    Output('output-container-button', 'children'),
    [Input('button-example', 'n_clicks')],
    [State('input-box', 'value')]
)
def update_output(n_clicks, value):
    return f'The input value was {value} and the button has been clicked {n_clicks} times'

if __name__ == '__main__':
    app.run(debug=True)
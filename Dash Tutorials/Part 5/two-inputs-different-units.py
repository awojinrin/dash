from dash import Dash, html, dcc, Input, Output, ctx
from dash.exceptions import PreventUpdate

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div('Convert Temperature'),
    'Celsius',
    dcc.Input(
        id='celsius',
        value = 0.0,
        type = 'number'
    ),
    '    Fahrenheit',
    dcc.Input(
        id='fahrenheit',
        type='number',
        value = 32.0
    )
])

@app.callback(
    Output('celsius', 'value'),
    Output('fahrenheit', 'value'),
    Input('celsius', 'value'),
    Input('fahrenheit', 'value')
)
def sync_output(celsius_value, fahrenheit_value):
    trigger_id = ctx.triggered_id
    try:
        celsius_value = (fahrenheit_value - 32)/1.8 if trigger_id == 'fahrenheit' else celsius_value
        fahrenheit_value = (celsius_value *1.8) +32 if trigger_id =='celsius' else fahrenheit_value
    except TypeError:
        raise PreventUpdate
    return celsius_value, fahrenheit_value

if __name__ == '__main__':
    app.run(debug=True)
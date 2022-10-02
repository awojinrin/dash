from dash import Dash, html, dcc, Input, Output, ctx

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Slider(
        id = 'circular-slider', min=0, max=20,
        marks={i:str(i) for i in range(21)},
        value = 5
    ),
    dcc.Input(id='circular-input', type='number', min=0, max=20, value=5)
])

@app.callback(
    Output('circular-slider', 'value'),
    Output('circular-input', 'value'),
    Input('circular-slider', 'value'),
    Input('circular-input', 'value')
)
def callback(slider_value, input_value):
    trigger_id = ctx.triggered_id
    value = input_value if trigger_id =='circular-input' else slider_value
    return value, value

if __name__ == '__main__':
    app.run(debug=True)
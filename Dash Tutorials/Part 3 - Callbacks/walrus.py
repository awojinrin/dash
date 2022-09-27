from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6('Change the value in the text box to see callbacks in action'),
    html.Div([
        'Input: ',
        my_input := dcc.Input(value='Initial value', type = 'text')
    ]),
    html.Br(),
    my_output := html.Div()
])

@app.callback(
    Output(my_output, 'children'),
    Input(my_input, 'value')
)
def update_output(input_value):
    return f'Output: {input_value}'

if __name__ == '__main__':
    app.run(debug=True)
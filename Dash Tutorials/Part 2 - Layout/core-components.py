# Core Components

from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([

    html.Div(children = [
        html.Label('Dropdown'),
        dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            ['New York City', 'Montreal', 'San Francisco'],
            ['Montreal', 'San Francisco'],
            multi=True),
        
        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal')
    ], style = {'padding': 10, 'flex':1}),

    html.Div(style = {'flex':1}, children = [
        html.Br(),
        html.Label('Text Input'),
        dcc.Input(
            placeholder='Enter a value...',
            type = 'text',
            value = ''
        ),

        html.Br(),
        html.Label('Textarea'),
        dcc.Textarea(
            placeholder='Enter a value...',
            value = 'This is a text area component',
            style={'width':'70%'}
        )
    ]),

    html.Div(children = [
        html.Label('Checkboxes'),
        dcc.Checklist(
            ['New York City', 'Montreal', 'San Francisco'],
            ['Montreal', 'San Francisco']
        ),

        html.Br(),
        html.Label('Inline Checkboxes'),
        dcc.Checklist(
            ['New York City', 'Montreal', 'San Francisco'],
            ['Montreal', 'San Francisco'],
            inline=True),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value = 'MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0, max = 9,
            marks = {i: f'Label {i}' if i==1 else str(i) for i in range(1,6)},
            value = 5
        ),

        html.Br(),
        html.Label('Range Slider'),
        dcc.RangeSlider(-5, 10, 1, count=1, value=[-3,7])
        
    ], style = {'padding':10, 'flex':2})

], style = {'display': 'flex', 'flex-direction':'row'})

if __name__ == '__main__':
    app.run_server(debug=True)
from turtle import back
from dash import Dash, html, Input, Output, DiskcacheManager, callback
import time
import diskcache

cache = diskcache.Cache('./cache')
background_callback_manager = DiskcacheManager(cache)

app = Dash(__name__, background_callback_manager=background_callback_manager)

app.layout = html.Div([
    html.Div([
        html.P('Button not clicked', id='paragraph-id'),
        html.Progress(id='progress-bar', value='0')
    ]),
    html.Button('Run Job!', id='button-id'),
    html.Button('Cancel Running Job!', id='cancel-button-id')
])

@callback(
    Output('paragraph-id', 'children'),
    Input('button-id', 'n_clicks'),
    background=True,
    running = [
        (Output('button-id', 'disabled'), True, False),
        (Output('cancel-button-id', 'disabled'), False, True),
        (
            Output("paragraph-id", "style"),
            {"visibility": "hidden"}, {"visibility": "visible"},
        ),
        (
            Output('progress-bar', 'style'),
            {'visibility': 'visible'}, {'visibility': 'hidden'}
        )
    ],
    cancel = Input('cancel-button-id', 'n_clicks'),
    progress = [
        Output('progress-bar', 'value'),
        Output('progress-bar', 'max')
    ],
    prevent_initial_call = True
)
def update_progress(set_progress, n_clicks):
    total = 5
    for i in range(total+1):
        set_progress((str(i), str(total)))
        time.sleep(1)

    return f'Clicked {n_clicks} times'

if __name__ == '__main__':
    app.run(debug=True)
import time
import os
from dash import callback, Dash, Input, Output, html, DiskcacheManager
import diskcache

cache = diskcache.Cache('./cache')
background_callback_manager = DiskcacheManager(cache)

app = Dash(__name__, background_callback_manager=background_callback_manager)

app.layout = html.Div([
    html.Div(html.P('Button not clicked', id = 'paragraph-id')),
    html.Button('Run Job!', id='button-id'),
    html.Button('Cancel Running Job!', id='cancel-button-id')
])

@callback(
    Output('paragraph-id', 'children'),
    Input('button-id', 'n_clicks'),
    background=True,
    running=[
        (Output('button-id', 'disabled'), True, False),
        (Output('cancel-button-id', 'disabled'), False, True)
    ],
    cancel = [Input('cancel-button-id', 'n_clicks')],
    prevent_initial_call=True
)
def update_clicks(n_clicks):
    time.sleep(45)
    return f'Clicked {n_clicks} times'

if __name__ == '__main__':
    app.run(debug=True)
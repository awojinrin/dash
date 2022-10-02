from dash import Dash, html, Input, Output, callback, DiskcacheManager
import time
import diskcache

cache = diskcache.Cache('./cache')
background_callback_manager = DiskcacheManager(cache)

app = Dash(__name__, background_callback_manager=background_callback_manager)

app.layout = html.Div([
    html.Div(
        html.P('Button not clicked', id='paragraph-id')
    ),
    html.Button('Run Job!', id='button-id')
])

@callback(
    Output('paragraph-id', 'children'),
    Input('button-id', 'n_clicks'),
    background=True,
    running=[
        (Output('button-id', 'disabled'), True, False)
    ],
    prevent_initial_call=True
)
def update_click(n_clicks):
    t1 = time.time()
    time.sleep(37.0)
    t2 = time.time()
    return f'Clicked {n_clicks} times. Took {t2-t1} seconds.'

if __name__ == '__main__':
    app.run(debug=True)
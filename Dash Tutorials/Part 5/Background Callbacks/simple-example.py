import time
import os
import dash
from dash import DiskcacheManager, CeleryManager, Input, Output, html

if 'REDIS_URL' in os.environ:
    from celery import Celery
    celery_app = Celery(
        __name__, broker=os.environ['REDIS_URL'], backend=os.environ['REDIS_URL']
    )
    background_callback_manager = CeleryManager(celery_app)
else:
    import diskcache
    cache = diskcache.Cache('./cache')
    background_callback_manager = DiskcacheManager(cache)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(html.P('Button not clicked', id='paragraph-id')),
    html.Button('Run Job!', id='button-id')
])

@dash.callback(
    Output('paragraph-id', 'children'),
    Input('button-id', 'n_clicks'),
    background=True,
    manager = background_callback_manager
)
def update_clicks(n_clicks):
    time.sleep(2.0)
    return f'Clicked {n_clicks} times'

if __name__ == '__main__':
    app.run(debug=True)
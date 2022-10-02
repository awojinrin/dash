from dash import Dash, html, dcc, Input, Output
from flask_caching import Cache
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'temp/cache'
})
app.config.suppress_callback_exceptions = True

timeout = 15

app.layout = html.Div([
    html.Div(id='flask-cache-memoized-children'),
    dcc.RadioItems(
        [f'Option {i}' for i in range(1,4)], 'Option 1',
        id = 'flask-cache-memoized-dropdown'
    ),
    html.Div(f'Results are cached for {timeout} seconds')
])

@app.callback(
    Output('flask-cache-memoized-children', 'children'),
    Input('flask-cache-memoized-dropdown', 'value')
)
@cache.memoize(timeout=timeout)
def render(value):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return f'Selected "{value}" at "{current_time}"'

if __name__ == '__main__':
    app.run(debug=True)
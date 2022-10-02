from dash import Dash, html, dcc, Input, Output, DiskcacheManager, callback
import time
import diskcache
import plotly.express as px

cache = diskcache.Cache('./cache')
background_callback_manager = DiskcacheManager(cache)

def make_progress_graph(progress, total):
    progress_graph = px.bar(x=[progress])
    progress_graph.update_xaxes(range=[0, total], title='')
    progress_graph.update_yaxes(showticklabels=False, title='')
    progress_graph.update_layout(height=100, margin=dict(t=20, b=40))
    return progress_graph


app = Dash(__name__, background_callback_manager=background_callback_manager)

app.layout = html.Div([
    html.Div([
        html.P('Button not clicked', id='paragraph-id'),
        dcc.Graph(id='progress-bar-graph', figure = make_progress_graph(0, 10))
    ]),
    html.Button('Run Job!', id='button'),
    html.Button('Cancel Running Job!', id='cancel-button')
])

@callback(
    Output('paragraph-id', 'children'),
    Input('button', 'n_clicks'),
    background=True,
    running=[
        (Output('button', 'disabled'), True, False),
        (Output('cancel-button', 'disabled'), False, True),
        (Output('paragraph-id', 'style'),
            {'visibility':'hidden'}, {'visibility':'visible'}),
        (Output('progress-bar-graph', 'style'),
            {'visibility':'visible'}, {'visibility': 'hidden'})
    ],
    cancel = Input('cancel-button', 'n_clicks'),
    progress = Output('progress-bar-graph', 'figure'),
    progress_default=make_progress_graph(0, 10),
    prevent_initial_call=True
)
def update_progress(set_progress, n_clicks):
    total = 10
    for i in range(total +1):
        time.sleep(0.5)
        set_progress(make_progress_graph(i, 10))

    return f'Clicked {n_clicks} {"time" if n_clicks==1 else "times"}'

if __name__ == '__main__':
    app.run(debug=True)
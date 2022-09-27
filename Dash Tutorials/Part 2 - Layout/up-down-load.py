import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

app = Dash(
    __name__, prevent_initial_callbacks=True,
    title = 'Uploading and Downloading Files'
)

app.layout = html.Div(
    [html.Button('Download Text', id='btn-txt'),
    dcc.Download(id='download-text-index')
    ]
)

@app.callback(
    Output('download-text-index', 'data'),
    Input('btn-txt', 'n_clicks')
)
def func(n_clicks):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    else:
        return dict(content = 'Hello world!', filename='hello.txt')

if __name__ == '__main__':
    app.run(debug=True)
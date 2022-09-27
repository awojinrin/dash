from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div(
    dcc.Loading([
        # ...
    ])
)

if __name__ == '__main__':
    app.run(debug=True)
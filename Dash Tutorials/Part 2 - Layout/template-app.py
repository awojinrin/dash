from dash import Dash, html, dcc, Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([])

if __name__ == '__main__':
    app.run(debug=True)
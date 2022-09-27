from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div()

if __name__ == '__main__':
    app.run(debug=True)
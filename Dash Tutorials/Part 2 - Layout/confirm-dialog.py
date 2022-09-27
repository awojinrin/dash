from operator import imod
from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div(
    dcc.ConfirmDialogProvider(
        children = html.Button(
            'Click Me',
        ),
        id = 'danger-danger',
        message='Danger danger! Are you sure you want to continue?'
    )
)

if __name__ == '__main__':
    app.run(debug=True)
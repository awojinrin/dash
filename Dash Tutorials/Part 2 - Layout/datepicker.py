from dash import Dash, html, dcc
from datetime import date

app = Dash(__name__)

app.layout = html.Div([
    html.Label('Date Picker Single'),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=date(1997,5,10)
    ),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Label('Date Picker Range'),
    dcc.DatePickerRange(
        id = 'date-picker-range',
        start_date = date(1997,5,3),
        end_date_placeholder_text='Select a date!'
    )]
)

if __name__ == '__main__':
    app.run(debug=True)
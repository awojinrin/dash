from dash import Dash, html, dcc, Input, Output, State, ctx

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

options = ['Lagos', 'Abuja', 'Port Harcourt', 'Ibadan']

app.layout = html.Div([
    dcc.Checklist(['All'], [], id='all-checklist', inline=True),
    dcc.Checklist(options, [], id='city-checklist', inline=True)
])

@app.callback(
    Output('all-checklist', 'value'),
    Output('city-checklist', 'value'),
    Input('all-checklist', 'value'),
    Input('city-checklist', 'value')
)
def sync_checklists(all_selected, cities_selected):
    input_id = ctx.triggered_id
    if input_id == 'city-checklist':
        all_selected = ['All'] if set(cities_selected)==set(options) else []
    else:
        cities_selected = options if all_selected else []
    return all_selected, cities_selected

if __name__ == '__main__':
    app.run(debug=True)
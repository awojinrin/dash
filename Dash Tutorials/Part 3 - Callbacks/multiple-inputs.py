from dash import Dash, html, dcc, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Fertility rate, total (births per woman)',
                id = 'xaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='xaxis-type',
                inline=True
            )
        ], style = {'width':'48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Life expectancy at birth, total (years)',
                id='yaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'], 'Linear',
                id='yaxis-type', inline=True
            )
        ], style = {'width': '48%', 'float':'right', 'display':'inline-block'})
    ]),
    
    dcc.Graph(id = 'indicator-graphic'),

    dcc.Slider(
        df['Year'].min(),
        df['Year'].max(),
        step=None,
        id = 'year-slider',
        value = df['Year'].max(),
        marks = {str(year): str(year) for year in df['Year'].unique()}
    )
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-column', 'value'),
    Input('yaxis-type', 'value'),
    Input('year-slider', 'value')
)
def update_graph(xaxis_column_name, xaxis_type, 
    yaxis_column_name, yaxis_type, year_value):

    data = df[df['Year'] == year_value]

    fig = px.scatter(x = data[data['Indicator Name'] == xaxis_column_name]['Value'] , 
        y = data[data['Indicator Name'] ==yaxis_column_name]['Value'],
        hover_name=data[data['Indicator Name'] ==yaxis_column_name]['Country Name'])
    
    fig.update_layout(margin = {'l':40,'b':40, 't':10, 'r':0},
        hovermode='closest')

    fig.update_xaxes(title = xaxis_column_name, type = xaxis_type.lower())

    fig.update_yaxes(title = yaxis_column_name, type = yaxis_type.lower())

    return fig

if __name__ == '__main__':
    app.run(debug=True)
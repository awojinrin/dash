# Scatter Plot Visualization

from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(
    df, x = 'gdp per capita', y = 'life expectancy',
    size = 'population', color = 'continent', hover_name = 'country',
    log_x=True, size_max=60
)

fig.update_layout(
    plot_bgcolor = '#333333',
    paper_bgcolor = '#333333',
    font_color = '#DDDDDD'
)

app.layout = html.Div(
    dcc.Graph(
        id = 'life-exp-vs-gdp',
        figure = fig
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
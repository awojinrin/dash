from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        figure = dict(
            data = [
                dict(
                    x = list(range(1995, 2013)),
                    y = [219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                        350, 430, 474, 526, 488, 537, 500, 439],
                    name = 'Rest of World',
                    marker = dict(color='rgb(55, 83, 109)')
                ),
                dict(
                    x = list(range(1995, 2013)),
                    y = [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                        299, 340, 403, 549, 499],
                    name = 'China',
                    marker = dict(color = 'rgb(26, 118, 255)')
                )
            ],
            layout = dict(
                title = 'US Export of Plastic Scrap',
                show_legend=True,
                legend = dict(x=0, y=1.0),
                margin = dict(l=40, r=0, t=40, b=30)
            )
        ), style = {'height':500},
        id = 'my-graph-example'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
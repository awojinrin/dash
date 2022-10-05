from dash import Dash, html
import base64

app = Dash(__name__, title='Embedding Images', update_title='Loading...')

image_filename = '7456.jpg'

def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/jpg;base64,' + base64.b64encode(image).decode('utf-8')

app.layout = html.Div([
    html.Div(html.Img(src='assets/12318.jpg')),
    html.Div([
        html.Img(src= b64_image(image_filename))
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
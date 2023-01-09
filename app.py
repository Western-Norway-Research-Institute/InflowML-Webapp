# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('tilsig_aaroy.csv', index_col=0)

fig = px.line(df, y="tilsig")

fig.update_layout(
    plot_bgcolor=app_color["graph_bg"],
    paper_bgcolor=app_color["graph_bg"],
    font_color="white"
)

app.layout = html.Div(children=[
    html.H1(children='Tilsig Årøy', style={'color': 'white'},),

    html.Div(children='''
        Tilsig: Årøy kraftverk
    ''', style={'color': 'white'},),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
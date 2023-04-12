import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dbiot
import plotly.graph_objs as go

df = pd.DataFrame(list(dbiot.consultar_sensore()))


def create_dash(flask_app):
    app = dash.Dash(server=flask_app, name="Nose", external_stylesheets=[dbc.themes.UNITED],
                    url_base_pathname="/dashb/")

    app.layout = html.Div(children=[
        html.H1('Monitoreo del Sistema de IoT', style={'textAlign': 'center'}),
        html.Br(),
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in df.columns],
            value='age',
            id='dropdown',
            style={"width": "50%", "offset": 1, },
            clearable=False,
        ),
        dcc.Graph(id='scatter')
    ])

    @app.callback(
        Output(component_id='scatter', component_property='figure'),
        Input(component_id='dropdown', component_property='value'),
    )
    def update_scatter(feature):
        fig = px.scatter(df, x=feature, y=feature, color=feature)
        return fig


'''def create_dash1(flask_app):
    app = dash.Dash(server=flask_app, name="Nose", external_stylesheets=[dbc.themes.UNITED],
                    url_base_pathname="/dashb1/")

    app.layout = html.Div(children=[
        html.H1('Monitoreo del Sistema de IoT', style={'textAlign': 'center'}),
        html.Br(),
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in df.columns],
            value='age',
            id='dropdown',
            style={"width": "50%", "offset": 1, },
            clearable=False,
        ),
        dcc.Graph(id='histogram')
    ])

    @app.callback(
        Output(component_id='histogram', component_property='figure'),
        Input(component_id='dropdown', component_property='value'),
    )
    def update_hist(feature):
        fig1 = px.histogram(df, x=feature)
        return fig1'''

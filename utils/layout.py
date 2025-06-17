# App layout

from utils.third_party import dbc, html, dcc, Output, Input, State, callback
from utils.local import fig


# Define app layout
def layout(): return\
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div(className='title', children=["Map of the World - Wildfires to be populated"]),
            ])
        ], justify="center"),
        dbc.Row([
            dbc.Col([
                html.Div([
                    dcc.Graph(
                        id="map", figure=fig,
                        config={'displayModeBar': False},
                        style={'height': '90%', 'width': '90%', 'margin-top':'2rem'},
                        className='border',
                    ),
                ], className="map-wrapper"),
            ])
        ], justify="center"),
    ])


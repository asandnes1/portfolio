# Imports
from utils.third_party import dash, dbc, dcc, html

# Page registration
dash.register_page(
    __name__,
    path='/testimonials',
    location='navbar',
    description='',
    order=2,
)

def layout(): return\
    dbc.Container(
        dbc.Row([
            dbc.Col([
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        dcc.Markdown(''' ##### Amgen Research Copenhagen '''),
                    ]),
                ], justify='center', align='center', style={'border-bottom':'Solid', 'border-color':'gray', 'color':'gray'}),
                dbc.Row([  # Person 1
                    dbc.Col([
                        dcc.Markdown(''' ##### **Johannes Dolberg** '''),
                        dbc.Row([
                            dbc.Col([
                                html.Img(src='./assets/statics/icons8-envelope-48.png', height='25px', style={'margin-bottom':'5px'}),
                            ], width=1),
                            dbc.Col([
                                dcc.Markdown(''' ###### johannesdolberg@gmail.com ''', style={'margin-left':'5px'})
                            ], width=11),
                        ])
                    ], xs=12, sm=12, md=12, lg=4, xl=4, style={'padding':'20px'}),
                    dbc.Col([
                        dcc.Markdown(
                            ''' ###### “We enjoyed having Andreas working with our computational science group as a student\
                            helper for two years before completing his thesis.\
                            During this time, he diligently pursued learning Python and became well-versed in Dash Enterprise.\
                            He has a keen eye for creating insightful dashboards, often in close collaboration with subject\
                            matter experts. Andreas demonstrated this ability multiple times with projects related to both\
                            biology and chemistry. Additionally, he engaged in various analyses related to his thesis on\
                            applying RNA seq analysis on DNA-encoded libraries, which led to insights for further\
                            exploration.” ''', style={'margin':'20px'},
                        ),
                    ], xs=12, sm=12, md=12, lg=6, xl=6),
                ], justify='center', align='center'),
                html.Hr(),
                dbc.Row([  # Person 2
                    dbc.Col([
                        dcc.Markdown(''' ##### **Martin Bengtsson** '''),
                        dbc.Row([
                            dbc.Col([
                                html.Img(src='./assets/statics/icons8-envelope-48.png', height='25px', style={'margin-top':'13px'}),
                            ], width=1),
                            dbc.Col([
                                dcc.Markdown(''' ###### martin76@gmail.com ''', style={'margin-left':'5px'}),
                                dcc.Markdown(''' ###### martin.bengtsson@amgen.com ''', style={'margin-left':'5px'}),
                            ]),
                        ], justify='center')
                    ], xs=12, sm=12, md=12, lg=4, xl=4, style={'padding':'20px'}),
                    dbc.Col([
                        dcc.Markdown(
                            ''' ###### “Andreas immediately understood our needs and quickly delivered a useful\
                            prototype that we could build on together. If we weren't sure where to go, he did not\
                            hesitate to suggest a direction that in the end turned out to be the right call.\
                            He created complex visualizations and data extractions involving multiple database\
                            calls, while always making sure performance was good for the user.” ''', style={'margin':'20px'},
                        ),
                    ], xs=12, sm=12, md=12, lg=6, xl=6),
                ], justify='center', align='center'),
                html.Hr(),
                dbc.Row([  # Person 3
                    dbc.Col([
                        dcc.Markdown(''' ##### **Daniel Vik** '''),
                        dbc.Row([
                            dbc.Col([
                                html.Img(src='./assets/statics/icons8-envelope-48.png', height='25px', style={'margin-bottom':'5px'}),
                            ], width=1),
                            dbc.Col([
                                dcc.Markdown(''' ###### mrdanielvik@gmail.com ''', style={'margin-left':'5px'})
                            ]),
                        ], justify='center')
                    ], xs=12, sm=12, md=12, lg=4, xl=4, style={'padding':'20px'}),
                    dbc.Col([
                        dcc.Markdown(
                            ''' ###### “One of the things that struck me while working with Andreas is that he is ambitious and driven.\
                            He is eager to throw himself at projects that might be out of his depth at first. However, he is a fast learner,\
                            and immediately picks up the skills needed to achieve his goals. His "can-do attitude", grit, and ability to\
                            learn quickly makes him an incredibly promising scientist/engineer.” ''',
                            style={'margin':'20px'},
                        ),
                    ], xs=12, sm=12, md=12, lg=6, xl=6),
                ], justify='center', align='center'),
                html.Hr(),
            ])
        ], justify='center', style={'color':'gray', 'margin':'10px'}, className='font-family-default')
    )
# --- End layout


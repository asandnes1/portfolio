# Imports
from utils.third_party import dash, dbc, dcc, html

# Page registration
dash.register_page(
    __name__,
    path='/contact',
    location='navbar',
    description='',
    order=3,
)

def layout():return\
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Markdown('''### Andreas Sandnes''', style={'color':'gray'}),
                html.Br(),
                dbc.Row([  # Location
                    dbc.Col([
                        html.Img(src='./assets/statics/icons8-location-50.png', height='30px')
                    ], width=1),
                    dbc.Col([
                        dcc.Markdown(
                            '''
                                #### Copenhagen, Denmark
                            ''', style={'color':'gray'}
                        ),
                    ], width=10)
                ], justify='around', align='center'),
                html.Br(),
                dbc.Row([  # Email
                    dbc.Col([
                        html.Img(src='./assets/statics/icons8-envelope-48.png', height='30px')
                    ], width=1),
                    dbc.Col([
                        dcc.Markdown(
                            '''
                                #### asandnes92@gmail.com
                            ''', style={'color':'gray'}
                        ),
                    ], width=10)
                ], justify='around', align='center'),
                html.Br(),
                dbc.Row([  # Phone
                    dbc.Col([
                        html.Img(src='./assets/statics/icons8-resume-phone-64.png', height='30px')
                    ], width=1),
                    dbc.Col([
                        dcc.Markdown('''#### +45 27890160''', style={'color':'gray'}),
                    ], width=10)
                ], justify='around', align='center'),
                html.Br(),
                dbc.Row([  # LinkedIn
                    dbc.Col([
                        html.Img(src='./assets/statics/icons8-www-50.png', height='30px')
                    ], width=1),
                    dbc.Col([
                        html.Div('', style={'color':'gray', 'display':'inline-block'}),
                        html.A(
                            html.Img(src='./assets/statics/icons8-linkedin-48.png', height="40px"),
                            href="https://linkedin.com/in/andreas-sandnes/",
                            target='_blank',
                            style={"textDecoration": "none"},
                        ),
                    ], width=10)
                ], justify='around', align='center')
            ], width=10, style={'border-left':'solid', 'border-color':'gray'}),
        ], justify='center', className='font-family-default', style={'margin-top':'30px'}),
    ], fluid=True)
#--- End layout

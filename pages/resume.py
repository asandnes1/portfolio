# This file contains my resume.

# Imports
from utils.third_party import dash, dbc, dcc, html, callback


# Page registration
dash.register_page(
    __name__,
    path='/',
    location='navbar',
    description='This page contains my resume.',
    order=0,
)

def layout(): return\
    dbc.Container([
        
        dbc.Row([  # Header
            dbc.Col([
                dcc.Markdown(
                    '''
                        #### __Andreas Sandnes__
                        
                        ##### ***It would be pretty cool to combine bioinformatics with software development to create tools for researchers.***
                        
                        ###### Bioinformatics | Data Science | Data Analysis: Bulk RNA-seq; Single-cell RNA-seq; DNA Encoded Chemical Libraries | HPC | Bash | R | Seurat | Data Visualization | Software Development | Git | Python | Dash Plotly | SQL | HTML | CSS | Dashboard Development
                    ''', className='font-family-default',
                ),
            ])
        ], className='style_resume_header'),

        dbc.Row([  # CV Onepager
            dbc.Col([
                dbc.Accordion([
                    dbc.AccordionItem([
                        html.Div(
                            className='cv-wrapper',
                            children=[html.Img(src='./assets/cv_andreas_sandnes.png', width='100%', height='100%')],
                        ),      
                    ], title="CV Onepager"),
                    # Add option to download CV
                    dcc.Download(id="download-cv"),
                    dbc.Button("Download CV", id="btn-download-cv", color="primary", class_name="mt-3"),
                ], start_collapsed=True),
            ], class_name='remove-mp-left'),
        ], class_name='row-offset', style={'margin-bottom':'4rem'}),
        html.Hr(),

        dbc.Row([  # Profile text
            dbc.Col([
                dcc.Markdown(
                '''
                    #### Profile    
                ''', style={'color':'gray'}, className='font-family-default',
                ),
                dcc.Markdown(
                    '''
                        ###### I like optimize workflows and to develop tools that make my life easier.

                        ###### The following content is a more detailed description of my experience.
                    ''', style={'color':'lightgray'}, className='font-family-default',
                ),
            ]),
        ], class_name='row-offset', style={'margin-top':'4rem'}),
        
        # dbc.Row([
        #     dbc.Col([
        #         dbc.Accordion([
        #             dbc.AccordionItem([  # Work Experience
        #                 dbc.Row([
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ### Amgen Research Copenhagen
        #                             ''', style={'margin-top':'20px', 'color':'gray'}, className='font-family-default',
        #                         ),
        #                     ], xs=12, sm=12, md=7, lg=6, xl=6),
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 #### 02/2020 - 06/2024
        #                             ''', style={'margin-top':'20px', 'color':'gray'}, className='font-family-default',
        #                         ),
        #                     ], xs=12, sm=12, md=5, lg=6, xl=6)
        #                 ]),
        #                 dbc.Row([
        #                     dbc.Col(
        #                         dcc.Markdown(
        #                             '''
        #                                 #### Computational Science Group
        #                             ''', style={'margin-top':'20px', 'color':'gray'}, className='font-family-default',
        #                         ),
        #                     ),
        #                     dbc.Col(
        #                         dcc.Markdown(
        #                             '''
        #                                 #### 12/2021 - 06/2024
        #                             ''', style={'margin-top':'20px', 'color':'gray'}, className='font-family-default',
        #                         ),
        #                     ),
        #                 ]),
        #                 dbc.Row([
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### **1.**
        #                             ''', style={'margin-top':'20px', 'color':'lightgray'}, className='font-family-default',
        #                         )
        #                     ], width=1),
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                         '''
        #                             ###### **Developed interactive dashboard applications using Python:**
        #                         ''', style={'margin-top':'20px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                         dcc.Markdown(
        #                             '''
        #                                 - Project overview of chemical compounds.
        #                                 - Structure panel display of medicine candidates.
        #                                 - Data analysis facilitation of the experimental pipeline.
        #                                     - Batch effect analysis
        #                                     - DNA sequencing cost efficiency
        #
        #                             ''', style={'margin-top':'10px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                         dcc.Markdown(
        #                             '''
        #                                 ###### **This job gave me experience in:**
        #                             ''', style={'margin-top':'30px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                         dcc.Markdown(
        #                             '''
        #                                 - Collaborating with diverse stakeholders to gather project requirements and to bring development forward.
        #                                 - Understanding scientific problems and finding solutions.
        #                                 - Documenting software development projects.
        #                             ''', style={'margin-top':'10px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                     ], width=10)
        #                 ]),
        #                 dbc.Row([
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### **2.**
        #                             ''', style={'margin-top':'30px', 'color':'lightgray'}, className='font-family-default',
        #                         )
        #                     ], width=1),
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                         '''
        #                             ###### **Conducted collaborative projects with Amgen and the University of Copenhagen (including my MSc thesis):**
        #                         ''', style={'margin-top':'30px', 'color':'lightgray'}, className='font-family-default'
        #                         ),
        #                         dcc.Markdown(
        #                             '''
        #                                 - The project aimed to partition signal from noise in the DNA-encoded library (DEL) molecular screening process of a drug discovery pipeline.
        #                                 - I successfully applied statistical tools designed for data from differential gene expression experiments on data from DEL selection experiments.
        #                                 - This work was highly regarded, leading Amgen to plan for a postdoctoral position to continue the research.
        #                             ''', style={'margin-top':'10px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                         dcc.Markdown(
        #                         '''
        #                             ###### **These projects significantly enhanced my skills in:**
        #                         ''', style={'margin-top':'30px', 'color':'lightgray'}, className='font-family-default'
        #                         ),
        #                         dcc.Markdown(
        #                             '''
        #                                 - Data analysis and intuitive visualization.
        #                                 - Statistics and statistical programming in R.
        #                             ''', style={'margin-top':'10px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                     ], width=10),
        #                 ]),
        #               
        #                 dbc.Row([
        #                     dbc.Col(
        #                         dcc.Markdown(
        #                             '''
        #                                 #### Student Group
        #                             ''', style={'margin-top':'20px', 'color':'gray'}, className='font-family-default',
        #                         ),
        #                     ),
        #                     dbc.Col(
        #                         dcc.Markdown(
        #                             '''
        #                                 #### 02/2020 - 12/2022
        #                             ''', style={'margin-top':'20px', 'color':'gray'}, className='font-family-default',
        #                         ),
        #                     ),
        #                 ], style={'margin-top':'20px'}),
        #                 dbc.Row([
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 My main tasks in this role were the following:
        #                                 - Lab-waste management
        #                                 - Solvent preparation for lab instruments
        #                                 - Ordering lab supplies
        #                                 - Setting up office equipment and other handy tasks
        #
        #                                 I also contributed to two organizational projects in the laboratories:
        #                                 - Reorganizing and labeling toxic compounds to comply with up-to-date regulations.
        #                                 - Reorganizing and optimizing a big category of compound solutions stored in the laboratories. This simplified the retrieval of compounds for biologists and simultaneously made it easier for other student workers to place compound solutions back in place after use.
        #
        #                             ''', style={'margin-top':'10px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                     ], width=10)
        #                 ]),
        #
        #                 dbc.Row([
        #                     dbc.Col([
        #                         html.Br(),
        #                         dcc.Markdown(
        #                             '''
        #                                 ###### *_And many other work experiences such as bricklaying (3 years), gardening,\
        #                                 and working in a warehouse._*
        #                             ''', style={'margin-top':'10px', 'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                     ])
        #                 ], justify='center'),
        #                 html.Hr(),
        #             ], title='Work Experience'),
        #             dbc.AccordionItem([  # Education
        #                 html.Br(),
        #                 dbc.Row([
        #                     dbc.Col([
        #                         dbc.Row([
        #                             dbc.Col([
        #                                 html.Img(
        #                                     src='./assets/statics/icons8-graduate-30.png',
        #                                     height='40px'),
        #                             ], xs=2, sm=2, md=2, lg=2, xl=2),
        #                             dbc.Col([
        #                                 dcc.Markdown(
        #                                     '''
        #                                         #### University of Copenhagen
        #                                     ''', style={'margin':'5px 0px 0px 0px', 'display':'inline-block', 'color':'gray'}, className='font-family-default',
        #                                 ),
        #                             ], xs=10, sm=10, md=10, lg=10, xl=10),
        #                         ]),
        #                     ]),
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### MSc Bioinformatics
        #                                 ##### 2021 - 2024
        #                             ''', style={'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                     ], xs=12, sm=12, md=3, lg=3, xl=3),
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### BSc Biochemistry
        #                                 ##### 2016 - 2020
        #                             ''', style={'color':'lightgray'}, className='font-family-default',
        #                         ),
        #                     ], xs=12, sm=12, md=3, lg=3, xl=3)
        #                 ]),
        #                 dbc.Row([
        #                     html.Hr(style={'margin-top':'30px'}),
        #                     html.Br(),
        #                     dbc.Col([
        #                         html.Img(
        #                             src='./assets/statics/icons8-brick-64.png',
        #                             height='50px',
        #                         ),
        #                     ], xs=3, sm=3, md=1, lg=1, xl=1, align='center'),
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### Bricklayer Journeyman Certificate
        #                                 ##### 2011 - 2013
        #                             ''', style={'color':'lightgray', '':''}, className='font-family-default',
        #                         )
        #                     ], xs=9, sm=9, md=10, lg=10, xl=10, align='center')
        #                 ]),
        #             ], title='Education'),
        #             dbc.AccordionItem([  # Skills
        #                 dbc.Row([  # Programming experience
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### __Programming__ Experience
        #                             ''', style={'color':'gray'}, className='font-family-default',
        #                         ),
        #                         html.Br(),
        #                         dbc.Row([  # Python
        #                             dbc.Col([
        #                                 dcc.Markdown('''##### Python''', className='font-family-default'),
        #                             ], xs=4, sm=4, md=2, lg=2, xl=2),
        #                             dbc.Col([
        #                                 dcc.Markdown('''⭐⭐⭐⭐⭐'''),
        #                             ], width=3),
        #                             dbc.Col([
        #                                 dcc.Markdown(
        #                                 '''
        #                                     ###### Application development, statistics, data preprocessing and intuitive visualization.
        #                                 ''', style={'color':'lightgray'}, className='font-family-default',
        #                                 ),
        #                             ], xs=12, sm=12, md=7, lg=7, xl=7),
        #                         ], align='center', style={'margin-top':'20px', 'margin-bottom':'20px'}),
        #                         dbc.Row([  # R
        #                             dbc.Col([
        #                                 dcc.Markdown(
        #                                 '''
        #                                     ##### R
        #                                 ''', className='font-family-default',
        #                                 ),
        #                             ], xs=4, sm=4, md=2, lg=2, xl=2),
        #                             dbc.Col([
        #                                 dcc.Markdown('''⭐⭐⭐⭐'''),
        #                             ], width=3),
        #                             dbc.Col([
        #                                 dcc.Markdown(
        #                                 '''
        #                                     ###### Statistics, data preprocessing and intuitive visualization.
        #                                 ''', style={'color':'lightgray'}, className='font-family-default',
        #                                 ),
        #                             ], xs=12, sm=12, md=7, lg=7, xl=7),
        #                         ], align='center', style={'margin-top':'20px', 'margin-bottom':'20px'}),
        #                         dbc.Row([  # C++
        #                             dbc.Col([
        #                                 dcc.Markdown(
        #                                 '''
        #                                     ##### C++
        #                                 ''', className='font-family-default',
        #                                 ),
        #                             ], xs=4, sm=4, md=2, lg=2, xl=2),
        #                             dbc.Col([
        #                                 dcc.Markdown('''⭐⭐'''),
        #                             ], width=3),
        #                             dbc.Col([
        #                                 dcc.Markdown(
        #                                 '''
        #                                     ######  Passed course: NDAK14007U Applied Programming (7.5 ECTS)
        #                                 ''', style={'color':'lightgray'}, className='font-family-default',
        #                                 ),
        #                             ], xs=12, sm=12, md=7, lg=7, xl=7),
        #                         ], align='center', style={'margin-top':'20px', 'margin-bottom':'20px'}),
        #                     ]),
        #                 ]),
        #                 html.Hr(),
        #                 dbc.Row([
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                         '''
        #                             ##### Personal Qualities and Interests
        #                         ''', style={'color':'gray'}, className='font-family-default',
        #                         ),
        #                         dbc.Row([
        #                             dbc.Col([
        #                                 dcc.Markdown(
        #                                     '''
        #                                         #### Teamwork
        #                                         ###### **&middot;** Happily brainstormed solutions whenever a colleague was stuck on a problem.
        #                                         ###### **&middot;** Repeatedly demonstrated willingness to work extra hours to complete tasks others had to leave unfinished.
        #                                         ###### **&middot;** Guided new student employees patiently through tasks ensuring a thorough understanding of their responsibilities while listening to questions without interrupting.
        #                                         ###### **&middot;** Documented detailed protocols for every reoccurring task to simplify the training of the next employee.
        #                                     ''', style={'color':'lightgray'}, className='font-family-default',
        #                                 ),
        #                                 dcc.Markdown(
        #                                     '''
        #                                         #### Autonomous and creative problem solver
        #                                         ###### **&middot;** Scheduled meetings with stakeholders when a prototype was ready and an idea needed to be discussed.
        #                                         ###### **&middot;** Took initiative and suggested creative ways forward when the best solution was less obvious.
        #                                         ###### **&middot;** Remained focused on the objective both when working on-site and remotely.
        #                                     ''', style={'margin-top':'40px', 'color':'lightgray'}, className='font-family-default',
        #                                 ),
        #                                 dcc.Markdown(
        #                                     '''
        #                                         #### Intercultural agility
        #                                         ###### **&middot;** Actively reflecting on how to turn cultural differences into problem-solving strengths,\
        #                                         by understanding how we may interpret problems differently, and therefore disagree on solutions.
        #                                     ''', style={'margin-top':'40px', 'color':'lightgray'}, className='font-family-default',
        #                                 ),
        #                                 dcc.Markdown(
        #                                     '''
        #                                         ##### **&middot;** **Mountain hiking** **&middot;** **Financial investing** **&middot;** **Philosophy**\
        #                                         **&middot;** **River fishing** **&middot;** **Winterbathing and sauna**
        #                                     ''', style={'margin-top':'40px', 'color':'lightgray'}, className='font-family-default',
        #                                 ),
        #                                 dcc.Markdown(
        #                                     '''
        #                                         ###### I grew up skiing, fishing and hiking in the norwegian mountains. I absolutely love it and spend most of my vacation days in nature. 
        #                                         ###### I am also fond of winter bathing and sauna-use. Nothing beats the relaxing feeling after a sauna struggle followed by a cold plunge.
        #                                     ''', style={'color':'lightgray'}, className='font-family-default',
        #                                 )
        #                             ], width=12)
        #                         ], justify='center', align='center'),
        #                     ]),
        #                 ], justify='center')
        #             ], title='Skills'),
        #             dbc.AccordionItem([  # Languages
        #                 dbc.Row([
        #                     dbc.Col([
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### &#9900 **Norwegian** (Native)
        #                             ''', style={'display':'inline-block', 'color':'lightgray', 'margin':'20px'}, className='font-family-default',
        #                         ),
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### &#9900 **English** (fluent)
        #                             ''', style={'display':'inline-block', 'color':'lightgray', 'margin':'20px'}, className='font-family-default',
        #                         ),
        #                         dcc.Markdown(
        #                             '''
        #                                 ##### &#9900 **Danish** (fluent)
        #                             ''', style={'display':'inline-block', 'color':'lightgray', 'margin':'20px'}, className='font-family-default',
        #                         ),
        #                         html.Br(),
        #                     ], style={'margin':'0px', 'padding':'0px'})
        #                 ], justify='center', align='start')
        #             ], title='Languages'),
        #         ], start_collapsed=True, flush=True),
        #     ], width=10),
        # ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Hr(),
                dcc.Markdown(
                    '''
                       ###### Take a look at my projects to see what I have been working on lately &#129312;
                    ''', style={'color':'lightgray'}, className='font-family-default',
                ),
            ]),
        ]),
    ], fluid=True)
#--- End Layout

    # Callback for download CV
@callback(
    dash.Output("download-cv", "data"),
    dash.Input("btn-download-cv", "n_clicks"),
    prevent_initial_call=True,
)
def download_cv(n_clicks):
    return dcc.send_file("./assets/cv_andreas_sandnes.pdf")



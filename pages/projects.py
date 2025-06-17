# Imports
from utils.third_party import pd,\
    dash, dbc, html, dcc, dag, Output, Input, State, PreventUpdate, no_update, callback
from utils.local_imports import structure_display
from utils.local_imports.fetch_pubchem_data import fetch_pubchem_data
from pages.sidebar import sidebar


# Page registration
dash.register_page(
    __name__,
    path='/projects',
    location='navbar',
    description='',
    order=1,
)

#--- Begin layout
def layout():
    return dbc.Container([
        dbc.Row([  # Search-bar, Radio-items
            dbc.Col([
                dbc.Row([  # sidebar
                    dbc.Col([sidebar()], width=12, style={'padding':'0px'}),
                ]),
                html.Br(),
                dbc.Row([  # titles
                    dbc.Col([
                        html.Br(),
                        dcc.Markdown(
                            '''
                                ## Need to extract data from PubChem? Look no further!
                            ''',
                            style={'color':'lightgray'},
                            className='font-family-default',
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                                ### By using the PubChemPy package in Python,\
                                this website fetches the data you need and teaches you the origin story of your favourite molecules!
                            ''',
                            style={'color':'lightgray'},
                            className='font-family-default',
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                                #### Fill in your search query and hit search to get started.
                            ''',
                            style={'color':'lightgray'},
                            className='font-family-default',
                        ),
                        html.Br(),
                    ], className='bg-dark', style={'border-radius':'10px'}),
                ], justify='center'),
                html.Br(),
                html.Hr(),
                dbc.Row([  # buttons
                    dbc.Col([
                        # Search Input Box
                        dcc.Input(
                            id="search-bar",
                            type="text",
                            value='',
                            placeholder="e.g., glucose insulin",
                            n_submit=0,                      
                        ),
                        # Search Button
                        html.Button(
                            "Search",
                            id="search-button",
                            className='button-click',
                        ),
                        dcc.Loading(
                            id='datatable-loader',
                            children=[],
                            overlay_style={'visibility':'visible', 'filter': 'blur(4px)'},
                            type="circle",
                            style={'margin':'0px 0px 90px 275px'}
                        ),
                    ], width=8, align='center'),
                    dbc.Col([
                        html.Button(
                            "Project Documentation",
                            id="see-docs-button",
                            className='button-click',
                        ),
                        dbc.Modal(
                            id='doc-modal',
                            children=[],
                            is_open=False,
                        ),
                    ], width=4, align='center', style={'text-align':'right'}),
                ]),
                dbc.Row([  # radio-buttons
                    dbc.Col([
                        dcc.Markdown(''' ##### Search by ''', className='font-family-default', style={'display':'inline-block', 'color':'lightgray', 'margin-right':'20px'}),
                        dcc.RadioItems(
                            id="search-types",
                            options=[  # Could be made dynamic
                                {"label": "Name", "value": "name"},
                                {"label": "SMILES", "value": "smiles"},
                                {"label": "SDF", "value": "sdf"},
                                {"label": "InChI", "value": "inchi"},
                                {"label": "InChIKey", "value": "inchikey"},
                                {"label": "Formula", "value": "formula"},
                            ],
                            value="name",  # Default value
                            labelStyle={"display": "inline-block", "margin-right": "20px"},
                            style={'display':'inline-block'}
                        ),
                    ], width=8),
                    dbc.Col([
                        html.A(
                            "GitLab Repository",
                            href="https://gitlab.com/ansandnes/asandnes_dash_portfolio",
                            target='_blank',
                            style={"textDecoration": "none", "border-bottom":"solid"},
                        ),
                        # html.Button(
                        #     ".. will take you to the GitLab repo",
                        #     id="see-code-button",
                        #     className='button-click',
                        # ),
                        html.Br(),
                        html.Br(),
                    ], width=4, style={'text-align':'right'}),
                ]),
                dbc.Row([  # alert
                    dbc.Col([
                        dbc.Alert(
                            id='empty-search-alert',
                            children=[
                                'Fill in your search query to find what you\
                                are looking for (e.g., glucose insulin).'
                            ],
                            dismissable=True,
                            color='#007BFF',  # Same blue as button
                            style={'display':'none'},
                        ),
                    ], xs=12, sm=12, md=8, lg=8, xl=8, xxl=8),
                ]),
            ]),
        ]),
        dbc.Row([  # Dropdown
            dbc.Col([
                html.Br(),
                dcc.Markdown('''#### Select the data you need and hit the search button''', className='font-family-default', style={'color':'darkgray'}),
                dcc.Dropdown(
                    id="data-extract-dropdown",
                    options=[  # Could be made dynamic. Atoms and Bonds is not JSON serializable
                        {'label': 'ATOM_STEREO_COUNT', 'value': 'atom_stereo_count'},
                        # {'label': 'ATOMS', 'value': 'atoms'},  # fix bug
                        {'label': 'BOND_STEREO_COUNT', 'value': 'bond_stereo_count'},
                        # {'label': 'BONDS', 'value': 'bonds'},  # fix bug
                        {'label': 'CACTVS_FINGERPRINT', 'value': 'cactvs_fingerprint'},
                        {'label': 'CANONICAL_SMILES', 'value': 'canonical_smiles'},
                        {'label': 'CHARGE', 'value': 'charge'},
                        {'label': 'COMPLEXITY', 'value': 'complexity'},
                        {'label': 'CONFORMER_ID_3D', 'value': 'conformer_id_3d'},
                        {'label': 'CONFORMER_RMSD_3D', 'value': 'conformer_rmsd_3d'},
                        {'label': 'COORDINATE_TYPE', 'value': 'coordinate_type'},
                        {'label': 'COVALENT_UNIT_COUNT', 'value': 'covalent_unit_count'},
                        {'label': 'DEFINED_ATOM_STEREO_COUNT', 'value': 'defined_atom_stereo_count'},
                        {'label': 'DEFINED_BOND_STEREO_COUNT', 'value': 'defined_bond_stereo_count'},
                        {'label': 'EFFECTIVE_ROTOR_COUNT_3D', 'value': 'effective_rotor_count_3d'},
                        {'label': 'ELEMENTS', 'value': 'elements'},
                        {'label': 'EXACT_MASS', 'value': 'exact_mass'},
                        {'label': 'FEATURE_SELFOVERLAP_3D', 'value': 'feature_selfoverlap_3d'},
                        {'label': 'FINGERPRINT', 'value': 'fingerprint'},
                        {'label': 'H_BOND_ACCEPTOR_COUNT', 'value': 'h_bond_acceptor_count'},
                        {'label': 'H_BOND_DONOR_COUNT', 'value': 'h_bond_donor_count'},
                        {'label': 'HEAVY_ATOM_COUNT', 'value': 'heavy_atom_count'},
                        {'label': 'INCHI', 'value': 'inchi'},
                        {'label': 'INCHIKEY', 'value': 'inchikey'},
                        {'label': 'ISOMERIC_SMILES', 'value': 'isomeric_smiles'},
                        {'label': 'ISOTOPE_ATOM_COUNT', 'value': 'isotope_atom_count'},
                        {'label': 'IUPAC_NAME', 'value': 'iupac_name'},
                        {'label': 'MMFF94_ENERGY_3D', 'value': 'mmff94_energy_3d'},
                        {'label': 'MMFF94_PARTIAL_CHARGES_3D', 'value': 'mmff94_partial_charges_3d'},
                        {'label': 'MOLECULAR_FORMULA', 'value': 'molecular_formula'},
                        {'label': 'MOLECULAR_WEIGHT', 'value': 'molecular_weight'},
                        {'label': 'MONOISOTOPIC_MASS', 'value': 'monoisotopic_mass'},
                        {'label': 'MULTIPOLES_3D', 'value': 'multipoles_3d'},
                        {'label': 'PHARMACOPHORE_FEATURES_3D', 'value': 'pharmacophore_features_3d'},
                        {'label': 'RECORD', 'value': 'record'},
                        {'label': 'ROTATABLE_BOND_COUNT', 'value': 'rotatable_bond_count'},
                        {'label': 'SHAPE_FINGERPRINT_3D', 'value': 'shape_fingerprint_3d'},
                        {'label': 'SHAPE_SELFOVERLAP_3D', 'value': 'shape_selfoverlap_3d'},
                        {'label': 'TPSA', 'value': 'tpsa'},
                        {'label': 'UNDEFINED_ATOM_STEREO_COUNT', 'value': 'undefined_atom_stereo_count'},
                        {'label': 'UNDEFINED_BOND_STEREO_COUNT', 'value': 'undefined_bond_stereo_count'},
                        {'label': 'VOLUME_3D', 'value': 'volume_3d'},
                        {'label': 'XLOGP', 'value': 'xlogp'},
                    ],
                    value=['isomeric_smiles', 'iupac_name', 'molecular_formula', 'exact_mass', 'molecular_weight'],  # Default selected values (empty initially)
                    multi=True,  # Allows selecting multiple options
                    placeholder="Select options...",
                ),
            ]),
        ]),
        dbc.Row([  # Datatable
            dbc.Col([  # AgGrid datatable
                html.Br(),
                dag.AgGrid(
                    id='compound-datatable',
                    columnDefs = [],
                    rowData = [],
                    style={'display':'none', 'height':'200px'},
                    dashGridOptions={'pagination': False},
                    # columnSize='responsiveSizeToFit',
                ),
            ], xs=12, sm=12, md=12, lg=12, xl=12),
        ], justify='center'),
        dbc.Row([  # 2D Structure
            dbc.Col([  # RDKit Structure Display
                html.Br(),
                dcc.Markdown('''#### 2D Structure and a casual origin story''', id='structure-title', className='font-family-default', style={'display':'none', 'color':'darkgray'}),
                dcc.Loading(
                            id='ai-loader',
                            children=[],
                            overlay_style={'visibility':'visible', 'filter': 'blur(2px)'},
                            type="circle",
                            style={'margin':'0px 400px 40px 0px'}
                        ),
                html.Div(
                    id='2d-structure',
                    children=[],  # filled by callback
                ),
                html.Br(),
                html.Br(),
                dcc.Markdown(
                    '''###### Remember that AI models could be wrong.\
                    Please take these short origin stories with a grain of salt. ''',
                    id='ai-note', className='font-family-default', style={'display':'none', 'color':'darkgray'},
                ),
                html.Br(),
                html.Br(),
            ], xs=12, sm=12, md=12, lg=12, xl=12),
        ], justify='center'),
    ])
#--- End layout

# Callbacks
@callback(
    [
        Output(component_id='compound-datatable', component_property='columnDefs'),
        Output(component_id='compound-datatable', component_property='rowData'),
        Output(component_id='empty-search-alert', component_property='style'),
        Output(component_id='datatable-loader', component_property='children'),
    ],
    [
        Input(component_id='search-button', component_property='n_clicks'),
        Input(component_id='search-button', component_property='n_submit'),
    ],
    [
        State(component_id='search-bar', component_property='value'),
        State(component_id='search-types', component_property='value'),
        State(component_id='data-extract-dropdown', component_property='value'),
    ],
    prevent_initial_callback=True,
)
def get_data(n_clicks, enter, search_value, search_type, cols):
    '''
        Trigger: search-button or enter is pressed
        Input: Users search string, chosen search type
        Output: Data from PubChem
    '''
    
    #|----------------------------------------------------|#
    if n_clicks is None: raise PreventUpdate
    if cols is None or '': raise PreventUpdate
    if search_type is None: raise PreventUpdate
    if search_value is None or search_value == '':
        return [no_update, no_update, {'display':'block'}, None] 
    #|----------------------------------------------------|#
    
    compound_list = str(search_value).split(sep=' ')  # Create a list of compounds from search query
    data_fields = cols  # Create a list of data fields to extract from PubChem

    # Create dataframe containing the data from search query
    try:
        df = fetch_pubchem_data(compound_list=compound_list, data_fields=data_fields)
    except Exception as e:
        print(f"Error fetching data for df: {e}")

    # Define outputs for the datatable
    try:
        columnDefs = [{'field': i, 'headerName':str(i).upper()} for i in df.columns]
    except Exception as e:
        print(f"Error fetching data for columnDefs: {e}")
    try:
        rowData = df.to_dict('records')
    except Exception as e:
        print(f"Error fetching data for rowData: {e}")

    return [columnDefs, rowData, {'display':'none'}, None]


@callback(
    [
        Output(component_id='2d-structure', component_property='children'),
        Output(component_id='ai-loader', component_property='children'),
    ],
    [
        Input(component_id='compound-datatable', component_property='rowData'),
    ],
    prevent_initial_call=True,
)
def draw_structure(rowData):
    """  """

    #|----------------------------------------------------|#
    if rowData is None: raise PreventUpdate
    #|----------------------------------------------------|#

    df = pd.DataFrame(rowData)
    smiles = list(df['isomeric_smiles'])
    compounds = list(df['Compound'])
    list_of_img = structure_display.draw_2d_structure(smiles, compounds)

    return [html.Div(children=list_of_img), None]


@callback(
[
    Output(component_id='compound-datatable', component_property='style'),
    Output(component_id='structure-title', component_property='style'),
    Output(component_id='ai-note', component_property='style'),
],
[
    Input(component_id='search-button', component_property='n_clicks'),
],
prevent_initial_call=True,
)
def hide_empty_components(n_clicks):
    """ Hide empty components """
    if n_clicks > 0:
        compound_datatable_style={'display':'inline-block', 'height':'200px'}
        structure_title_style={'display':'inline-block', 'color':'darkgray'}
        ai_note_style={'display':'inline-block', 'color':'darkgray'}
        return [compound_datatable_style, structure_title_style, ai_note_style]
    

@callback(
    [
        Output(component_id='doc-modal', component_property='children'),
        Output(component_id='doc-modal', component_property='is_open'),
    ],
    [Input(component_id='see-docs-button', component_property='n_clicks')],
    prevent_initial_call=True,
)
def open_modal(n_clicks):
    """  """
    if n_clicks:
        return [[
            dbc.ModalHeader(dbc.ModalTitle("Documentation")),
            dbc.ModalBody([
                dcc.Markdown(
                    '''
                        #### Project Description
                    ''', className='font-family-default', style={'display':'inline-block', 'color':'lightgray'},
                ),
                html.Br(),
                html.Br(),
                dcc.Markdown(
                    '''
                        ##### I did this project because I wanted to learn how to implement AI tools in a web app using APIs and Python.
                    ''', className='font-family-default', style={'display':'inline-block', 'color':'lightgray'},
                ),
                html.Br(),
                html.Br(),
                dcc.Markdown(
                    '''
                        ##### The result is a web-based tool that enables users to search for molecular compounds available in the PubChem database using a search bar interface.\
                        The application connects to the PubChem database through the PubChemPy package, allowing users to easily fetch relevant data about various chemical compounds\
                        and display it in an AgGrid datatable. The chemical structure is the drawn by RDKit and is displayed in a 2D representation together with an AI generated origin story about the compound.
                    ''', className='font-family-default', style={'display':'inline-block', 'color':'lightgray'},
                ),
                html.Br(),
                html.Br(),
                dcc.Markdown(
                    '''
                        ##### Technologies Used
                        ###### Python version 3.10.14
                        ###### dash==2.17.1
                        ###### pubchempy==1.0.4
                        ###### ag-grid==23.1.0
                        ###### rdkit==2024.03.5
                        ###### Gemini 1.5 Flash
                    ''', className='font-family-default', style={'display':'inline-block', 'color':'lightgray'},
                ),
            ]),
            dbc.ModalFooter(
                dcc.Markdown(
                    '''
                        ##### This project offers a practical solution for exploring chemical compounds while also adding educational and storytelling elements to enhance the user experience.
                    ''', className='font-family-default', style={'display':'inline-block', 'color':'lightgray'},
                ),
            ),
        ],True]
        #-------------|
    


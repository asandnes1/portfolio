# Imports
from utils.third_party import dash, dbc, html

def sidebar() -> dbc.Nav:
    """  """
    nav_links=[]
    for page in dash.page_registry.values():
        if page['path'].startswith('/app'):
            nav_links.append(
                dbc.NavLink([
                        html.Div(page['name'], style={'text-align':'center', 'color':'lightgray'}, className='font-family-default font-weight-subtitle'),
                ], href=page['path'], active='exact')
            )
        elif page['path']=='/projects':
            nav_links.append(
                dbc.NavLink([
                    html.Div('App1', style={'text-align':'center', 'color':'lightgray'}, className='font-family-default font-weight-subtitle'),
                ], href=page['path'], active='exact')
            )
    return dbc.Nav(
        children=nav_links,
        vertical=False,
        pills=True,
        className='bg-dark',
    )


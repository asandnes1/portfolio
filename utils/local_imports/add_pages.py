# """
# This is a function that adds pages to the app
# that are registered in the page registry.
# """
# # File imports
# from utils.third_party import dash, dbc


# def add_pages() -> dbc.Nav:
#   """ Returns a list of page objects """
#   return dbc.Nav(
#     [
#       dbc.NavLink(f"{page['name']}", href=page['path'])
#       for page in dash.page_registry.value()
#       if not page['path'].startswith('/app')
#     ]
#   )

# # This function is not in use.


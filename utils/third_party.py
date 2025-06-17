# Third party imports

# Data processing imports
import pandas as pd
# import polars as pl
import numpy as np

# # Database imports
# import oracledb

# Dash Plotly imports
import dash
from dash import Dash, html, dcc, callback, Output, Input, State, no_update
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
# import dash_bio as dashbio
# from dash_bootstrap_templates import load_figure_template

# RDKit imports
from rdkit.Chem import MolFromSmiles
from rdkit.Chem.rdDepictor import Compute2DCoords, StraightenDepiction
from rdkit.Chem.Draw import MolDraw2DSVG
# from rdkit.Chem.Draw import IPythonConsole

# PubChemPy imports
from pubchempy import get_compounds

# Gemini imports
import google.generativeai as genai
from dotenv import load_dotenv

# # PyDeseq2 imports
# from pydeseq2.ds import DeseqStats

# # Import modules needed for creating PowerPoint slides
# import pptx


# This file contains functions related to the structure display

# Imports
from utils.third_party import MolDraw2DSVG, html, dbc, dcc, genai, MolFromSmiles, Compute2DCoords, StraightenDepiction, load_dotenv
from utils.built_in import os, b64encode


# Function that creates a structure image
def show_mol(drawer, mol, legend:list[str]) -> str:
    """
        Description: Takes a drawer-, and a mol object, and a list if legends and returns an image src.
        Args: drawer (rdkit.Chem.Draw.rdMolDraw2D.MolDraw2DSVG), mol (rdkit.Chem.rdchem.Mol), legend (list of strings).
        Returns: A src string (like: f"data:image/svg+xml;base64,{svg_base64}")
    """
    # Draw structure
    try:
        drawer.DrawMolecule(mol, legend=legend)
    except Exception as e:
        print('Error in show_mol when using DrawMolecule:', e)
    try:
        drawer.FinishDrawing()
    except Exception as e:
        print('Error in show_mol when using FinishDrawing:', e)
    
    # Convert svg string to byte-like object
    try:
        svg_string = drawer.GetDrawingText()
    except Exception as e:
        print('Error when getting svg string:', e)
    
    # Encode the svg string as base64
    try:
        svg_base64 = b64encode(svg_string.encode("utf-8")).decode("utf-8")
    except Exception as e:
        print('Error in show_mol when converting svg string to byte-like object:', e)

    src = f"data:image/svg+xml;base64,{svg_base64}"
    
    return src


# Function that generates AI text
def ai_output(compound:str) -> str:
    """
    Description: Takes a compound name and generates a casual origin story about the compound using AI.

    Args:
        compound (str): Compound name (e.g., 'glucose']).

    Returns:
        Text (str): An AI generated text.
    """
    # Authenticate with API key
    load_dotenv(dotenv_path="./../.env")  # Read your API Key from your .env file
    api_key = os.getenv("GENAI_API_KEY")  # Load the API key

    if api_key is None:
        raise Exception("API key not set! Make sure API_KEY environment variable is defined.")
    else:
        genai.configure(api_key=api_key)
    #---
    # Choose AI model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Create an interesting, funny and factual text about the compounds of interest
    try:
        response = model.generate_content(
            f"Write a 8-line educational and interesting history summary of {compound}.\
            Think of it as a documentary about the compound,\
            from its humble beginnings to its present-day uses.\
            Don't be afraid to get silly and make light of its sometimes-strange origins.\
            Ensure it is factual, and use a conversational tone."
        )
        response = response.text
    except Exception as e:
        response = 'The AI prompt was flagged as a safety concern. No origin story was generated.'
        print('Error when generating AI response:', e)
    return response


# Function that draws a 2d structure using RDKit
def draw_2d_structure(list_of_smiles:list, compounds:list) -> list:
    """
    Draw the 2D structure of a molecule\
    from a list of SMILES string(s) using RDKit.

    Args:
        list_of_smiles (list of str): List of SMILES strings representing compounds.

    Returns:
        List of images: RDKit 2D structure image objects of the compounds.
    """

    list_of_img = []
    for i in range(len(list_of_smiles)):
        try:
            # Generate RDKit molecule from SMILES string
            try :
                mol = MolFromSmiles(list_of_smiles[i])
                if mol is None:
                    raise ValueError(f"Mol object is type None: {list_of_smiles[i]}")
            except Exception as e:
                print('Error when generating Mol object from smiles:', e)
            
            # Compute 2D coordinates for the molecule
            try:
                Compute2DCoords(mol)
            except Exception as e:
                print('Error when computing 2D coordinates:', e)
            
            # Optionally straighten depiction (can improve aesthetics)
            try:
                StraightenDepiction(mol)
            except Exception as e:
                print('Error when straightening depiction:', e)

            # Set drawing options
            try:
                # Create drawer object
                drawer = MolDraw2DSVG(300, 300)
                dopts = drawer.drawOptions()
                # Set options
                dopts.setBackgroundColour((0.95, 0.95, 0.95, 1))  # Set background color
                dopts.setLegendColour((0.5, 0.5, 0.5, 1))  # Set legend color
            except Exception as e:
                print('Error when setting options:', e)

            # Create the image object
            try:
                img = show_mol(drawer, mol, compounds[i])
            except Exception as e:
                print('Error when creating src string using show_mol:', e)

            # Wrap the img in dbc elements
            try:
                image_text_row = \
                    dbc.Row([
                        dbc.Col([
                            html.Img(src=img, style={'border-radius':'5%'}),
                        ], xs=10, sm=10, md=4, lg=4, xl=4,
                        style={'display':'block', 'margin':'10px'}),
                        dbc.Col([
                            dcc.Markdown(
                                '''###### Text generated by the gemini-1.5-flash AI model''',
                                style={'margin-top':'20px', 'color':'lightgray'},
                                className='font-family-default',
                            ),
                            html.Div(
                                ai_output(str(compounds[i])),
                                className='default-font-family',
                            ),
                            html.Button(
                                'expand structure',
                                id='expand-image-button',
                                className='button-click',
                                style={'display':'none', 'margin':'20px 20px 20px 0px'}
                            ),
                        ], xs=10, sm=10, md=6, lg=6, xl=6),
                        html.Hr(),
                    ], justify='center')
            except Exception as e:
                print('Error when wrapping image in dbc elements:', e)
            
            # Appending image to list
            try:
                list_of_img.append(image_text_row)
            except Exception as e:
                print('Error when appending image to list of images:', e)

        except Exception as e:
            print(f"Error occurred when drawing the 2D structure of smiles: {i}: {e}")
            return [dcc.Markdown(
                '''###### Something went wrong in the drawing process. No results are shown.''',
                style={'margin-top':'20px', 'color':'lightgray'},
                className='font-family-default',
            ),]
    
    return list_of_img
    #-------------------------------------------------------------------|


# This file contains the definition of the fetch_pubchem_data function

# Imports
from utils.third_party import pd, get_compounds


# Function used for data extraction for search-bar queries
def fetch_pubchem_data(compound_list:list[str], data_fields:list[str]) -> pd.DataFrame:
    """
    Fetch compound data from PubChem using PubChemPy and return as a Pandas DataFrame.

    Args:
        compound_list (list of str): List of compound names or identifiers (e.g., ['glucose', 'insulin']).
        data_fields (list of str): List of specific data fields to retrieve (e.g., ['molecular_weight', 'isomeric_smiles']).

    Returns:
        pd.DataFrame: A pd.DataFrame containing the requested data fields for each compound.
    """
    # Add isomeric_smiles to data_fields if not present.
    # The structure callback depends on it.
    if 'isomeric_smiles' not in data_fields:
        data_fields.append('isomeric_smiles')
    
    # Initialize an empty list to store the results
    data = []
    for compound in compound_list:
        try:
            # Fetch the compound from PubChem
            c = get_compounds(compound, 'name')

            # If a compound is found, extract the requested data fields
            if c:
                compound_data = {"Compound": compound}
                for field in data_fields:
                    compound_data[field] = getattr(c[0], field, None)
                data.append(compound_data)
            else:
                # If no compound found, append None for each field
                compound_data = {"Compound": compound}
                for field in data_fields:
                    compound_data[field] = None
                data.append(compound_data)

        except Exception as e:
            # Handle any errors and append None for the compound's data
            compound_data = {"Compound": compound}
            for field in data_fields:
                compound_data[field] = None
            data.append(compound_data)
            print(f"Error fetching data for {compound}: {e}")

    # Create a DataFrame from the collected data
    df = pd.DataFrame(data)

    return df


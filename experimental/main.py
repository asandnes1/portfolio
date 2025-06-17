
# pyscript imports
# from utils.built_ins import display
from pyscript import display

# Third party imports
import pandas as pd
import matplotlib.pyplot as plt
# from utils.third_party import *



# python_output = "Hello World"
df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

fig, ax = plt.subplots()
ax.scatter(df["col1"], df["col2"])



display(fig, target="python_output", append=False)


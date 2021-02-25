# IPOArbitrage

![](Images/IPO_arbitrage_image.jpg)

In this application we will analyze stock performance from 5 companies that recently went public along over a 30 day period. We will calculate their daily returns, cumulative returns, and variance of each stock. In addition to this we will compare 5 currencies to determine if arbitrage exists for the same 30 day period. If arbitrage does exist we will determine which companies offer the best opportunity for foreign investors from those countries. An interactive user application will be able to prompt users to select which company and currency they would be interested to invest in and advise whether or not it is worth it to invest in that company. 

---

## Technologies

This project uses a Jupyter Notebook in Jupyter Lab to analyze the stock performance of the 5 companies and visualize the returns during the 30 day period. A python file will also be used for the interactive user application and to build the functions related to the user story.

- Questionary: for the interactive user interface that will ask an investor how they would like to invest. 
- Pandas: to help with the robust amount of features that will help analyze and organize the data.
- Path: to extract and read the data from the CSV files using the file paths.
- Plotly Express: to create interactive maps for our geospatial data.
- PyViz & hvPlot: to create interactive data visualizations that are visually pleasing to the audience.
- Holoviews: used as the new python library for additional visualizations.

---

## Installation

```
pip install questionary
```

```
conda install -c plotly plotly=4.13.
conda install -c pyviz hvplot
```

JupyterLab extentions so that the plots will render in JupyterLab:
```
jupyter labextension install jupyterlab-plotly@4.13.0
jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.13.0
jupyter labextension install @pyviz/jupyterlab_pyviz
```

```
jupyter lab build
```

```
pip install holoviews
```

---

## Usage

To succesfully run this notebook, please be sure to import the required libraries and dependencies:

```
import pandas as pd
from pathlib import Path
import hvplot.pandas
import holoviews as hv
from holoviews import opts
import questionary
```

---

## Contributors

Aye Oo, Callie Yu, Fatimah Hasan, and Michael Husary were the main contributer for this project. The educational staff also assisted in pointing us in the right direction. 

--- 

## License
*(Not sure if a license was required on this Challenge)*


MIT

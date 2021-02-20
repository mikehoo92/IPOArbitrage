# IPOArbitrage

In this application we will analyze stock performance from 5 companies that recently went public along over a 30 day period. We will calculate their daily returns, ......  In addition to this we will compare 5 currencies to determine if arbitrage exists for the same 30 day period. If arbitrage does exist we will determine which companies offer the best opportunity for foreign investors from those countries. An interactive user application will be able to prompt users to select which company and currency they would be interested to invest in and advise whether or not it is worth it to invest in that company. 

![](Images/IPO_arbitrage_image.jpg)

---

## Technologies

This project uses a Jupyter Notebook in Jupyter Lab to analyze the stock performance of the 5 companies and visualize the returns during the 30 day period. A python file will also be used for the interactive user application and to build the functions related to the user story.

- Pandas: to help with the robust amount of features that will help analyze and organize the data.
- Path: to extract and read the data from the CSV files using the file paths.
- Plotly Express: to create interactive maps for our geospatial data.
- PyViz & hvPlot: to create interactive data visualizations that are visually pleasing to the audience.


---

## Usage

To succesfully run this notebook, please be sure to import the required libraries and dependencies:

```
import plotly.express as px
import pandas as pd
from pathlib import Path
import hvplot.pandas
```

---

## Contributors

Aye Oo, Callie Yu, Fatimah Hasan, and Michael Husary were the main contributer for this project. The educational staff also assisted in pointing us in the right direction. 

--- 

## License
*(Not sure if a license was required on this Challenge)*


MIT
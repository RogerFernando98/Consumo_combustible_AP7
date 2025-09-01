# Run in terminal (IF NEEDED)

#pip install geopy
#pip install ipykernel
#pip install matplotlib
#pip install numpy
#pip install pandas
#pip install plotly
#pip install scikit-learn
#pip install seaborn

import pandas as pd
pd.DataFrame.iteritems = pd.DataFrame.items
from typing import List
from datetime import datetime
from dateutil import relativedelta

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from scipy.spatial.distance import cdist

import pandas as pd
from scipy.spatial import KDTree
from geopy.distance import geodesic
from datetime import timedelta




# Load data

PATH = 'Data_Part1_Datathon.csv'
df = pd.read_csv(PATH)

print(df.head())

PATH2 = 'Data_Part2_APG_Datathon.csv'
df2 = pd.read_csv(PATH2)

print(df2.head())
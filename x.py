
import pandas as pd

import matplotlib.pyplot as plt
import missingno as msno
df=pd.read_csv("Dataset_API/dataset_function_API.csv")## Load dataset from ETL analysis
msno.bar(df.sample(1000),labels=True)

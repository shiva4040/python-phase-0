# Mini: Load any CSV (Titanic on Kaggle is free). Print basic stats.
import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.head())
print(df.shape)
df.info()
print(df.describe())

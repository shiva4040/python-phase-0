# Mini: Find average survival rate by gender and class in Titanic dataset.
import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.groupby(["Sex", "Pclass"])["Survived"].mean().reset_index())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")
# plt.plot(df.head()["Age"])
# plt.bar(df.head().index, df.head()["Pclass"])
# plt.title("bar")
# plt.xlabel("Pasanger")
# plt.ylabel("Pclass")
# plt.show()
# plt.scatter(df.head().index ,df.head()["Pclass"])
# plt.title("sctter")
# plt.show()
# plt.hist(df.head()["Pclass"])
# plt.title("hist")
# plt.show()
# plt.pie(df.head()["Pclass"])
# plt.title("pie")
# plt.show()
# sns.lineplot(data = df , x = "Age", y = "Pclass")
# plt.show()

# sns.lineplot(x = df.head().index, y = df.head()["Age"] )
# plt.title("plotline")
# plt.show()
# sns.barplot(x = df.head().index, y = df.head()["Pclass"])
# plt.title("Barplot")
# plt.show()
# sns.scatterplot(df.head()["Age"])
# plt.title("Scatter")
# plt.show()
# sns.histplot(df.head().index)
# plt.title("Histplot")
# plt.show()
# sns.boxplot(x = df.head().index, y = df.head()["Age"])
# plt.title("Boxplot")
# plt.show()
# sns.countplot(x = df.head().index)
# plt.title("Countplot")
# plt.show()

#Mini: Plot age distribution + survival heatmap from Titanic data.
sns.histplot(df["Age"])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("count")
plt.show()

heatmap_data = df.groupby(["Sex", "Pclass"])["Survived"].mean().unstack()
sns.heatmap(heatmap_data,
            annot = True,
            cmap = "YlGnBu",
            fmt = ".2f")
plt.show()
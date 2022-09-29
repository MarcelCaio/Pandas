
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Gapminder.csv", error_bad_lines=False, sep=";")

#Visualizando as 5 primeiras linhas
df.head()

df = df.rename(columns={"country" : "Pais", "continent" : "Continente", "year" : "Ano", "lifeExp" : "Expectativa de Vida", "pop" : "Populacao", "gdpPercap" : "PIB"})

df.head(10)

#Total de linhas e colunas
df.shape

df.columns

df.dtypes

df.tail()

df.tail(15)

df.describe()

df["Continente"].unique()

oceania = df.loc[df["Continente"] == "Oceania"]
oceania.head()

df.groupby("Continente")["Pais"].nunique()

df.groupby("Ano")["Expectativa de Vida"].mean()

df["PIB"].mean()

df["PIB"].sum()


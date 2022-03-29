# Project  -  Analysing Iris Dataset
# Author: Renan Riva

import pandas as pd
from sympy import false

iris_df = pd.read_csv('iris.csv')


#Adding headers to the collums using the attribut information on "https://archive.ics.uci.edu/ml/datasets/iris". To make clear what each column represent.
list_of_columns = ["Sepal length in cm", "Sepal width in cm", "Petal length in cm", "Petal width in cm", "Class"]
iris_df.columns = list_of_columns
iris_df.describe().to_csv("Summary_of_varibles.txt", sep= "\t")


# Project  -  Analysing Iris Dataset
# Author: Renan Riva

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plots_file as plots

# Opening the file and allocating it to a variable.
iris_df = pd.read_csv('iris.csv')

#Adding headers to the collums using the attribut information on "https://archive.ics.uci.edu/ml/datasets/iris". To make clear what each column represent and to use after when
# generating and saving the plots
list_of_columns = ["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"]
iris_df.columns = list_of_columns


# Using a lambda function to apply a formating to every item in the summary of the data frame and setting it to 3 decimals. Reference week 6 ,(https://stackoverflow.com/questions/55394854/how-to-change-the-format-of-describe-output) and  (https://www.w3schools.com/python/python_lambda.asp)
iris_df.describe().applymap(lambda x: f"{x:0.3f}").to_csv("Summary_of_varibles.txt ", header =True, sep= "\t")


#Filtering the data to make the plots, references https://www.youtube.com/watch?v=vmEHCJofslg&t=1390s, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
#Using the Panda's Loc function to filter the collums per type of flower, to use it in the scatter plot and check if there is any relation between the flower type
# and the size or proportions of the petal/Sepal 
iris_setosa = iris_df.loc[iris_df['Class'] == "Iris-setosa"]
iris_versicolor = iris_df.loc[iris_df['Class'] == "Iris-versicolor"]
iris_virginica = iris_df.loc[iris_df['Class'] == "Iris-virginica"]



### Importing the plots functions from the plots module created, these function will create a histogram plot. These function take one argument which is Database name and column name
### following the format database['column'] in this case the database is iris_df

plots.sepal_length_hist(iris_df['Sepal length'])
plots.sepal_width_hist(iris_df['Sepal width'])
plots.petal_length_hist(iris_df['Petal length'])
plots.petal_width_hist(iris_df['Petal width'])

# ### Importing the plots functions from the plots module created, these function will create a Scatter plot using the data filtered by class of flower.
# References: https://stackoverflow.com/questions/17411940/matplotlib-scatter-plot-legend , https://realpython.com/visualizing-python-plt-scatter/



plots.scatter_plot_petal(iris_setosa['Petal length'], iris_setosa['Petal width'], iris_versicolor['Petal length'], iris_versicolor['Petal width'], iris_virginica['Petal length'], iris_virginica['Petal width'])
plots.scatter_plot_sepal(iris_setosa['Sepal length'], iris_setosa['Sepal width'], iris_versicolor['Sepal length'], iris_versicolor['Sepal width'], iris_virginica['Sepal length'], iris_virginica['Sepal width'])
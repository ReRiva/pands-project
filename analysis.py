# Project  -  Analysing Iris Dataset
# Author: Renan Riva

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris_df = pd.read_csv('iris.csv')

def summary_variables():
    #Adding headers to the collums using the attribut information on "https://archive.ics.uci.edu/ml/datasets/iris". To make clear what each column represent.
    list_of_columns = ["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"]
    iris_df.columns = list_of_columns
    # Using the describle function to get a summary of the variables and formating it to 3 decimals (https://stackoverflow.com/questions/55394854/how-to-change-the-format-of-describe-output)

    # Using a lambda function to apply a formating to every item in the summary of the data frame and setting it to 3 decimals.
    return iris_df.describe().applymap(lambda x: f"{x:0.3f}").to_csv("Summary_of_varibles.txt ", header =True, sep= "\t")

summary_variables()





### Creating the Histogram Plots(not saving yet, need to do some adjustments and style it)
def sepal_length_plot():
    plt.hist(iris_df['Sepal length'], bins=10)
    plt.style.use("fivethirtyeight")
    plt.title("Testing")
    plt.xlabel("Sepal Length")
    plt.ylabel("Occurrences")
    plt.show()
    return

def sepal_width_plot():
    plt.hist(iris_df['Sepal width'], bins=10)
    plt.style.use("fivethirtyeight")
    plt.title("Testing")
    plt.xlabel("Sepal width")
    plt.ylabel("Occurrences")
    plt.show()
    return

def petal_length_plot():
    plt.hist(iris_df['Petal length'], bins=10)
    plt.style.use("fivethirtyeight")
    plt.title("Testing")
    plt.xlabel("Petal length")
    plt.ylabel("Occurrences")
    plt.show()
    return

def petal_width_plot():
    plt.hist(iris_df['Petal width'], bins=10)
    plt.style.use("fivethirtyeight")
    plt.title("Testing")
    plt.xlabel("Petal width")
    plt.ylabel("Occurrences")
    plt.show()
    return

petal_width_plot()
# Function for saving the histogram plots in png format
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Code for ploting the histogram and saving it as png.  References https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.hist.html https://www.youtube.com/watch?v=XDv6T4a0RNc&t=246s, https://stackoverflow.com/questions/16180946/drawing-average-line-in-histogram-matplotlib
# https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib. 

def sepal_length_hist(database):
    plt.clf()
    plt.hist(database, bins=9, edgecolor="black")
    plt.style.use("fivethirtyeight")
    plt.title("Occurrences by Sepal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Occurrences")
    plt.axvline(database.mean(), color='Red', linestyle="--", linewidth=1.3, label = "Median Lenght")  
    plt.legend(fontsize = "x-small")    
    plt.savefig("Sepal_length_hist.png")
    return
    



def sepal_width_hist(database):
    plt.clf()
    plt.hist(database, bins=9, edgecolor="black")
    plt.style.use("fivethirtyeight")
    plt.title("Occurrences by Sepal Width")
    plt.xlabel("Sepal Width")
    plt.ylabel("Occurrences")
    plt.axvline(database.mean(), color='Red', linestyle="--", linewidth=1.3)    
    plt.savefig("Sepal_width_hist.png")
    return


def petal_length_hist(database):
    plt.clf()
    plt.hist(database, bins=9, edgecolor="black")
    plt.style.use('fivethirtyeight')
    plt.title("Occurrences by Petal Length")
    plt.xlabel("Petal length")
    plt.ylabel("Occurrences")
    plt.axvline(database.mean(), color='Red', linestyle="--", linewidth=1.3, label = "Median Lenght")  
    plt.legend() 
    plt.savefig("Petal_length_hist.png")
    return
    
    

def petal_width_hist(database):
    plt.clf()
    plt.hist(database, bins=9, edgecolor="black")
    plt.style.use("fivethirtyeight")
    plt.title("Occurrences by Petal Width")
    plt.xlabel("Petal width")
    plt.ylabel("Occurrences")
    plt.axvline(database.mean(), color='Red', linestyle="--", linewidth=1.3)
    plt.savefig("Petal_width_hist.png")
    return




##### Scatter plot code - Creating the Scatter plots using Matplotlib. Add https://stackoverflow.com/questions/17411940/matplotlib-scatter-plot-legend , https://realpython.com/visualizing-python-plt-scatter/

def scatter_plot_petal(setosa_length,setosa_width, versicolor_length, versicolor_width,virginica_length, virginica_width ):
    plt.clf()
    plt.cla()
    setosa = plt.scatter(setosa_length, setosa_width, color = 'Green', edgecolors='Black')
    versicolor = plt.scatter(versicolor_length, versicolor_width, color = 'Red', edgecolors='Black')
    virginica = plt.scatter(virginica_length, virginica_width, color = 'Blue', edgecolors='Black')
    plt.style.use('seaborn-dark-palette')
    plt.title('Iris Petal Sizes')
    plt.xlabel('Petal Length', fontsize = "small")
    plt.ylabel('Petal Width', fontsize = "small")
    plt.legend((setosa, versicolor, virginica), ('Iris Setosa', 'Iris Versicolor', 'Iris Virginica'), scatterpoints = 1)
    plt.savefig('Petal_sizes_scatter.png')
    return


def scatter_plot_sepal(setosa_length,setosa_width, versicolor_length, versicolor_width,virginica_length, virginica_width ):
    plt.clf()
    plt.cla()
    setosa = plt.scatter(setosa_length, setosa_width, color = 'Green', edgecolors='Black')
    versicolor = plt.scatter(versicolor_length, versicolor_width, color = 'Red', edgecolors='Black')
    virginica = plt.scatter(virginica_length, virginica_width, color = 'Blue', edgecolors='Black')
    plt.style.use('seaborn-dark-palette')
    plt.title('Iris Sepal Sizes')
    plt.xlabel('Sepal Length', fontsize = "small")
    plt.ylabel('Sepal Width', fontsize = "small")
    plt.legend((setosa, versicolor, virginica), ('Iris Setosa', 'Iris Versicolor', 'Iris Virginica'), scatterpoints = 1)
    plt.savefig('Sepal_sizes_scatter.png')
    return
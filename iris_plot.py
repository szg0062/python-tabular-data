#! /usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

"""
A script for regressing and plotting two variables stored in columns of a
tabular data file ('iris.csv'). 
"""

def plot_data():
    data = pd.read_csv("iris.csv")

    setosa = data[data.species == "Iris_setosa"]
    virginica = data[data.species == "Iris_virginica"]
    versicolor = data[data.species == "Iris_versicolor"]

    a = setosa.petal_length_cm
    b = setosa.sepal_length_cm
    regression = stats.linregress(a, b)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(a, b, label = 'Setosa Petal vs Sepal Lengths (cm)')
    plt.plot(a, slope * a + intercept, color = "red", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("Setosa_regression_plot.png")
    #plt.clf - clears previous plots for the upcoming one in the script 
    plt.clf()



    c = virginica.petal_length_cm
    d = virginica.sepal_length_cm
    regression = stats.linregress(c, d)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(c, d, label = 'Virginica Petal vs Sepal Lengths (cm)')
    plt.plot(c, slope * c + intercept, color = "blue", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("Virginica_regression_plot.png")
    plt.clf()


    x = versicolor.petal_length_cm
    y = versicolor.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Versicolor Petal vs Sepal Lengths (cm)')
    plt.plot(x, slope * x + intercept, color = "green", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("Versicolor_regression_plot.png")
    plt.clf()

    print("You have plots!")

if __name__ == '__main__':
  plot_data()

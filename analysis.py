#install packages and set options
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option("precision", 2)


# Define functions
def appendTable(input,title):
    with open("output.txt", "a") as f:
        output = input.to_string()
        f.write(title + "\n")
        f.write(output)
        f.write("\n \n")
        

def appendText(input):
          with open("output.txt", "a") as f:
              f.write(input) 

# Create the output file
filename = "output.txt"
with open("output.txt", "w") as f:
    f.write("iris.data Summary \n \n")
    

# Import data
datafile = "iris.data"
variableNames = ["sepal lenght","sepal width","petal lenght","petal width","class"]
data = pd.read_csv(datafile,header = None, names = variableNames ) 

# summary statistics

for i in variableNames:
    summaryTable = data[i].describe()
    appendTable(summaryTable,i)


summaryDesc = """The summary statistics are shown for the variables: sepal lenght, sepal width, petal lenght, petal width and class.
These variables refer to the dimensions of the Iris flower and the class refers to type of plant. """

appendText(summaryDesc)

# histograms

colors = ["aqua","coral","indigo","lavender","lightgreen"]

n_bins = 15
for i, j  in zip(variableNames, colors):
    plt.hist(data[i], n_bins, facecolor = j)
    plt.title("Histogram of " + i)
    plt.savefig(i + ".png")
    plt.close()
    
# Data as arrays

sepalLenght = data["sepal lenght"].to_numpy()
sepalWidth = data["sepal width"].to_numpy()
petalLenght = data["petal lenght"].to_numpy()
petalWidth = data["petal width"].to_numpy()


# scatter plots

xVariables = [sepalLenght,sepalLenght,sepalLenght,sepalWidth,sepalWidth,petalLenght]
yVariables = [sepalWidth,petalLenght,petalWidth,petalWidth,petalLenght,petalWidth]
Titles = ["sepal lenght sepal width","sepal lenght petal lenght","sepal lenght petalwidth",\
"sepal width petal width","sepal width petal lenght","petal lenght petal width"]


for x in xVariables:
    for y in yVariables:
        for t in Titles:
            plt.scatter(x,y)
            plt.savefig(t)
            plt.close()




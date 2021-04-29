#install packages and set options
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as stats
from scipy.stats import f_oneway
import seaborn as sns




pd.set_option("precision", 2)


# Define functions
def appendTable(input,title):
    with open("output.txt", "a") as f: # append mode
        output = input.to_string()
        f.write(title + "\n")
        f.write(output)
        f.write("\n \n")
        

def appendText(input):
          with open("output.txt", "a") as f:
              f.write("\n")
              f.write(input) 
              f.write("\n")

# Create the output file
filename = "output.txt"
with open("output.txt", "w") as f:  # want a new file - open in write mode/
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


for i, j, k in zip(xVariables,yVariables,Titles):
    plt.scatter(i,j)
    #plt.savefig(k)
    plt.close()




# summary statistics by iris class
groupMeans = data.groupby(["class"]).mean()
appendTable(groupMeans,"\n Group Means")
groupDesc = data.groupby(["class"]).describe(percentiles = [])
appendTable(groupDesc,"\n Descriptive Statistics by Class")



# group by class
irisSetosa = data.loc[data["class"] == "Iris-setosa"]
IrisVersicolor = data.loc[data["class"] == "Iris-versicolor"]
IrisVirginica = data.loc[data["class"] == "Iris-virginica"]



# group graphs








#statistical tests

#F-Test petal lenght
a = irisSetosa["petal lenght"].to_numpy()
b = IrisVersicolor["petal lenght"].to_numpy()
c = IrisVirginica["petal lenght"].to_numpy()

petalLenghtTest = f_oneway(a,b,c)
appendText("Petal Lenght F-Test")
appendText(repr(petalLenghtTest))

#F-Test petal width
a = irisSetosa["petal width"].to_numpy()
b = IrisVersicolor["petal width"].to_numpy()
c = IrisVirginica["petal width"].to_numpy()


petalWidthTest = (f_oneway(a,b,c))
appendText("Petal Width F-Test")
appendText(repr(petalWidthTest))

#F-Test sepal lenght
a = irisSetosa["sepal lenght"].to_numpy()
b = IrisVersicolor["sepal lenght"].to_numpy()
c = IrisVirginica["sepal lenght"].to_numpy()

sepalLenghtTest = f_oneway(a,b,c)
appendText("Sepal Lenght F-Test")
appendText(repr(sepalLenghtTest))

#F-Test sepal width
a = irisSetosa["sepal width"].to_numpy()
b = IrisVersicolor["sepal width"].to_numpy()
c = IrisVirginica["sepal width"].to_numpy()

sepalLenghtTest = f_oneway(a,b,c)
appendText("Sepal Width F-Test")
appendText(repr(sepalLenghtTest))

#appendText(sepalLenghtTest)
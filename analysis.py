#install packages and set options
import numpy as np
import pandas as pd


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



for i in variableNames:
    summaryTable = data[i].describe()
    appendTable(summaryTable,i)


summaryDesc = """The summary statistics are shown for the variables: Sepal lenght, sepal width, petal lenght, petal width and class.
These variables refer to the dimensions of the Iris flower and the class refers to type of plant. """

appendText(summaryDesc)



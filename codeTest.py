
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

###################################

print(data.columns)

print(data["sepal lenght"])


'''
sepalLenghtDesc = data["sepal lenght"].describe()
appendTable(sepalLenghtDesc,"sepal lenght")
sepalLenghtDesc = data["sepal width"].describe()
appendTable(sepalLenghtDesc,"sepal width")
sepalLenghtDesc = data["petal lenght"].describe()
appendTable(sepalLenghtDesc,"petal lenght")
sepalLenghtDesc = data["petal width"].describe()
appendTable(sepalLenghtDesc,"petal width")
sepalLenghtDesc = data["class"].describe()
appendTable(sepalLenghtDesc,"class")


# Descriptive Statistics
dataDesc = data.describe()  # by default only the numeric data types are included. 

#print(dataDesc)
#append(dataDesc) 


n_bins = 20 
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

sepalLenght = data(["sepal lenght"])
sepalWidth = data(["sepal width"])

axs[0].hist(sepalLenght)
axs[1].hist(sepalWidth)
#plt.hist(data["sepal lenght"],n_bins)
#plt.show()


'''

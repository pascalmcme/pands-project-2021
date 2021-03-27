#install packages
import numpy as np
import pandas as pd
import os


# options
pd.set_option("precision", 2)


# functions
def append(input,title):
    with open("output.txt", "a") as f:
        output = input.to_string()
        f.write(title + "\n")
        f.write(output)
        f.write("\n \n")
        
        

# Create the output file
filename = "output.txt"
with open("output.txt", "w") as f:
    f.write("iris.data Summary \n \n")
    


#import the data
datafile = "iris.data"
data = pd.read_csv(datafile,header = None, names = ["sepal lenght","sepal width","petal lenght","petal width","class"] ) 
#print(data)


# Descriptive Statistics
dataDesc = data.describe()  # by default only the numeric data types are included. 

#print(dataDesc)
#append(dataDesc) 


sepalLenghtDesc = data["sepal lenght"].describe()
append(sepalLenghtDesc,"sepal lenght")
sepalLenghtDesc = data["sepal width"].describe()
append(sepalLenghtDesc,"sepal width")
sepalLenghtDesc = data["petal lenght"].describe()
append(sepalLenghtDesc,"petal lenght")
sepalLenghtDesc = data["petal width"].describe()
append(sepalLenghtDesc,"petal width")
sepalLenghtDesc = data["class"].describe()
append(sepalLenghtDesc,"class")







#os.remove("input.txt")
#https://realpython.com/python-csv/
import numpy as np
import pandas as pd


data = pd.read_csv("iris.data",header = None, names = ["sepal lenght","sepal width","petal lenght","petal width","class"] ) 


print(data)

dataDesc = data.describe()  # by default only the numeric data types are included. 
print(dataDesc)


sepalLenghtDesc = data["sepal lenght"].describe()
print(sepalLenghtDesc)

sepalLenghtDesc = data["sepal width"].describe()
print(sepalLenghtDesc)

sepalLenghtDesc = data["petal lenght"].describe()
print(sepalLenghtDesc)

sepalLenghtDesc = data["petal width"].describe()
print(sepalLenghtDesc)

sepalLenghtDesc = data["class"].describe()
print(sepalLenghtDesc)



#look at one column / variable
#sepalLenght = data["sepal lenght"]
#print(sepalLenght)
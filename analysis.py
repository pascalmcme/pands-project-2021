#https://realpython.com/python-csv/
import numpy as np
import pandas as pd


data = pd.read_csv("iris.data",header = None, names = ["sepal lenght","sepal width","petal lenght","petal width","class"] ) 


#look at one column / variable
#sepalLenght = data["sepal lenght"]
#print(sepalLenght)




#print(data)


print(data.mean())

#https://pandas.pydata.org/docs/user_guide/10min.html 
# introduction to working with dataframes
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
#dataframe

#https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#descriptive-statistics
# see for descriptive statistics
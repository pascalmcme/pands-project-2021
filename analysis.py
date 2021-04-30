#install packages and set options
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as stats
from scipy.stats import f_oneway
import seaborn as sns


pd.set_option("precision", 2) # set pandas decimal precision
sns.set_theme(palette="magma") #set color seaborn plots

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
variableNames = ["Sepal-Lenght","Sepal-Width","Petal-Lenght","Petal-Width","Class"]
data = pd.read_csv(datafile,header = None, names = variableNames ) 

# summary statistics

for i in variableNames:
    summaryTable = data[i].describe()
    appendTable(summaryTable,i)


summaryDesc = """The summary statistics are shown for the variables: sepal lenght, sepal width, petal lenght, petal width and class.
These variables refer to the dimensions of the Iris flower and the class refers to type of plant. """

appendText(summaryDesc)

# histograms


for i in ["Sepal-Lenght","Sepal-Width","Petal-Lenght","Petal-Width"]:

    sns.histplot(data=data, x=i, hue="Class", multiple="stack",bins=15,kde=True) # remove class for kde 
    sns.light_palette("seagreen", as_cmap=True)
    plt.xlabel(i+" in cm")
    plt.title("Histogram of " + i)
    plt.savefig(i + ".png")
    plt.close()



# Data as arrays

sepalLenght = data["Sepal-Lenght"].to_numpy()
sepalWidth = data["Sepal-Width"].to_numpy()
petalLenght = data["Petal-Lenght"].to_numpy()
petalWidth = data["Petal-Width"].to_numpy()


# scatter plots

xVariables = [sepalLenght,sepalLenght,sepalLenght,sepalWidth,sepalWidth,petalLenght]
yVariables = [sepalWidth,petalLenght,petalWidth,petalWidth,petalLenght,petalWidth]
Titles = ["Sepal-Lenght Sepal-Width","Sepal-Lenght Petal-Lenght","Sepal-Lenght Petal-Width",\
"Sepal-Width Petal-Width","Sepal-Width Petal-Lenght","Petal-Lenght Petal-Width"]


for i, j, k in zip(xVariables,yVariables,Titles):
    #plt.scatter(i,j)
    sns.scatterplot(data=data, x=i, y=j,hue="Class")
    plt.savefig(k)
    plt.close()
    


# summary statistics by iris class
groupMeans = data.groupby(["Class"]).mean()
appendTable(groupMeans,"\n Group Means")
groupDesc = data.groupby(["Class"]).describe(percentiles = [])
appendTable(groupDesc,"\n Descriptive Statistics by Class")



# group by class
irisSetosa = data.loc[data["Class"] == "Iris-setosa"]
IrisVersicolor = data.loc[data["Class"] == "Iris-versicolor"]
IrisVirginica = data.loc[data["Class"] == "Iris-virginica"]




#statistical tests

#F-Test petal lenght
a = irisSetosa["Petal-Lenght"].to_numpy()
b = IrisVersicolor["Petal-Lenght"].to_numpy()
c = IrisVirginica["Petal-Lenght"].to_numpy()

petalLenghtTest = f_oneway(a,b,c)
appendText("Petal-Lenght F-Test")
appendText(repr(petalLenghtTest))

#F-Test petal width
a = irisSetosa["Petal-Width"].to_numpy()
b = IrisVersicolor["Petal-Width"].to_numpy()
c = IrisVirginica["Petal-Width"].to_numpy()


petalWidthTest = (f_oneway(a,b,c))
appendText("Petal-Width F-Test")
appendText(repr(petalWidthTest))

#F-Test sepal lenght
a = irisSetosa["Sepal-Lenght"].to_numpy()
b = IrisVersicolor["Sepal-Lenght"].to_numpy()
c = IrisVirginica["Sepal-Lenght"].to_numpy()

sepalLenghtTest = f_oneway(a,b,c)
appendText("Sepal-Lenght F-Test")
appendText(repr(sepalLenghtTest))

#F-Test sepal width
a = irisSetosa["Sepal-Width"].to_numpy()
b = IrisVersicolor["Sepal-Width"].to_numpy()
c = IrisVirginica["Sepal-Width"].to_numpy()

sepalLenghtTest = f_oneway(a,b,c)
appendText("Sepal-Width F-Test")
appendText(repr(sepalLenghtTest))

#appendText(sepalLenghtTest)



''''

# histograms

colors = ["aqua","coral","indigo","lavender","lightgreen"]

n_bins = 15
for i, j  in zip(variableNames, colors):
    plt.hist(data[i], n_bins, facecolor = j)
    plt.title("Histogram of " + i)
    plt.savefig(i + ".png")
    plt.close()
    
sns.kdeplot(data=data, x="petal lenght", hue="class", multiple="stack")
plt.show()

'''
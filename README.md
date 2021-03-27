

# Summary of the data set

The iris data set is available from the UCI machine learning repository [1]. It is a frequently used database for demonstrating tools in data anaylsis [2]. The data set consists of 150 observations of iris plants.  Five attributes are recorded. Sepal lenght , sepal width, petal length, petal width,  are measured in centimeters. The class if also given which refers to the type of iris plant. There are three classes with 50 obervations of each, namely Iris Setosa, Iris Versicolour and Iris Virginica. The data set was famously used in a study meausring how the different classes of iris could best be differentiated based on these measurements [3]. 


[1] https://archive.ics.uci.edu/ml/datasets/iris
[2] https://www.sciencedirect.com/topics/mathematics/iris-data
[3] Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to Mathematical Statistics" (John Wiley, NY, 1950).


For opening the data stored in a csv file I used [4] as  a reference. I decided to use the pandas module to import the data as it made it easy to write the code for storing the data. With one line of code I could import the data and store it as a data frame. This is a familiar data structure, with the rows showing different observations and the columns their respective attributes. Pandas also offers many other useful features, for example manipulating or visualising data [5]

[4] https://realpython.com/python-csv/
[5] https://pandas.pydata.org/docs/user_guide/index.html#user-guide


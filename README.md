

# Summary of the data set

The iris data set is available from the UCI machine learning repository [1]. It is a frequently used database for demonstrating tools in data anaylsis [2]. The data set consists of 150 observations of iris plants.  Five attributes are recorded. Sepal lenght , sepal width, petal length, petal width,  are measured in centimeters. The class if also given which refers to the type of iris plant. There are three classes with 50 obervations of each, namely Iris Setosa, Iris Versicolour and Iris Virginica. The data set was famously used in a study meausring how these three classes of iris could best be differentiated based on their measurements [3]. 


[1] https://archive.ics.uci.edu/ml/datasets/iris
[2] https://www.sciencedirect.com/topics/mathematics/iris-data
[3] Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to Mathematical Statistics" (John Wiley, NY, 1950).

# opening the data
For opening the data stored in a csv file I used [4] as  a reference. I decided to use the pandas module to import the data as it made it easy to write the code. With one line of code I could import the data and store it as a data frame. This is a familiar data structure, with the rows showing different observations and the columns their respective attributes. Pandas also offers many other useful features, for example manipulating or visualising data [5]. The 

[4] https://realpython.com/python-csv/
[5] https://pandas.pydata.org/docs/user_guide/index.html#user-guide

# summary statistics
To create summary statistics for the variables I used pandas detailed user guide [6]. The describe command can be used to generate summary statistics for a variable, such as the mean, standard deviation and percentiles. In order to output the summary tables to the text file I first convert the data to text and use the inbuilt write funtion to append the table. This is a flexible method, which allows titles and text to be added to the tables [7]. I use the additional options offered by pandas limit the number of decimal places, making the tables easier to read. 

[6] https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics
[7] https://stackoverflow.com/questions/43423950/how-to-print-title-above-pandas-dataframe-to-csv
[8] https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#frequently-used-options


# additional references

https://scipy-lectures.org/packages/statistics/index.html#data-representation-and-interaction
overview of statistical methods in python. 
https://www.w3schools.com/python/python_file_remove.asp
removing a file
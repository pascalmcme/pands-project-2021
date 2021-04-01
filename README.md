

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
To create summary statistics for the variables I used the describe() funtion from the pandas module . The describe funtion can be used to generate summary statistics for a variable, such as the mean, standard deviation and percentiles. In order to output the summary tables to the text file I first convert the data to text and use the inbuilt write funtion to append the tables. This is a flexible method, which allows titles and text to be added to the tables [7]. I use the option pd.set_option("precision", 2) whichs limit the number of decimal places, making the tables easier to read. 

[6] https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics
[7] https://stackoverflow.com/questions/43423950/how-to-print-title-above-pandas-dataframe-to-csv
[8] https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#frequently-used-options


# histograms
To create historgrams of the variables I use the hist() funtion from matlotlib[9]. In addition to plotting the variables I also include optional paramaters for the bin sizes and colors. I also used sample histograms from matplotlibs documentation as a reference[10]. The bins option allowed me to specify how many intervals I wanted to seperate the data into. I use a loop with two indexes, to creat a histogram for each variable in a seperate color [11]


[9] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist
[10]https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
[11]https://stackoverflow.com/questions/18648626/for-loop-with-two-variables
[12]https://stackoverflow.com/questions/37734512/savefig-loop-adds-previous-plots-to-figure
[13]https://matplotlib.org/3.1.1/tutorials/colors/colors.html


# scatter plots

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
https://stackoverflow.com/questions/914715/how-to-loop-through-all-but-the-last-item-of-a-list



# data as arrays
Storing the columns as arrays is useful in the case that the whole data frame is not needed. It is also necessary for some of the plotting functions in matplotlib, which do not allow for dataframe inputs. The dataFrame.to_numpy() function converts a dataframe object type to a numpy array. dataFrame is the name of the dataframe object, in my case data. In order to get an array for each column or variable I select columns from the data frame using dataFrame("column name") [14]


[14] https://pandas.pydata.org/docs/user_guide/10min.html
[15] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy
[16] https://stackoverflow.com/questions/46122910/display-print-one-column-from-a-dataframe-of-series-in-pandas

# additional references








https://scipy-lectures.org/packages/statistics/index.html#data-representation-and-interaction
overview of statistical methods in python. 
https://www.w3schools.com/python/python_file_remove.asp
removing a file
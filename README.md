# Iris Database Project

The iris dataset is a dataset that contains fifty entries of data for the petal length, petal width, sepal length and sepal width from three different types of Iris flower (Iris setosa, Iris versicolor and Iris virginica).

The explanation for the code used to analyse the Iris dataset can be found below.

The pandas module was used to read the dataset that was provided in a .csv(comma-separated values) document using the read_csv function of the module and assigned to the variable iris_df. For the data columns a variable containing a list of columns names was created following the description on [UCI Machine Learning Repository - Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris), which shows what each column from the csv document represents, and set as iris_df.columns, the data frame columns

To print the summary of the variables the function .describe() was used, however as it returned values with different decimal lengths. I was also used the .applymap() to apply a function to the database and a lambda function was used to add formatting to the output, setting it to 3 decimal spaces f"{x:0.3f}" .

Before starting with the plots more preparation was done to the database. The .loc function from the Pandas module was used on the column “class” from the data frame to locate each occurrence os each type of Iris flower and store it in a variable. For example, using the .loc on the Class column to search for the string “Iris-virginica” will return all the lines where the flower class is Iris-virginica, by doing we can break down the information in the database in smaller parts making it easier use when plotting the information.

For the plots, a plots module was created to host all the code related to the plots. This file named plots_file.py contains the code for all the plots used and the plots were created using the matplotib.plyplot module.
The plots created are four histogram plots one for each of the Iris flowers attributes ( petal length, petal width, sepal length and sepal width). All the four histogram plots use the same plot style and the code is identical for them.

The plots were made into functions that takes one argument,  iris_df[“name of the column”]. The plots.sepal_length_hist function takes iris_df['Sepal length'] as argument and so on. 
After that there is a. clf() function from matplotib.plyplot for clearing the figure generated by the previous plots so the plots do not overlap each other, also used .context with the “with” keyword to force apply the plot style to the whole plot, instead of using style.use as it was making the plot styles not to be applied after the first plot was generated.

The number of bins for the histogram plot was set to nine and the color edge for the bins to black to make it easier to see each bin. After that the title, x and y labels were set, a mean line was created and stylised using. axvline to add a little bit more of information to the plot and finally the plot was saved as a PNG.




![Iris Setosa](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.plant-world-seeds.com%2Fstore%2Fview_seed_item%2F6010&psig=AOvVaw1OC8i7rQk0_sCaSyPa0P4c&ust=1650892562942000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCNDDip_krPcCFQAAAAAdAAAAABAD)
![Iris Virginica](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.fs.fed.us%2Fwildflowers%2Fbeauty%2Firis%2FBlue_Flag%2Firis_virginica.shtml&psig=AOvVaw16NtNIGyxmfRV_jReyEFba&ust=1650892606355000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCJiPuq7krPcCFQAAAAAdAAAAABAD)
![Iris Versicolor](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.etsy.com%2Fie%2Flisting%2F492772424%2Firis-versicolor-blue-flag-dagger-flower&psig=AOvVaw1J10Ml9cHwPGgJbrUqmBeG&ust=1650892641097000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKiAo8DkrPcCFQAAAAAdAAAAABAD)

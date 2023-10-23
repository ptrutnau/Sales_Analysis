# Sales_Analysis

## Description
This is an analysis of sales data from 2019. Each csv file represents a whole month. All csv files contain the same column names. The data contains purchases of electronic products broken down by order date, product type, quantity ordered, price each and total cost of the order. 
For this task, i will mainly be using Pandas and Matplotlib.

## Process
I start by merging all csv files of every single month having all the sales data in just one dataframe. Link for the code is [here.](https://github.com/ptrutnau/Sales_Analysis/blob/main/merge_dataframes.py)
After that, i read in the merged data into a jupyter notebook.

I proceed with the cleaning of the data which includes the following steps:

- Drop NaN Values
- Removing rows with unplausible values
- Changing column datatypes


In the next Section i answer 5 business questions related to the data:

- What was the best month for sales? How much was earned that month?
- What city sold the most product?
- What time should we display advertisemens to maximize the likelihood of customer’s buying product?
- What products are most often sold together?
- What product sold the most? Why do you think it sold the most?

All the code for the data cleaning section and data exploration section is [here.](https://github.com/ptrutnau/Sales_Analysis/blob/main/SalesAnalysis.ipynb)

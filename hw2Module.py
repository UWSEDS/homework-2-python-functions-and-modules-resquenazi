##1.(1 points) Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or CSVs in data.gov 

import pandas as pd
import numpy as np

def create_dataframe(url):
    return pd.read_csv(url)

##2.(6 points) Create the function test_create_dataframe that takes as input: (a) a pandas DataFrame and (b) a list of column names. 
# The function returns True if the following conditions hold:

# The DataFrame contains only the columns that you specified as the second argument.
# The values in each column have the same python type
# There are at least 10 rows in the DataFrame.
url = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
data = create_dataframe(url)
colNames = list(data.columns)

def test_create_dataframe(data, colNames):
    test_match_colNames = list(data.columns)
    test_rows = len(data)
    test_colDtype = data.dtypes

    if test_match_colNames == colNames:
        print("true")
    elif tes_rows > 10:
        print("true")
    #checking that there are no more data types than there are columns (more data types than columns
    # would indicate rows within a specific column have multiple data types
    elif len(test_colDtype) == len(data.columns): 
        print("true")
    else:
        print("false")

#testing function
test_create_dataframe(data,colNames)

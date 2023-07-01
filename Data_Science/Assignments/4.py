# 4. Implement a function to count the occurrence of each element in a list.
import pandas as pd
# install pandas module using "pip install pandas" command

# it will count all the objects occurrences irrespective of it's data type
def countOccurences(py_list):
    print(pd.Series(py_list).value_counts())

countOccurences([23, 23, 23, 566, "ineuron", "PW Skills", "ineuron", "PW Skills", "ineuron", "ineuron", 96])
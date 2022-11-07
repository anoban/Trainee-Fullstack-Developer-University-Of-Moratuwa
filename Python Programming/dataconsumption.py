from tokenize import Name
import numpy as np

# a dummy one dimensional array
evens = np.array(range(0,1001,2), dtype=float)
evens[1]

my2darray = np.array([range(0,1001,2), [i**2 for i in range(0,1001,2)]], dtype=int)
my2darray[0]
my2darray[1]

dummy = np.array([range(0,101,2), [i**2 for i in range(0,101,2)], [i**3 for i in range(0,101,2)],
                [i**4 for i in range(0,101,2)]], dtype=int)
dummy.T
dummy.transpose()

np.array(range(0,10000,2), dtype=int).shape
np.array(range(0,10000,2), dtype=int).reshape(25,200)

np.array(range(0,100,2)).reshape(10,5)
import random
random.seed(2022-5-11)

nums = np.array([random.choice(range(0,50,3)) for i in range(0,10000,1)])
nums.max()
nums.argmax()
nums[nums.argmax()]

nums.min()
nums.argmin()
nums[nums.argmin()]

nums.argsort()
nums[nums.argsort()]

np.sort(nums)

np.where(nums > 40)
nums[np.where(nums > 40)]
nums[np.where(nums > 40)].max()
nums[np.where(nums > 40)].min()
nums[np.where(nums > 40)].mean()

# slicing by stepping

list(range(0,1000,2))[::2]  # jumps by skipping one element in the list; i.e jumps from index 0 to 2 then to 4 .....
list(range(0,500,5))[::-1]
list(range(0,500,5))[::-2]
list(range(0,500,5))[::-5]

import pandas as pd

# pandas has 3 data structures
# Series - one dimensional
# DataFrame - two dimensional
# Panel - three dimensional

pd.Series(range(0,100))
# series objects have elements, with indices!

series = dict()
x = 0
for i in range(100,0,-1):
    series[i] = x
    x += 1
series

# we can modify the indices in Series objects :)
pd.Series(series)[1] == 99
pd.Series(series)[99] == 1
pds = pd.Series(series)
pd.concat({"First_col":pds, "Second_col": pds}, axis=1)

# data extraction
DataFrame["colname"]  # for extracting columns
DataFrame.loc["rowlabel"]
DataFrame.iloc["integerindex"]

df = pd.DataFrame({"Name": ["Jane","Jennifer","June","Kyle","Sam"],
            "Age" : [22,32,29,27,35],
            "Residence" : ["LA","San Jose","Miami","Tampa","Houston"],
            "Score" : [np.nan,45,89,np.nan,29]})
df

df.dropna() # removes all rows with NaNs :(
df.fillna(0)
df.fillna("")

df = pd.DataFrame({"Name": ["Jane","Jennifer","June","Kyle","Sam","Jane","Kyle"],
            "Age" : [22,32,29,27,35,22,33],
            "Residence" : ["LA","San Jose","Miami","Tampa","Houston","LA","Boston"],
            "Score" : [np.nan,45,89,np.nan,29,np.nan,87]})
df.duplicated()
df.drop_duplicates() # does not affect the original dataframe
df
df.drop_duplicates(inplace = True)  # will drop rows having nas in the original dataframe!
df


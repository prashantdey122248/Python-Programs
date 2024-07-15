
import numpy as np
import pandas as pd
from IPython.display import display

data = {'Animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'Age': [2.5, 3.0, 0.5, np.nan, 5.0, 2.0, 4.5, np.nan, 7, 3],
        'Priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no'],
        'Visits': [1,3,2,3,2,3,1,1,2,1] }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#print(data)
print('1--------Create dataframe from dictionary--------')
df = pd.DataFrame(data,index=labels)
#print(df)
display(df)


print('\n2--------Display a summary of the data frame’s basic information--------\n')
print("summary of dataframe is:")
print(df.info())

print('3--------Return the first three rows of the data frame df--------\n')
print(df.head(3))


print('\n4--------Select just the animal and age columns from the data frame df--------\n')
print("dataframe with only 2 column")
print(df[['Animal','Age']])


print('\n5--------Group by animal name--------\n')
grp=df.groupby('Priority')

for i in grp:
    print(i)

print('\n6--------Find the mean of the animals’ ages--------\n')

print('mean of age is :', df['Age'].mean())

print('\n7--------Display a summary of the data set--------\n')
print(df.describe())


print('\n8--------USING iloc, Return the first three rows of the data frame df-------\n')

print(df.iloc[:3])


print('\n9--------display first and last column of data--------\n')

#syntax: df.iloc[rows,cols]
print(df.iloc[:,[0,3]])

print('------------Another way to display 1st and last columns----')
print(df.iloc[ : , 0],df.iloc[: , 3])

print('\n10--------Observe output of ndim(), shape()-----------\n')
print(df.ndim)
print(df.shape)

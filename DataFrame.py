#WAP to create DataFrame using three different ways (from dictionay,list,array).
#Create food DataFrame (food id,food item,food category).Print
#Add column price per unit,and row.
import pandas as pd
import numpy as np

Data = {'Food_id' : [101,102,103],
        'Food_item' : ["Dhokla","Kulcha","Brownie"],
        'Food_Category' : ["Gujarati","Punjabi","Dessert"]}
df1 = pd.DataFrame(Data)
print(df1)

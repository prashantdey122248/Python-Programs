#DataFrame in python
import pandas as pd

student_data={'id':[101,102,103,104,105,106],
                       'name':['Adwit','Khiyansh','Tathagat','Aditi','Diyana','Geeta'],
                        'age':[19,20,19,22,23,22],
                        'city':['Rajkot','Rajkot','Mumbai','Mumbai','Surat','Surat']
              }

student_df=pd.DataFrame(student_data)
print(student_df,'\n')
'''
#access single cloumn of df
print(student_df['city'])

#access more than 1 columns
print(student_df[['name','city'] ])
'''
#only few records/rows

#head() is for initial 5 rows
#print('This is using head() : ',student_df.head(3))

#tail() is for last 5 rows
#print('This is using tail() : ',student_df.tail(2))

#loc & iloc


#print(student_df.iloc[[3,5],[1,2,3]])

#print(student_df.loc[ (student_df.id>102) & (student_df.city=='Mumbai') ] )

print(student_df.loc[2:4]) #label based index
print(student_df.iloc[2:4]) # integer based index
#-------------------------------------------------------------------
Write a program to create dataframe for movies with movie_id,name,actor,actress,year
use all possible condition and print various output

dict1 = {'movie_id' : [1,2,3,4,5],
         'name' : ["Salaar","Jawan","Krissh","Tiger","OMG"],
         'actor' : ["Prabhas","Shahruk","Hrithik","Salman","Akshay"],
         'actress' : ["Shruti","Ashlesha","Priyanka","Katrina","Genelia"]}

movies = pd.DataFrame(dict1)
print(movies)
print(movies['name'])
print(movies['actor'])
print(movies['actress'])
print(movies[['name','actor']])
print(movies[['name','actress']])
print(movies.head(3))
print(movies.tail(3))





















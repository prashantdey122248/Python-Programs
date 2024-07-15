import xlrd
import pandas as pd

print('\n1--------Read data from excel--------\n')

Second_sheet = pd.read_excel('movies.xls',sheet_name='2000s') # sheet1=0, sheet2=1.....
#print(Second_sheet)

#print('---------print column names---------')
#print(Second_sheet.columns)

print('\n2--------Diplay first seven rows--------\n')
print(Second_sheet.head(7))

print('\n3--------Diplay last 5 rows--------\n')

print(Second_sheet.tail(5))

print('\n4--------- show only one column that is named Budget---------\n')
print(Second_sheet['Budget'])


print('\n5---------Number of rows in 1st sheet----------------\n')
First_sheet=pd.read_excel('movies.xls',sheet_name='1900s') # sheet1=0, sheet2=1.....
print(First_sheet.shape)

print("number of rows are",First_sheet.shape[0])
#print("number of cols are",First_sheet.shape[1])
#print(len(First_sheet))


print('6---------maximum value stored in the Budget column---------\n')
print(Second_sheet['Budget'].max())

print('7--------minimun value stored in the Budget column---------\n')
print(Second_sheet['Budget'].min())

print('8---------find min,max,mean,std, 25%,50%,75% of userr votes column---------\n')
print((Second_sheet['User Votes'].describe()))


print('9--------print the data country=USA and duration= less than---------\n')
print( "Data with country=usa and duration less than 50:")

USA50= Second_sheet[(Second_sheet['Country'] == 'USA') & (Second_sheet['Duration'] <50)]
print(USA50.head())

#print('10-------create avg reviews new column by adding two column---------\n')
Second_sheet['Avg Review'] = (Second_sheet['Reviews by Users'] + Second_sheet['Reviews by Crtiics'])/2

#print(Second_sheet.head(5))


print('11--------sort ascending by Country and avg review by descending order-------\n')
Sort_Country = Second_sheet.sort_values(by='Country', ascending=True)
print(Sort_Country.head())

Sort_Avg_Review=Second_sheet.sort_values(by='Avg Review',ascending=False)
print(Sort_Avg_Review.tail())

#code to create a list having  8 elements.
product = ['phone','earbuds','headphone','laptop','pc','smartWatch','stylus','tab']

#1.Original list
print(product)#['phone', 'earbuds', 'headphone', 'laptop', 'pc', 'smartWatch', 'stylus', 'tab']

#2.5th index of the list
'''print(product[5])#smartWatch

#3.last element of the list
print(product[-1])#tab

#4.-2nd index of the list
print(product[-2])#stylus

#5.print total elements
print(len(product))#8

#6.zero to 3rd index
print(product[0:3])#['phone', 'earbuds', 'headphone']

#7.2nd index to 6th index included
print(product[2:7])#['headphone', 'laptop', 'pc', 'smartWatch', 'stylus']

#8.last four elements using negative index
print(product[5:])#['pc', 'smartWatch', 'stylus', 'tab']

#9.first two index using negative index
print(product[-8:-6])#['phone', 'earbuds']

#10.product[0:]
print(product[0:])#['phone', 'earbuds', 'headphone', 'laptop', 'pc', 'smartWatch', 'stylus', 'tab']

#11.product[:5]
print(product[:5])#['phone', 'earbuds', 'headphone', 'laptop', 'pc']

#12.product[:]
print(product[:])#['phone', 'earbuds', 'headphone', 'laptop', 'pc', 'smartWatch', 'stylus', 'tab']

#13.product[7:]
print(product[7:])#['tab']

#14.product[8]
#print(product[8])#List index out of range.

#15.product[-4:-2]
print(product[-4:-2])#['pc', 'smartWatch']

#16.product[-4:]
print(product[-4:])#['pc', 'smartWatch', 'stylus', 'tab']

#17.sort the list in ascending and descending order
product.sort()
print(product)#['earbuds', 'headphone', 'laptop', 'pc', 'phone', 'smartWatch', 'stylus', 'tab']

product.sort(reverse=True)
print(product)#['tab', 'stylus', 'smartWatch', 'phone', 'pc', 'laptop', 'headphone', 'earbuds']

#18.Append the list with one element
product.append('bluetooth')
print(product)#['phone', 'earbuds', 'headphone', 'laptop', 'pc', 'smartWatch', 'stylus', 'tab', 'bluetooth']

#19.add more products using extend
product.extend(['camera','tv'])
print(product)#['phone', 'earbuds', 'headphone', 'laptop', 'pc', 'smartWatch', 'stylus', 'tab', 'bluetooth', 'camera', 'tv']

#20.add one product at 3rd index
product.insert(3,'ac')
print(product)#['phone', 'earbuds', 'headphone', 'ac', 'laptop', 'pc', 'smartWatch', 'stylus', 'tab', 'bluetooth', 'camera', 'tv']

#21.remove 5th index
product.remove('laptop')
print(product)#['phone', 'earbuds', 'headphone', 'ac', 'pc', 'smartWatch', 'stylus', 'tab', 'bluetooth', 'camera', 'tv']

#22.remove last element.
product.pop()
print(product)#['phone', 'earbuds', 'headphone', 'ac', 'pc', 'smartWatch', 'stylus', 'tab', 'bluetooth', 'camera']

#23.remove elemet by its index.
product.pop(6)
print(product)#['phone', 'earbuds', 'headphone', 'ac', 'pc', 'smartWatch', 'tab', 'bluetooth', 'camera']

#24.copy the list into another list.
product1 = product.copy()
print(product1)#['phone', 'earbuds', 'headphone', 'ac', 'pc', 'smartWatch', 'tab', 'bluetooth', 'camera']

#25.replace the element at index 4 with capital letters.
product[4]='PC'
print(product)#['phone', 'earbuds', 'headphone', 'ac', 'PC', 'smartWatch', 'tab', 'bluetooth', 'camera']
'''

















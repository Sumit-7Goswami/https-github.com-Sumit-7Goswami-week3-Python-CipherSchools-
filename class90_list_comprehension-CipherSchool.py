#  with the help of list comprehension we an create of list in one line

#  create a list of squares from 1 to 10

squares = []
for i in range(1,6):
    squares.append(i**2)
print(squares)    

'''comprehension method'''
sqr = [i**2 for i in range(1,11)]
print(sqr)




negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)   

'''comprehension method''' 
new_negtive = [-i for i in range(1,11)]





names = ['sumit','mohit','rohit']
# output -->  ["s","m","r"]

new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

'''comprehension method'''
new_list = [name[0] for name in names]
print(new_list)







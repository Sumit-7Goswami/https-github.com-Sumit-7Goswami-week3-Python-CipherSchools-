#  map function

numbers = [1,2,3,4]

def square(a):
    return a**2

squares = list(map(square , numbers)) # map kk ander ,,phele function kaa name fir iterable name likhna hh*****
print(squares)    


#**lambda type**## we can do by this way also
numbers = [1,2,3,4]
squares = list(map(lambda a:a**2 , numbers)) 
print(squares)




#** methd 2nd , we can do this y list comprehensive
squares_new = [i**2 for i in numbers]
print(squares_new)




# agr map kee age list lgayayenge to kitni bee baar loop chala skte 
names = ['abc' , 'abcd' , 'abcks']
length = list(map(len , names))
print(length)
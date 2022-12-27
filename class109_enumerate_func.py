# we use enumerate function with for loop to track position of our item  in iterable 


#  How we can do this without enumerate function 
names = ['abc' , 'abcdef' , 'sumit ']
pos = 0
for i in names:
    print(f"{pos} ---> {i}")
    pos += 1



for pos , name in enumerate(names):
    print(f"{pos} ---> {name}")    



# Define a function that takes two arguments 
# 1. list containing string 
# 2. string that want to find in your list and this function will return the index of string in  your list and if string is not present thenn return -1


names = ['abc' , 'abcdef' , 'sumit ']

def find_pos(l , target):
    for pos , name in enumerate(l):
        if name == target:
            return pos
    return -1 

print(find_pos(names , "Sumit"))            

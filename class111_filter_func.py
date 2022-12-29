# we can iterate map and filter only once at a time ,,so we use list and tuple

def is_even(a):
    return a%2 == 0

num = [3,4,2,1,5,6,9,8,10]    

evens = tuple(filter(is_even , num))
print(evens)


#  we can use lambda too 
def is_even(a):
    return a%2==0 
num = [1,2,3,4,5,6,7,8,9,10]    

obj = tuple(filter(lambda a:a%2==0 , num))
# obj = list(filter(lambda a:a%2==0 , num))  
print(obj)


# ################
num = [1,2,3,4,5,6,7,8,9,10]    
obj = filter(lambda a:a%2==0 , num)
for i in obj:
    print(i)
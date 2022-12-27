#  write a function ,on whih when we run we,get our first letter of string is CAPITAL
# 

# function
# list , reverse_str = True
# list

def func(l , **kwargs):
    if kwargs.get('reverse_str'):
        return [i.title() for i in l]
    else:
        return [i.title() for i in l]
names = ["sumit" , "goswami"]
print(func(names))

'''title -- > capitalize the first word '''
#  reverse the string and then capitalize
def func(l , **kwargs):
    if kwargs.get('reverse_str'):
        return [i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]
names = ["sumit" , "goswami"]
print(func(names , reverse_str = True))



# kwargs (keyword arguments)
#  **kwargs (dpoble star operator)

'''*args will take in tuple , while kwargs take in dictionary'''


# kwargs as an parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(name = "sumit" , age =19)

# dictionary unpacking
d = {'name' : 'Sumit', "fav" : "avengers"}
func(**d)


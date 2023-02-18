# You have to have  a complete understanding of functions ,
# first class function / closures
# then finally we will learn about decorators 

def square(a):
    return a**2

s = square(7)
print(s)


# 
s = square
print(s.__name__)

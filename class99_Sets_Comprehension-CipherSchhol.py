#  sets comprehension 
s = {k**2 for k in range(1,11)}
'''sets have npo order'''
print(s)


names = ["Sumit" , "mohit" , "rohit"]
first = {name[0] for name in names}
print(first)
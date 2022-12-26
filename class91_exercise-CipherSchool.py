#  list containing reverse of every string

# Note - USE List comprehension because we already did this exercise 
#  using normal method

#  example
#   l = ['abc' , 'tuv' , 'xyz']
#   reverse_str(1) ----> ['cba' , 'vut' , 'zyx']

def reverse_string(l):
    return [name[::-1] for name in l]

print(reverse_string(['abc','tuv','xyz'])) 



def reverse_str(l):
    new_list = []
    for name in l :
        new_list.append(name[::-1])
    return new_list
print(reverse_str(['abc','tuv','xyz'])) 
       
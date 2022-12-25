# exercise
# define a function that takes a number(n)
# return a dictionary containing cube of numbers from 1 to n


#example/
# cube_finder(4)
# {1:1 , 2:4, 3:9 , 4:16} 



def cube_find(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

print(cube_find(6))        




# def cube_finder(n):
#     return n**3
# n = int(input(""))  
# print(cube_finder(n))


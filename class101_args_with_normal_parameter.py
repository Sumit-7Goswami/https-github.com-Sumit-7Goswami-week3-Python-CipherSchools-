# *args with normal parameter
 
def multiply_nums(num , *args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,6,3,4)) 
'''because 2 is not a part of args'''

 

######
def multiply_nums(num , *args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2)) 



def multiply_nums(num1, num2 , *args):
    multiply = 1
    # print(num1)
    # print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,6,3,4)) 
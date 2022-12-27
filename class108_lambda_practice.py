#  lambda expression practice 

def is_even(a):
    return a%2 == 0  # a%2 ---> True , False
print(is_even(5))

'''now how we can do above question in lambda expression'''
is_even = lambda a: a%2==0 
print(is_even(6))   # so we get true here 



# another example
def last_char(s):
    return s[-1]
print(last_char("Sumit"))    


'''now we do bye lambda expression'''
last_char = lambda  s: s[-1] 
print(last_char("GOSWAMI"))




##**   lambda with if , else 
def func(s):
    if len(s) > 5 :
        return True
    return False
print(func("Sumit"))     

'''it is not compulsory to write if else statement '''
def func(s):
    return len(s) > 5  


'''lambda using'''
func = lambda s : True if len(s)>5 else False 
print(func(input("")))












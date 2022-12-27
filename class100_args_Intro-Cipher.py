# make flexible functions

#  *operator
#  *args

def total(a,b):
    return a+b

# print(total(3,4,10,9))  ,so not possible this,because we have given more than 2 arguents


def all_total(*args):
    print(args)

all_total(1,2,3,4,5,6,7) 


def all_total(*num):
    print(num)
all_total(1,2,3,4,5,6,7)    



# ########
def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4))        



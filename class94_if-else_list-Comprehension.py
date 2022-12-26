# list comprehension with if else
# nums = [1,2,3,4,5,6,7,8,9,10] 
# output -- > if num is even then multiply num  with 2 and if num is odd ,then multiply with -1 with num
# new_list = [-1,4,-3,8]

 
nums = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for i in nums :
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-1)
print(new_list) 




#  comprehensive method
nums = [1,2,3,4,5,6,7,8,9,10]
new_list = [i*2 if (i%2==0) else (-i) for i in nums]
print(new_list)
    

## List Comprehnsive Summary
square = []
for i in range(1,11):
    square.append(i**2)
print(square)    

# comprehensive method
sqr = [i**2 for i in range(1,5)]
print(sqr)

# 
even_num = [i for i in range(1,11)]
print(even_num)



## if-else
# ex --> [1,2,3,4,....10]
#  output ---> [-1,4,-3,8,...]
mixed = [i*2 if (i%2==0) else -i  for i in range(1,11)] 
print(mixed)



nl = [[1,2,3],[1,2,3],[1,2,3]]

new_list2 = []
for j in range(3):
    new_list2.append([1,2,3])

'''comp method'''
new_list = [[i for i in range(1,4)] for j in range(4)]
print(new_list)




l1 = [1,3,5,7]
l2 = [2,4,6,8]

l = [(1,2) , (3,4) , (5,6) , (7,8)]
# * operator with zip

print(list(zip(*l)))


#######################
l = [(1,2) , (3,4) , (5,6) , (7,8)]

l1 , l2 = list(zip(*l))
print(l1)
print(l2)


############33
l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)   # so we get maximum numbers which is in list 1 and dlist 2

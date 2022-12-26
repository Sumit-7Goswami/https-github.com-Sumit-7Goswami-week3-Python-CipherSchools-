#  list comprehension in nested list

example = [[1,2,3],[1,2,3],[1,2,3]]


nested_comp = [[i for i in range(1,4)] for j in range(3) ] 
print(nested_comp)


''' we can write also  in place of j ,,but if we write j ,then we will not confuse'''
# in keyword in sets and for loop

s = {'a','b','c'}

#  in keywords to check if items is prsent or not in sets 
if 'a' in s:
    print("present")
else:
    print("not present")



# for loop 
for item in s:
    print(item) 



# union and inersection
s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union |
union_set = s1 | s2
print(union_set)

print(s1 & s2) ## intersection





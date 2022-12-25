# set data type
# unordered collection of unique items


# s = {1,2,3,2}
# # print(s[l])
# l = [1,2,3,4,5,5,5,5,6,7,7,8]
# # remove duplicate 
# s2 = set(l)
# print(s2)

# s3=list(s2)
# print(s3)


s = {1,2,3}
s.add(4)
s.add(5)
s.add(4)
print(s)


s.remove(3)
print(s)

s.discard(5)

s1 = s.copy()
print(s1)
print(s)


s = {1,1.1,"sring"} #we can store but tupple and list not in sets 
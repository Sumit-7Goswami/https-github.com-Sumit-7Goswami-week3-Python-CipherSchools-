#  list comprehension with if else statement

numbers = list(range(1,11))
# print(numbers)
# even_nums = [2,4,6]
nums = []
for i in numbers:
    if i%2 == 0:
        nums.append(i)
print(nums)        


#  comprehensive method\

even_nums = [i for i in range(1,11)  if i%2==0]
print(even_nums)
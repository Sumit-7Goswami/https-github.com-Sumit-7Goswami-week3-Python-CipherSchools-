# any , all function 

number1 = [2,4,6,8,10]
number2 = [1,2,3,4,5,6]

print(all(num%2==0 for num in number1))


####
even1 = []
for num in number1:
    even1.append(num%2==0)

print(all([True , True ,True , True ,True]))    



# any function
'''any function wil do whether there any one thing whhich is in the condition , like  num%2==0 , if there any even numbers in number 1 , then it calls as true '''
number1 = [1,4,3,7,9]
number2 = [1,2,3,4,5,6]

print(any(num%2==0 for num in number1))

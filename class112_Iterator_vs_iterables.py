#  iterator vs iterables 

num = [1,2,3,4]  # tuples , string , ----> iterables  
squares = map(lambda a:a**2 , num)  # iterator


for i in num:
    print(i)


print(iter(num))


#  ypu can see on youtube of thier differences and make it allow to access  



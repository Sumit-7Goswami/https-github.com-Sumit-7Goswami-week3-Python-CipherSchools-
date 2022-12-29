
# zip function 
user_id = ['user1' , 'user2', 'user3']
names = ['Sumit','Satyam','kisu']
'''if we directly print zip ,,then we got itera obj ...ex....for we use list and tuple '''
print(list(zip(user_id , names)))


# example = [('a',1), ('b',2)]
# print(dict(example))

user_id = ['user1' , 'user2', 'user3']
names = ['Sumit','Satyam','kisu']
print(dict(zip(user_id , names)))


user_id = ['user1' , 'user2', 'user3']
names = ['Sumit','Satyam','kisu']
last_name = ["goswami" , "goswami","goswami"]
print(list(zip(user_id , names , last_name))) #we cannot make dict now with three variables,but we can make list and tuples too
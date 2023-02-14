# advance min() and max() 

# numbers = [1 , 2 , 4 , 5 ,7]
# print(max(numbers))



'''if we have to find the maximum lenght of names'''

# def func(item):
#     return len(item)

# names = ['Sumit' , 'Goswami' ,'ponky']
# print(max(names , key = func))
    


'''we can use lambda also'''   
names = ['Sumit' , 'Goswami' ,'ponky']
print(max(names , key = lambda item : len(item)))


############3

students = [
    {'name' : 'Goswami' , 'score' : 90 , 'age':24},
    {'name': 'Sumit' , 'score': 70, 'age':19},
    {'name': 'rohit' , 'score': 60 , 'age':23}
]

print(max(students , key = lambda item:item.get('score')))
print(max(students , key = lambda item:item.get('score'))['name'])

############################


student = {
    'Goswami' : { 'score' : 90 , 'age':24},
    'Sumit' : { 'score': 70, 'age':19},
    'rohit' : {'score': 60 , 'age':23}
}
print(max(student , key = lambda item : student[item]['score']))


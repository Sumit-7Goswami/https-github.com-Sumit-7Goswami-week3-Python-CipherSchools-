# summary dictionary '
#  what is dictionary 
#  unordered collection of data

d = {"name" : "Sumit" , "age" : 19}

# or
d1 = dict(name = "Sumit" , age = "24")


# or

d2 = {
    "name"  :'Sumit Goswami',
    'age'   : 19 , 
    'gender'  :"male"
}



# how to access data from the dictionary 
# you cannot do like this 
# d[0] , because there is no order inside dixtionary



# syntax
# print(dict-name[key-name])
print(d["name"])



# add data inside empty dict
empty_dict = {}
empty_dict['key1'] = 'value1'
empty_dict["key2"] = 'value2'


#  check existence of value inside dict
#  use in keyword to check for keys
# if 'name' in d:



# how to iterate over dictionary
# most common method
for key , value in d.items():
    print(f' key is {key} and value is {value}')




# to print all keys 
for i in d :
    print(i) 



# to print all values 
for i in d.values():
    print(i)


# most common dict methods
'''get method'''  
print(d.get('name'))


# Q - why we use get
# A - to get rid of error
# example
print(d['name'])
# print(d.get['names'])













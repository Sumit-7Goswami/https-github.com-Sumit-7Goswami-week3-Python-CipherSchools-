# users = {
#     "name" : "Goswami",
#     "age" : "19",
#     "fav_movies" : ["spy" , "avengers"],
#     "fav_songs" : ["song1" , "song2"]
# }

user = {}

name = input("your name : ")
age = input("your age : ")
fav_movies = input("your fav movies  ").split(',')
fav_songs = input("ur fav songs : ").split(',')

user["name"] = name
user["age"] = age
user["fav_movies"] = fav_movies
user["fav_songs"] = fav_songs

for key,value in user.items():
    print(f"{key}:{value}") 
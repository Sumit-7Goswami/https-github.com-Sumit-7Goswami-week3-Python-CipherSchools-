#  dictionary comprhension 

# square = {1:1 , 2:4 , 3:9}
square = {num:num**2 for num in range(1,11)}
print(square)


# square = {square of 1 : 1 , square of 2 :4 ...}
square = {f"Square of {num} is":num**2 for num in range(1,11)}
print(square)


square = {f"Square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")


# word counter
string = "Sumit Goswami"
word_count = {char:string.count(char) for char in string}
print(word_count)

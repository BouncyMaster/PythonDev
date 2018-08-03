# List Less than 10

num_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in num_list:
    if x < 5:
        print(x)


new_list = []

for x in num_list:
    if x < 5:
        new_list.append(x)
print(new_list)


another_list = []

user_input = int(input("Please type in a number to be the greater: "))
for x in num_list:
    if x < user_input:
        another_list.append(x)
print(another_list)

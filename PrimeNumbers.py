# Divisors

num_list = []


def load_list():
    for x in range(2, 100):
        num_list.append(x)


load_list()
result = ""
num2check = int(input("Please enter a number to check for divisors: "))
for x in num_list:
    if x >= num2check:
        break
    elif num2check % x == 0:
        result = "Number is not a prime number!"
        break
    else:
        result = "%d is a prime number!" % num2check

print(result)

import random

# Password generator


def addword():
    wordlist = list(("Apple", "Banana", "Cherry", "Dates", "Elephant", "Fungus", "Grape", "Hash", "Indo", "Jeffry", "Koko", "Lemon",
                     "Mango", "Nana", "Orange", "Pair", "Quite", "Resin", "Salt", "Table", "Ubuntu", "Valve", "Wine", "Xamarin", "Yarn", "Zelda"))
    return random.choice(wordlist)


def addchars():
    method = random.randint(1, 4)
    output = ""
    if method == 1:
        output += random.choice('!@#$^&*/\/')
    elif method == 2:
        output += random.choice('abcdefghijklmnopqrstuvwxyz')
    elif method == 3:
        output += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    elif method == 4:
        output += str(random.randint(0, 9))
    else:
        print("Something went wrong")
    return output


def generatepassword(val):
    output = ""
    if val == "w":
        output = addword() + addword()
    elif val == "m":
        while len(output) < 13:
            output += addchars()
    elif val == "s":
        while len(output) < 21:
            output += addchars()
    else:
        print("Something went wrong")
    return output


app = "reset"
while app == "reset":
    strength = input(
        "Choose your password strength - (W)eak /(M)edium / (S)trong : ").lower()
    print(generatepassword(strength))
    app = ""
    app = input(
        "Press the enter key to close or type 'reset' to try again...").lower()

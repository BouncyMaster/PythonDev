import random

# Password generator


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
        print "Something went wrong"
    return output


def generatepassword(val):
    output = ""
    if val == "W":
        while len(output) < 9:
            output += addchars()
    elif val == "M":
        while len(output) < 13:
            output += addchars()
    elif val == "S":
        while len(output) < 21:
            output += addchars()
    else:
        print "Something went wrong"
    return output


strength = raw_input("Choose your password strength - (W)eak /(M)edium / (S)trong : ")
password = generatepassword(strength)

print "\n"+password+"\n"
raw_input("Press any key to close")

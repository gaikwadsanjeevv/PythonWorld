# we can make the parameter optional by giving it value

def increment(number, by=1):
    return number + by

print(increment(2))
print(increment(2,5))  #in case of both values given for parameter the one with calling function is taken.
# all the optional parameter must come after the required parameter so def increment(number, by=1, another) would throw a error


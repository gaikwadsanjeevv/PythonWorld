#the number of paramters defined in a function shows the number of arguments must be passed what if the number or arguments is more than the number if parameter as below :

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2, 3, 4, 5))  #here this is kind of structure like a tuple and it is iterable represented in () braces also tuples are different from list - once creted you cannot change elements- fixed collction of data.
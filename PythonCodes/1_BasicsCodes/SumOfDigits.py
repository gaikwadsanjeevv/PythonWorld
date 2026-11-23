sum = 0
number = int (input ("Enter a positive number with atmost 4 digits:")) # Taking input in variable number
if (number > 0 and number < 9999): # Checking number range between 0 and 9999
    sum +=  number % 10 # Adding remainder to variable sum
    number = number // 10 # Adding quotient to the number
    if (number > 0 ):
        sum +=  number % 10 # Adding remainder to variable sum
        number = number // 10 # Adding quotient to the number
    if (number > 0 ):
        sum +=  number % 10 # Adding remainder to variable sum
        number = number // 10 # Adding quotient to the number
    if (number > 0 ):
        sum +=  number % 10 # Adding remainder to variable sum
        number = number // 10 # Adding quotient to the number
    print ("Sum of digits is:",sum)
else:
    print ("Invalid number")

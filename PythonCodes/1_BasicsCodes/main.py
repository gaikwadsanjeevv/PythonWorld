sum = 0
number = int(input("Enter a number between 0 to 9999: "))
if(number > 0 and number < 9999):
    sum+= number % 10
    number = number // 10
    if(number > 0):
        sum+= number % 10
        number = number // 10
    if(number > 0):
        sum+= number % 10
        number = number // 10
    if(number > 0):
        sum+= number % 10
        number = number // 10
    print("Sum of digits is:",sum)
else:
    print("Invalid Number")
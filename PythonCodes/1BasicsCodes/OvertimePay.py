##This program should calculate the pay of an employee based on hours worked. The input includes the employee’s total hours worked per week and their hourly pay rate. The employee will be paid a base wage for the first 40 hours worked and time-and-a-half (150% of base pay) for any hours past 40 as overtime pay. Output the regular pay, overtime pay, and total pay for the week on the screen.

hours = int(input ("Enter the total working hours:"))
payRate = int (input ("Enter the hourly pay rate:"))
if (hours <= 40): # If hours are less than or equal to 40
    regPay = hours * payRate # regular pay will be calculated.
    print ("Regular pay:",regPay)
else: # if hours are greater than 40
    regPay = 40 * payRate
    overTime = hours - 40
    increasePay = payRate + (payRate / 2)
    overPay = increasePay * overTime
    print ("Regular pay:",regPay)
    print("Overtime pay:",overPay)
    print ("Total pay:",regPay+overPay)

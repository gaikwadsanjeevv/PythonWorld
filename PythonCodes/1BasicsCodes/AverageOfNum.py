values = int(input ("How many values do you want to enter:"))
sumOfValues = 0
print("Enter", values, "values:")

for i in range (1,values+1):
    v = int(input())
    sumOfValues += v
if values > 0:
   print ("The average is :",sumOfValues/values)

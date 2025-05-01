##Use Case                  	Use if + elif          	Use multiple if
##One condition should match	    ✔️	                  ❌
##Multiple conditions can match	  ❌	                  ✔️
##Need exclusive decision tree	  ✔️ if → elif → else 	❌
##Conditions are independent	    ❌	                  ✔️



x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

if x > 0 and y > 0:
    print("The point lies in the 1st Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the 2nd Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the 3rd Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the 4th Quadrant.")
elif x == 0 and y == 0:
    print("The point lies at the Origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
elif y == 0:
    print("The point lies on the X-axis.")

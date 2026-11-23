n = int (input("Enter the side of hollow square:"))
for x in range(n):
 for y in range(n):
   if (x==0 or x==n-1 or y==0 or y==n-1):
     print ("*", end="")
   else:
     print (" ", end="")
 print()

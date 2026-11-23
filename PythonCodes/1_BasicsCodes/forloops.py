

for number in range(5):
    print("Sending a message ", number+1, (number + 1) * ".")
print("-------------------------------")
# Cleaner code
for num in range(0,5):
    print("Sending a message ", num+1, num * ".")
print("-------------------------------")
for num2 in range(1,20,2):   # 2 is step
    print("Sending a message ", num2+1, num2 * ".")
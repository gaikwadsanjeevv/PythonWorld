//Nearest Power of 2
num = int(input("Enter a positive number: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    power = 0
    while 2 ** power < num:
        power += 1

    # Two candidate powers of 2
    higher = 2 ** power
    lower = 2 ** (power - 1)

    # Choose the closer one, or the smaller if equally close
    if abs(num - lower) <= abs(num - higher):
        pwr = lower
    else:
        pwr = higher

    print("Nearest power of 2 is:", pwr)

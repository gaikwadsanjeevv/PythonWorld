# input from user always comes as a string

x = input("x:  " )
print(type(x))
y = int(x) + 1
print(y)

# Falsy
# ""
# 0
# None
# when we use above values in boolean context it is false
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(5))
print(bool(""))
print(bool("False"))

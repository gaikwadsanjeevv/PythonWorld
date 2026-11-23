def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    

save_user(id = 1, name = "Josh", age =22)

# ** is used to unpack keyword arguments in to a dictonary
# * is used to unpack positional argument in to a tuple
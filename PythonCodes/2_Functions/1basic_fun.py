def greet(first_name, last_name):    # parameters in bracket
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Sanjeev", "Gaikwad")  #arguments in bracket
greet("John", "Smith")

# 2 types of fucntions
# Above function is - performing a task
# round(1.9) calculates and return a vlaue

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Sanjeev")  
# in above method the variable message can be used for printing on console, write it to a file, send it to a mail 

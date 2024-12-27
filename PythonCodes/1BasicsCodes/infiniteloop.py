# when you evaulate while to always true you may run in infinite loop to make sure to use break

while True: 
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
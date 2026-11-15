message = 'hello world'
print(message.capitalize())
print(message.lower())
print(message.count('l'))
print(message.find('o'))
message = message.replace('world','Universe')
print(message)

greeting = 'Hello'
name = 'sanjeev'
print(greeting+ ',' + name)

##it may be complicated to use + concatination for longer strings
##use formatting placeholder
message = '{},{}'.format(greeting,name)
message = f'{greeting},{name.upper()}'
print(message)
##print(dir(message)) -- gives list of all methods available for the datatype variable
##print(help(str)) -- give more details of the any particular Data type
##print(help(str.lower)) -- give more details of the any particular method

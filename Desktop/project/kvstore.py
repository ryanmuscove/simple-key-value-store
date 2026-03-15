database = []

while True:
    user_input = input() #getting input
    if user_input.lower() == ("exit"):
        break 
    else: 
        split = user_input.split() #splitting 
        command = split[0]
        if command.lower() == "set":
            key = split[1]
            value = split[2]
            print(key,  value)
            database.append([key, value])
      
        elif command.lower() == "get": #get command
         key = split[1]
         for pair in database:
            pair[0] = key
            pair[1]
            if pair == key:
               print(value)
         

print(database)




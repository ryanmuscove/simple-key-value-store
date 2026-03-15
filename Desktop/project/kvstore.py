database = []

while True:
    user_input = input() #getting input
    if user_input.lower() == ("exit"):
        break 
    else: 
        split = user_input.split() #splitting 
        command = split[0]
        if command.lower() == "set":
            found = False
            key = split[1]
            value = split[2]
            for pair in database:
               if pair[0] == split[1]: #pair key matching request key
                  pair[1] = value  #makes new value
                  found = True
               else:
                    database.append([key, value])
      
        elif command.lower() == "get": #get command
         key = split[1]
         for pair in database: #the linear seach
            if pair[0] == key:
               print(pair[1])
         






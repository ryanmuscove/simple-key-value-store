database = []

try:
    with open("data.db") as file: # replay
        for line in file:
            split = line.strip().split()
            command = split[0]
            key = split[1]
            value = split[2]
            found = False
            for pair in database:
                if pair[0] == key:
                    pair[1] = value
                    found = True
                    break
            if not found:
                database.append([key, value])
except FileNotFoundError: #try case error
    pass



while True:
    user_input = input() #getting input
    if user_input.lower() == ("exit"):
        break 
    else: 
        split = user_input.split() #splitting 
        command = split[0]

        if command.lower() == "set": #set command
            found = False
            key = split[1]
            value = split[2]
            with open("data.db", "a") as file: #peristance with database file
                file.write(" ".join([command, key, value]) + "\n")
            for pair in database:
               if pair[0] == key: #pair key matching request key
                  pair[1] = value  #makes new value
                  found = True
                  break
            if not found:
                     database.append([key, value])
      
        elif command.lower() == "get": #get command
         key = split[1]
         for pair in database: #the linear seach
            if pair[0] == key:
               print(pair[1])
         






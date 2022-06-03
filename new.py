print("WELCOME TO REGISTER AND LOGIN PORTAL")      # This a login programme to enable users to create a new account
welcome = input("Do you have an account Yes/No" )   # and to give access to previously created accounts.
if welcome == "No":
    while True:
        username = input("Enter your desired username here: ") # This is the input code for the user to input their
        password = input("Enter your password here: ")          # username and password
        password2 = input (" Confirm password: ")          # If the user input no the code enables the user to create a
                                                             # new account
        if password == password2:            # This code is where the txt file to save the user input is created and
            file = open(username+".txt", "w") # also to make sure the users desired password is correct
            file.write(username+","+password)
            file.close()
            break
if welcome == "Yes":
    while True:                                      # If the user input Yes this code takes the logins of the user and
        login1 = input("Enter your username here :") # retrieve it from the users txt.
        login2 = input("Enter your password here :")
        file = open(login1+".txt", "r")
        data = file.readline()
        file.close()
        if data == login1+","+login2:
            print(" Welcome " + login1)
        else:
            print("Incorrect Username or Password") #This code lets the user know if the login details where accurate
            break


import string
import login
while True:
    print("Welcome to Method&Tools Group 1 Shopping!")
    print("\t")
    print("1.Login")
    print("2.Create Account")
    print("3.Exit")
    print("\t")
    print("What would you like to do?")
    option = input("Command: ")
    print("\t")

    if option == "1":
        print("I work!")  

    elif option == "2":
        p1 = login.LoggingIn()
        print(p1.createAccount())
        print("What would you like to login: ")
        print("1.Yes")
        print("2.No")
        option = input("Command: ")
        if option == "1":
            login()
        elif option == "2":
            break
        else:
            print("No such option please try again.")
            print("\t")


    elif option == "3":
        print("Exiting the Program")
        break

    else:
        print("No such option please try again.")
        print("\t")
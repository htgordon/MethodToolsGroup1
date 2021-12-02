import string
import login
import user
import book
import movie
import activeUser
import cart

activeUser.init()

def menu():
    while True:
        print("Method&Tools 1 Shopping Menu")
        print("\t")
        print("1. Search for item")
        print("2. Cart")
        print("3. Order History")
        print("4. Account Settings")
        print("5. Log Out")
        print("6. Exit")
        print("\t")
        print("What would you like to do?")
        option = input("Command: ")
        print("\t")

        if option == "1":
            while True:
                print("1. Books")
                print("2. Movies")
                print("\t")
                input("Which items are you searching for: ")
                print("\t")
                if option == "1":
                    while True:
                        p5 = book.Book()
                        print(p5.displayAll())
                        print("\t")
                if option == "2":
                    while True:
                        p6 = movie.Movie()
                        print(p6.displayAll())
                        print("\t")
                else:
                    print("No such option please try again.")
                    print("\t")
        if option == "2":
            while True:        
                file1 = open('classCart.txt', 'r')
                Items = file1.readlines()
                print("Name  |  Price  |  Quantity  |  Type")

                i = 0
                for j in Items:
                    currItem = Items[i]
                    currItemArray = currItem.split("|")
                    if currItemArray[0] == activeUser.activeUserName:                    
                        print(currItemArray[1], " | ", currItemArray[2], " | ", currItemArray[3], " | ", currItemArray[4])
                    i += 1
                print("1. Add an item to cart")
                print("2. Remove an item from cart")
                print("3. Checkout")
                print("4. Go back")
                print("\t")
                input("Would you like you with your cart?")
                print("\t")
                if option == "1":
                    print("1. Books")
                    print("2. Movies")
                    print("\t")
                    input("Which items are you searching for: ")
                    print("\t")
                    if option == "1":
                        while True:
                            p5 = book.Book()
                            print(p5.displayAll())
                            print("\t")
                    if option == "2":
                        while True:
                            p6 = movie.Movie()
                            print(p6.displayAll())
                            print("\t")
                    else:
                        print("No such option please try again.")
                        print("\t")
                elif option == "2":
                    remname = input("What item would you like to remove?")
                    print("\t")
                    p7 = cart.cart()
                    print(p7.removeItem(remname))
                    print("\t")
                elif option == "3":
                    p8 = cart.cart()
                    print(p8.checkOut())
                    print("Your items have been checked out!")
                elif option == "4":
                    menu()
                else:
                    print("No such option please try again.")
                    print("\t")
        if option == "3":
            while True:
                print("Order History: ")
                print("\t")
        if option == "4":
            while True:
                print("1. Update Information")
                print("2. Delete Account")
                print("3. Go Back")
                print("4. Logout")
                print("\t")
                print("What would you like to do with your account?")
                option = input("Command: ")
                print("\t")
                if option == "1":
                    p4 = user.User()
                    print(p4.update())
                    menu()
                if option == "2":
                    print("Are you sure you want to delete your account?")
                    print("1. Yes")
                    print("2. No")
                    option = input(": ")
                    if option == "1":
                        p3 = user.User()
                        print(p3.deleteAccount())
                        loginMenu()
                    if option == "2":
                        menu()
                    else:
                        print("No such option please try again.")
                        print("\t")
                if option == "3":
                    menu()
                if option == "4":
                    loginMenu()
                else:
                    print("No such option please try again.")
                    print("\t")
        if option == "5":
            print("Logging Out...")
            loginMenu()
        if option == "6":
            print("Exiting..")
            exit(0)
        else:
            print("No such option please try again.")
            print("\t")
def loginMenu():
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
            p2 = login.LoggingIn()
            print(p2.logOn())
            menu()
            
        elif option == "2":
            p1 = login.LoggingIn()
            print(p1.createAccount())
            print("Would you like to login: ")
            print("1.Yes")
            print("2.No")
            option = input("Command: ")
            if option == "1":
                p2 = login.LoggingIn()
                print(p2.logOn())
                menu()
            elif option == "2":
                break
            else:
                print("No such option please try again.")
                print("\t")
                
        elif option == "3":
            print("Exiting.....")
            break
        else:
            print("No such option please try again.")
            print("\t")
loginMenu()

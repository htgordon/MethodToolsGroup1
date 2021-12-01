class User:
    def update(self):
        print("1. Username")
        print("2. Password")
        print("3. Address")
        print("4. Card information")
        option = input("Which one would you like to change: ")
        
       if option = "1":
            while True:
                userName = input("Username: ")
                print("\t")
                string = userName
                if len(string) > 20:
                    print("Character exceeds limit please make a username below 20 characters.")
                else:
                    #compare to file
                    file1 = open('classUser.txt', 'r')
                    Items = file1.readlines()
                    i = 0
                    exists = 0
                    for j in Items:
                        currItem = Items[i]
                        currItemArray = currItem.split("|")
                        if currItemArray[0] == userName:
                            exists = 1
                        i += 1
                    file1.close()
                    if exists == 1:
                        print ("Username already in use")
                    else:
                        break

        if option = "2":
            while True:
                password = input("Password: ")
                print("\t")
                string2 = password
                if len(string2) > 20:
                    print("Character exceeds limit please make a password below 20 characters.")
                else:
                    break
        if option = "3":
            while True:
                address = input("Address: ")
                print("\t")
                city = input("City: ")
                print("\t")
                state = input("State: ")
                print("\t")
                while True:
                    try:
                        zipcode = int(input("Zipcode: "))
                        break
                    except ValueError:
                        print("Please use numbers for the zipcode.")
                print("\t")
                print("Address = ", address)
                print("City = ", city)
                print("State = ", state)
                print("Zip = ", zipcode)
                print("\t")
                print("Is this correct?")
                print("1. Yes")
                print("2. No")
                option = input(": ")
                print("\t")
                if option == "1":
                    break
                print("\t")
            
        if option = "4":
            while True:
                while True:
                    try:
                        paymentInfo1 = int(input("Card Number: "))
                        break
                    except ValueError:
                        print("Please use numbers for the Card Number")
                print("\t")
                print("Example: 08/04")
                paymentInfo2 = input("Expiration Date: ")
                print("\t")
                print("Card Number: ", paymentInfo1)
                print("Expiration Date: ", paymentInfo2)
                print("\t")
                print("Is this correct?")
                print("1. Yes")
                print("2. No")
                option = input(": ")
                if option == "1":
                    break

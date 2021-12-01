class LoggingIn:
    def createAccount(self):
        print("Please input the information as asked")
        print("\t")
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
            
        while True:
            password = input("Password: ")
            print("\t")
            string2 = password
            if len(string2) > 20:
                print("Character exceeds limit please make a password below 20 characters.")
            else:
                break
            
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
        
        #writing to file
        zipcode = str(zipcode)
        paymentInfo1 = str(paymentInfo1)
        newUser = [userName, password, address, city, state, zipcode, paymentInfo1, paymentInfo2]
        newUser.insert(1, "|")
        newUser.insert(3, "|")
        newUser.insert(5, "|")
        newUser.insert(7, "|")
        newUser.insert(9, "|")
        newUser.insert(11, "|")
        newUser.insert(13, "|")
        file1 = open('classUser.txt', 'r')
        Items = file1.readlines()
        file1.close()
        Items.append(newUser)
        file1 = open('classUser.txt', 'w')
        i = 0
        for j in Items:
        	line = Items[i]
	        file1.writelines(line)
	        file1.writelines("\n")
	        i += 1
        file1.close()
                
        print("\t")
        print("Account Successfully Created!")
        
    def logOn(self):
        while True:
            userName = input("Username: ")
            password = input("Password: ")
            file1 = open('classUser.txt', 'r')
            Items = file1.readlines()
            i = 0
            match = 0
            for j in Items:
                currItem = Items[i]
                currItemArray = currItem.split("|")
                
                if userName == currItemArray[0]:
                    
                    if password == currItemArray[1]:
                        
                        match = 1
                i += 1
            if match != 1:
                print("The username or password is incorrect please try again.")
            else:
                break

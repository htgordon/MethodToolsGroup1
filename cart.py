class User:
    def update(self):
        print("1. Username")
        print("2. Password")
        print("3. Address")
        print("4. Card information")
        option = input("Which one would you like to change: ")
        
        if option == "1":
            while True:
                userName = input("Current Username: ")
                newUser = input("New Username:")
                print("\t")
                string = newUser
                if len(string) > 20:
                    print("Character exceeds limit please make a username below 20 characters.")
                else:
                    #compare to file
                    file1 = open('classUser.txt', 'r')
                    Items = file1.readlines()
                    i = 0
                    for j in Items:
                        currItem = Items[i]
                        currItemArray = currItem.split("|")
                        if currItemArray[0] == userName:
                            currItemArray[0] = newUser
                            currItemArray.insert(1, "|")
                            currItemArray.insert(3, "|")
                            currItemArray.insert(5, "|")
                            currItemArray.insert(7, "|")
                            currItemArray.insert(9, "|")
                            currItemArray.insert(11, "|")
                            currItemArray.insert(13, "|")
                            Items[i] = currItemArray
                        i += 1
                    file1.close()
                    file1 = open('classUser.txt', 'w')
                    i = 0
                    for j in Items:
                        line = Items[i]
                        file1.writelines(Items[i])
                        file1.writelines("\n")
                        i += 1
                    file1.close()
                    break

        if option == "2":
            while True:
                userName = input("Username: ")
                password = input("Password: ")
                print("\t")
                string2 = password
                if len(string2) > 20:
                    print("Character exceeds limit please make a password below 20 characters.")
                else:            
                    #compare to file
                    file1 = open('classUser.txt', 'r')
                    Items = file1.readlines()
                    i = 0
                    index = -1
                    for j in Items:
                        currItem = Items[i]
                        currItemArray = currItem.split("|")
                        if currItemArray[0] == userName:
                            currItemArray[1] = password
                            currItemArray.insert(1, "|")
                            currItemArray.insert(3, "|")
                            currItemArray.insert(5, "|")
                            currItemArray.insert(7, "|")
                            currItemArray.insert(9, "|")
                            currItemArray.insert(11, "|")
                            currItemArray.insert(13, "|")
                            Items[i] = currItemArray
                        i += 1
                    file1.close()
                    file1 = open('classUser.txt', 'w')
                    i = 0
                    for j in Items:
                        line = Items[i]
                        file1.writelines(line)
                        file1.writelines("\n")
                        i += 1
                    file1.close()
                break
        if option == "3":
            while True:
                userName = input("Username: ")
                address = input("Address: ")
                #compare to file
                file1 = open('classUser.txt', 'r')
                Items = file1.readlines()
                i = 0
                index = -1
                for j in Items:
                    currItem = Items[i]
                    currItemArray = currItem.split("|")
                    if currItemArray[0] == userName:
                        currItemArray[2] = address
                        currItemArray.insert(1, "|")
                        currItemArray.insert(3, "|")
                        currItemArray.insert(5, "|")
                        currItemArray.insert(7, "|")
                        currItemArray.insert(9, "|")
                        currItemArray.insert(11, "|")
                        currItemArray.insert(13, "|")
                        Items[i] = currItemArray
                    i += 1
                file1.close()
                file1 = open('classUser.txt', 'w')
                i = 0
                for j in Items:
                    line = Items[i]
                    file1.writelines(line)
                    file1.writelines("\n")
                    i += 1
                file1.close()
                break
        if option == "4":
            while True:
                userName = input("Username: ")
                paymentInfo1 = input("Card Number: ")
                paymentInfo2 = input("Expiry Date: ")
                #compare to file
                file1 = open('classUser.txt', 'r')
                Items = file1.readlines()
                i = 0
                index = -1
                for j in Items:
                    currItem = Items[i]
                    currItemArray = currItem.split("|")
                    if currItemArray[0] == userName:
                        currItemArray[6] = paymentInfo1
                        currItemArray[7] = paymentInfo2
                        currItemArray.insert(1, "|")
                        currItemArray.insert(3, "|")
                        currItemArray.insert(5, "|")
                        currItemArray.insert(7, "|")
                        currItemArray.insert(9, "|")
                        currItemArray.insert(11, "|")
                        currItemArray.insert(13, "|")
                        Items[i] = currItemArray
                    i += 1
                file1.close()
                file1 = open('classUser.txt', 'w')
                i = 0
                for j in Items:
                    line = Items[i]
                    file1.writelines(line)
                    file1.writelines("\n")
                    i += 1
                file1.close()
                break
    def deleteAccount(self):
        userName = input("Username: ")
        #delete user
        file1 = open('classUser.txt', 'r')
        Items = file1.readlines()
        i = 0
        index = -1
        for j in Items:
            currItem = Items[i]
            currItemArray = currItem.split("|")
            if currItemArray[0] == userName:
                index = i
            i += 1
        Items.pop(index)
        file1.close()
        file1 = open('classUser.txt', 'w')
        file1.writelines(Items)
        file1.close()
        print("Account deleted\n")

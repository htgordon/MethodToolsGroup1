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
            
        if option = "4":

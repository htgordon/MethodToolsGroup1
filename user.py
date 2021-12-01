class User:
    
    def deleteAccount(self):
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

import activeUser

class cart:
    def addItem(itemName, itemClass):
        if itemClass == "classBooks.txt":
            file1 = open('classBooks.txt', 'r')
            Items = file1.readlines()
            i = 0
            exists = 0
            index = -1
            price = " "
            for j in Items:
                currItem = Items[i]
                currItemArray = currItem.split("|")
                if currItemArray[0] == itemName:
                    price = currItemArray[1]
                    exists = 1
                    index = i
                i += 1
            file1.close()
            userName = activeUser.activeUserName
            file1 = open('classCart.txt', 'r')
            Items = file1.readlines()
            i = 0
            exists = 0
            index = -1
            for j in Items:
                currItem = Items[i]
                currItemArray = currItem.split("|")
                if currItemArray[0] == userName:
                    if currItemArray[1] == itemName:
                        exists = 1
                        quantity = currItemArray[3]
                        quantity = int(quantity)
                        quantity += 1
                        index = i
                i += 1
            file1.close()
            if exists == 0:
                newItem = [userName, itemName, price, "1", "Book"]
                newItem.insert(1, "|")
                newItem.insert(3, "|")
                newItem.insert(5, "|")
                newItem.insert(7, "|")
                Items.append(newItem)
                file1 = open('classCart.txt', 'w')
                i = 0
                for j in Items:
                    line = Items[i]
                    print(line)
                    file1.writelines(line)
                    file1.writelines("\n")
                    i += 1
                file1.close()
            else:
                print("Quant:")
                print (quantity)
                quantity = str(quantity)
                print(index)
                line = Items[index].split("|")
                line.pop(3)
                line.insert(3, str(quantity))
                line.insert(1, "|")
                line.insert(3, "|")
                line.insert(5, "|")
                line.insert(7, "|")
                Items[index] = line
                file1 = open('classCart.txt', 'w')
                i = 0
                for j in Items:
                    line = Items[i]
                    file1.writelines(line)
                    i += 1
                file1.close()
        elif itemClass == "classMovies.txt":
            file1 = open('classMovies.txt', 'r')
            Items = file1.readlines()
            i = 0
            exists = 0
            index = -1
            price = " "
            for j in Items:
                currItem = Items[i]
                currItemArray = currItem.split("|")
                if currItemArray[0] == itemName:
                    price = currItemArray[1]
                    exists = 1
                    index = i
                i += 1
            file1.close()
            userName = activeUser.activeUserName
            file1 = open('classCart.txt', 'r')
            Items = file1.readlines()
            i = 0
            exists = 0
            index = -1
            for j in Items:
                currItem = Items[i]
                currItemArray = currItem.split("|")
                if currItemArray[0] == userName:
                    if currItemArray[1] == itemName:
                        exists = 1
                        quantity = currItemArray[3]
                        quantity = int(quantity)
                        quantity += 1
                        index = i
                i += 1
            file1.close()
            if exists == 0:
                newItem = [userName, itemName, price, "1", "Movie"]
                newItem.insert(1, "|")
                newItem.insert(3, "|")
                newItem.insert(5, "|")
                newItem.insert(7, "|")
                Items.append(newItem)
                file1 = open('classCart.txt', 'w')
                i = 0
                for j in Items:
                    line = Items[i]
                    print(line)
                    file1.writelines(line)
                    file1.writelines("\n")
                    i += 1
                file1.close()
            else:
                print("Quant:")
                print (quantity)
                quantity = str(quantity)
                print(index)
                line = Items[index].split("|")
                line.pop(3)
                line.insert(3, str(quantity))
                line.insert(1, "|")
                line.insert(3, "|")
                line.insert(5, "|")
                line.insert(7, "|")
                Items[index] = line
                file1 = open('classCart.txt', 'w')
                i = 0
                for j in Items:
                    line = Items[i]
                    file1.writelines(line)
                    i += 1
                file1.close()
        
    def removeItem(itemName):
        userName = activeUser.activeUserName
        if True:
            file1 = open('classCart.txt', 'r')
            Items = file1.readlines()
            i = 0
            exists = 0
            index = -1
            for j in Items:
                currItem = Items[i]
                currItemArray = currItem.split("|")
                if currItemArray[0] == userName:
                    if currItemArray[1] == itemName:
                        exists = 1
                        index = i
                i += 1
            file1.close()
            if exists == 1:
                line = Items[index].split("|")
                quant = line[3]
                quant = int(quant)
                if quant > 1:
                    quant -= 1
                    quant = str(quant)
                    line[3] = quant
                    line.insert(1, "|")
                    line.insert(3, "|")
                    line.insert(5, "|")
                    line.insert(7, "|")
                    Items[index] = line
                    file1 = open('classCart.txt', 'w')
                    i = 0
                    for j in Items:
                        line = Items[i]
                        file1.writelines(line)
                        i += 1
                    file1.close()
                else:
                    Items.pop(index)
                
                
    def checkOut(self):            
        file1 = open('classCart.txt', 'r')
        Items = file1.readlines()
        file2 = open('classOrderHistory.txt', 'r')
        Items2 = file2.readlines()
        i = 0
        for j in Items:
            line = Items[i]
            Items2.append(line)
            i += 1
        file1.close()
        file2.close()
        file3 = open('classOrderHistory.txt', 'w')
        i = 0
        for j in Items:
            line = Items2[i]
            file3.writelines(line)
            i += 1
        file1.close()
        file1 = open('classCart.txt', 'w')
        file1.write("\n")
        file1.close()
                
                
                
                
                
                
                
                

import activeUser

class Cart:
	def addItem(itemName, itemClass):
		print("in cart")
		print("itemName: " + itemName)
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
					print (currItemArray[0])    
					#print (currItemArray[1])
					#price = currItemArray[1]
					exists = 1
					index = i
				i += 1
			file1.close()
			userName = activeUser.activeUserName
			quantity = 1
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
						quantity = currItemArray[2]
						print(quantity)
						quantity += 1
				i += 1
			file1.close()
			quantity = str(quantity)
			print("before write")
			newItem = [userName, itemName, price, quantity, "classBooks"]
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
        
        
        
        
    
        

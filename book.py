class Book:
  def displayAll(self):
        # readlines()
        file1 = open('classBooks.txt', 'r')
        Items = file1.readlines()

        # prints to command line, not needed for final
        #Read first element from each item
        i = 0
        for j in Items:
            currItem = Items[i]
            currItemArray = currItem.split("|")
            print(currItemArray[0] + "\n")
            i += 1
        
        option = input("Which book would you like to look more at: ")
        #compare to file
        file1 = open('classBooks.txt', 'r')
        Items = file1.readlines()
        i = 0
        exists = 0
        for j in Items:
        currItem = Items[i]
        currItemArray = currItem.split("|")
        if currItemArray[0] == option:
          if exists = 1:
            
            print("What would you like to do next: ")
            print("1. Add book to cart")
            print("2. Go Back")
            option = input(": ")
                  if option == "1":
                    print("1")
                  if option == "2":
                    displayAll()
          i += 1
          file1.close()
        

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
          exists = 1
          i += 1
          file1.close()

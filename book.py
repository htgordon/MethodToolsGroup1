import activeUser
import cart

from cart import *

class Book:
  def displayAll(self):
    while True:
        # readlines()
        file1 = open('classBooks.txt', 'r')
        Items = file1.readlines()

        #     s to command line, not needed for final
        #Read first element from each item
        i = 0
        for j in Items:
            currItem = Items[i]
            currItemArray = currItem.split("|")
            print(currItemArray[0] + "\n")
            bookName = currItemArray[0]
            i += 1
        
        option = input("Which book would you like to look more at: ")
        bookName = option
        #compare to file
        file1 = open('classBooks.txt', 'r')
        Items = file1.readlines()
        i = 0
        exists = 0
        index = -1
        for j in Items:
            currItem = Items[i]
            currItemArray = currItem.split("|")
            if currItemArray[0] == option:
                exists = 1
                index = i
            i += 1
        file1.close()
        if exists != 1:
                ("Book does not exist\n")
        else:
                print(Items[index])
                print("What would you like to do next: ")
                print("1. Add book to cart")
                print("2. Go Back")
                option = input(": ")
                if option == "1":
                    cart.addItem(bookName, "classBooks.txt")
                    break
                if option == "2":
                    break

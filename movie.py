import activeUser

class Movie:
  def displayAll(self):
    while True:
        # readlines()
        file1 = open('classMovies.txt', 'r')
        Items = file1.readlines()

        #     s to command line, not needed for final
        #Read first element from each item
        i = 0
        for j in Items:
            currItem = Items[i]
            currItemArray = currItem.split("|")
            print(currItemArray[0] + "\n")
            i += 1
        
        option = input("Which movie would you like to look more at: ")
        #compare to file
        file1 = open('classMovies.txt', 'r')
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
                ("Movie does not exist\n")
        else:
                print(Items[index])
                print("What would you like to do next: ")
                print("1. Add movie to cart")
                print("2. Go Back")
                option = input(": ")
                if option == "1":
                    p1 = cart.Cart()
                    print(p1.addItem(option, 'classMovies.txt'))
                    print("Movie was added to your cart!")
                if option == "2":
                    break

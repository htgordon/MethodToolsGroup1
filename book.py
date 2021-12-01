class Book:
  def displayAll(self):
        # readlines()
        file1 = open('classBooks.txt', 'r')
        Lines = file1.readlines()

        # prints to command line, not needed for final
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

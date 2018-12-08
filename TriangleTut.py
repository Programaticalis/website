def rectangle():
    row = int (input("Enter row number: " ))
    col = int (input("Enter column number: "))
    num = 1
    for h in range (row):
        for l in range (col):
            print (num, end="\t")
            num += 1
        print()

def triangle():
    lim = int (input("Enter limit number: " ))
    #col = int (input("Enter column number: "))
    num = 1
    for h in range (lim):
        for l in range (h+1):
            print (num, end="\t")
            num += 1
        print()

def square():
    lim = int (input("Enter limit number: " ))
    #col = int (input("Enter column number: "))
    num = 1
    for h in range (lim):
        for l in range (lim):
            print (num, end="\t")
            num += 1
        print()


if __name__ == "__main__":
    square()    
    #triangle()

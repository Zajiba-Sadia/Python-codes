def first():
    print("Hello")
    #break


def second():
    print("World")
    #break


def menu():
    l = 1
    while l <= 5:
        i = int(input("Enter 1 to search, enter 2 to edit"))
        if i == 1:
            first()
            #break
        elif i == 2:
            second()
            #break
        else:
            print("Invalid entry")
            #break
        l = l+1

menu()



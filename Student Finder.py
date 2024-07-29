lst1 = {}
def finder():
    a = int(input("Press 1 to search, 2 to add: "))
    if a == 1:
        search(lst1)
    elif a == 2:
        add()
    else:
        print("Invalid entry")

def search(t):

    if t:
        b = input("Enter the ID you are looking for: ")
        if b in t:
            print(lst1[b])

        else:
            print("Cannot find the student")
            #finder()
    else:
        print("There are no entries in database, do you want to add?")
        d = input("yes or no?")
        if d == "yes":
            add()
        elif d == "no":
            print("Goodbye!")

def add():

    c = int(input("Enter the number of students you want to add: "))
    for i in range(0, c):
        id = input("Enter the ID of the student")
        name = input("Enter the name of the student: ")
        lst1[id] = name
        print(lst1)
    finder()
    #search(lst1)





finder()
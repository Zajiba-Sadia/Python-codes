stu_base = {}
def base(j):

    if j == 2:
        search(stu_base)
    else:
        n = int(input("Enter the number of entries: "))
        for i in range(0, n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            stu_base[key] = value
            stu_base.update(stu_base)
        print("Dictionary after adding user",stu_base)
        # search(stu_base)



def search(y):
    print(y)
    if y:
        print("There are a lot of students. Which one are you looking for ?")
        u_input = input("Enter an ID: ")
        if u_input in y:
            x = y[u_input]
            print(x)
    else:
        print("there is no student. Taking you to main menu")
        menu()


def menu():
    l = 1
    while l <= 5:
        i = int(input("Enter 1 to edit, enter 2 to search"))
        if i == 1:
            base(i)

            #break
        elif i == 2:
            base(i)
            #break
        else:
            print("Invalid entry")
            #break
        l = l+1

menu()


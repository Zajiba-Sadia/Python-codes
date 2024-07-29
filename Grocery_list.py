lst1 = {}
def menu():
    b = input("Press 1 to search, 2 to add to list, 3 to see total price ")
    if b == "1":
        search(lst1)
    elif b == "2":
        add()
    elif b == "3":
        price(lst1)
    else:
        print("Invalid entry")

def search(y):
    if y:
        c = input("Enter name of item to search: ")
        if c in y:
            print(y[c])
        else:
            print("Not found")
            menu()
    else:
        print("The list is empty")
        menu()

def add():
    a = int(input("Enter the number of elements you want to add"))
    for i in range(0, a):
        item = input("Enter name of item: ")
        price = input("Enter price of item")
        weight = input("Enter weight of item")
        sub_lst = [price, weight]

        lst1[item] = sub_lst

        item_price = lst1[item]
        for i in range(0,len(item_price)):
            item_price[i] = int(item_price[i])


    print(f"The shopping list is", lst1)


    menu()

def price(x):
    total_price = 0
    if x:
        #item_price = x[item]
        for value in x.values():
            dam = value[0]
            total_price += dam

        #total_price = sum(value[0] for value in x.values())
        print(f"The total price of the items is: {total_price}")
    else:
        print("The list is empty again")
        menu()


menu()

def search():
    u_input = input("Enter an ID: ")
    if u_input == key:
        x = stu_base[u_input]
        print(x)
    else:
        print("Does not exist")

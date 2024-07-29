def base():
    stu_base = {}
    n = int(input("Enter the number of entries: "))
    for i in range(0, n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        stu_base[key] = value

    u_input = input("Enter an ID: ")
    if u_input in stu_base:
     x = stu_base[u_input]
     print(x)
    else:
     print("Does not exist")

    print("Dictionary after adding user",stu_base)

base()


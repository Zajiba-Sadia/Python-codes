def dictio():
    n = int(input("Enter the number of dictionary elements: "))
    students = {}
    for i in range(0, n):
        name = input("Enter the name of the student: ")
        age = input("Enter the age of the student: ")
        students[name] = age

    print(students)
    search_stu(students)


def search_stu(a):
    p = 0
    while p < 3:
        m = input("Search the name of the student: ")
        for k in a:
            if m in k:
                print(a[m])
                break
        else:
            print("Name not found: ")
        p = p +1

dictio()




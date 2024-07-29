def lst():
    l1 = []
    n1 = int(input("Enter the number of elements of the first list"))
    for i in range(0, n1):
        e1 = int(input())
        l1.append(e1)
    l2 = []
    n2 = int(input("Enter the number of elements of the second list"))
    for j in range(0, n2):
        e2 = int(input())
        l2.append(e2)
    l3 = []
    for i in l1:
        if i != j:
            l3.append(i)
    print(l3)

lst()


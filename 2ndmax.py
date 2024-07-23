def make():
    list = []
    len = int(input("Enter the total numbers in the list "))
    for i in range(0, len):
        numb = int(input())
        list.append(numb)
    print(list)
    #To sort the list in the ascending order
    list.sort()
    print(list[-2])

make()
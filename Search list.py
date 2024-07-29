def lst():
    lst1 = []
    length = int(input("Enter the length of the list: "))
    for i in range(0, length):
        a = input("Enter a number you like")
        lst1.append(a)
    srch(lst1)

def srch(k):
    lst2 = []
    p = 0
    while p < 3:
        b = input("Search the number")
        for j in k:

            if b == j:

                lst2.append(b)
                print("Found one!", lst2)
                break
        else:
            print("Sorry, not the number")


        p = p+1
lst()
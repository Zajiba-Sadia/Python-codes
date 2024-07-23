def calc():
    list1 = []
    for i in range(0,4):
        l = int(input("Enter a number"))
        list1.append(l)
    print(list1)
    a = list1[0] +list1[1]
    print("The sum of the first 2 numbers is ", a)
    b = a * list1[2]
    print("The multiplication with the third number is ", b)
    c = b - list1[3]
    print("Subtracting the fourth number we get: ", c)
    print(c)
    return c
#calc()

def stars():
    ran = calc()
    i = 0
    while i<ran:
        for j in range(0,i+1):
            print("*", end="\t")
        i = i + 1
        print(i)

stars()


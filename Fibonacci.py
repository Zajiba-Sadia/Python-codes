#num = int(input("Enter a number: "))

#f1 = 0
#f2 = 1
#f3 = f1 + f2
#f = 0
#f1 = 0
#for i in range(1, num):
   # f = i + f
    #f1 = f1 + f
#print(f1)


def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program
print(Fibonacci(6))
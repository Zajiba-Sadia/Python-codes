fact = int(input("Enter a number"))
f = 1
if fact == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, fact+1):
        f = f * i
    print("The factorial of", fact, "is", f)

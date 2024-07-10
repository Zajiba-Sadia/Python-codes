try:
    Num = int(input("Enter the number you want to check: "))
except:
    print("Invalid input")

Mod = Num % 2
if Mod == 0:
    print("It is an even number")
else:
    print("It is an odd number")

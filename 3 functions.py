def variable():
    inp = int(input("Enter an integer value: "))
    add(inp) #passing the value of input to a function.

s = 0
def add(k):
    s = k + 10
    show(s)

def show(j):
    print(j)

variable()


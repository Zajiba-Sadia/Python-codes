def variable():
    a = int(input("Enter an integer value: "))
    add(a)
def add(i):
    s = 0
    s = i + 35
    pnt(s)
    minus(s)


def pnt(j):
    print("Adding 35 to the given number we get", j)

def minus(k):
    m = 0
    m = k - 10
    pnt2(k, m)

def pnt2(q,l):
    print(f"Subtracting 10 from {q} we get {l}")


variable()
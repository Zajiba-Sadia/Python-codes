list1 = []
len1= int(input("Enter the number of elements for first list:"))
for i in range(0,len1):
    num1 = int(input())
    list1.append(num1)
list2 = []
len2= int(input("Enter the number of elements for second list:"))
for j in range(0,len2):
    num2 = int(input())
    list2.append(num2)
l = []
for i in list1:
    for j in list2:
        if i==j and i !=l:
         l.append(i)

print(l)

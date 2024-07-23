def merge(list1, list2):
    new_list = list1 + list2
    new_list.sort()
    return new_list
list1 = []
len1 = int(input("Enter no. of elements for list 1: "))
for i in range(0,len1):
    num1 = int(input())
    list1.append(num1)
    list1.sort()
list2 = []
len2 = int(input("Enter no. of elements for list 2: "))
for j in range(0,len2):
    num2 = int(input())
    list2.append(num2)
    list2.sort()
result = merge(list1, list2)
print(result)
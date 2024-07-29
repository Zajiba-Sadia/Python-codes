a = [1,2,3,4,5]
b = [2,30,4,1]
c =[]
for i in a:
    flag = "False"
    for j in b:
        if i == j:
            # print(i)
            flag = "True"
        else:
            print("")

    if flag == "False":
        print(i)



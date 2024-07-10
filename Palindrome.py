check = input("Enter a word: ")
rev_str = ''.join(reversed(check))

if check == rev_str:
    print("Palindrome")
else:
    print("Not Palindrome")


#for i in (check[0], check[4]):
    #for j in (check[-1], check[-5]):
        #if i == j:
         #   print("Palindrome")
        #else:
         #   print("Normal")




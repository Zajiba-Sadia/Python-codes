string_name = input("Enter a word to check for palindrome: ")

for element in range(0, len(string_name)):
    print(string_name[element])

for i in range(len(string_name) - 1, 0 - 1, -1):
    print(string_name[i])
if string_name[element] == string_name[i]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")


s = input("Enter a string: ")

# remove spaces and convert to lowercase
str1 = s.replace(" ", "").lower()

if str1 == str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
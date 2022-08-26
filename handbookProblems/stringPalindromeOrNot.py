# Check whether a string is palindrome

s = "level"
pali = ''
for i in s:
    pali=i+pali

if pali==s:
    print("String is palindrome")

else:
    print("String is not Palindrome")

def palindrome(soz):
    s=soz.lower().replace(" "," ")
    return s == s[::-1]

print(palindrome("madam"))  
print(palindrome("racecar"))  
print(palindrome("hello"))
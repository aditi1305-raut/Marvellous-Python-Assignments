
def Palindrome(s):
    s = s.replace(" "," ").lower()
    n = len(s)

    for i in range(n//2):
        if s[i] != s[n-1 -i]:
            return False
    return True


print("Enter a String: ")
string = input()


if Palindrome(string):
    print("The String is Palindrome")

else:
    print("String is not Palindrome")
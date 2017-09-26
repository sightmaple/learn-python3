def is_palindrome(n):
    if n>10:
        s = str(n)
        for i in range(len(s)):
            if s[i] == s[len(s)-1-i]:
                return True
            else:
                return False
output = list(filter(is_palindrome,range(0,1000)))
print(output)

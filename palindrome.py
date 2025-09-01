ef pal(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return pal(s[1:-1])
    return False

# Usage
s = "55"
print("Palindrome" if pal(s) else "Not Palindrome")

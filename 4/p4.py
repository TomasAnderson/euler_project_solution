def ispalindromic(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

print(max(x*y
    for x in range(100, 1000)
    for y in range(100, 1000)
    if ispalindromic(str(x*y))))

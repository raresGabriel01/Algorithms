#https://codeforces.com/problemset/problem/1023/A
x, y = input().split()
n, m = int(x), int(y)
s = input()
t = input()

if '*' not in s and s != t:
    print("NO")
elif '*' not in s and s==t:
    print("YES")
elif len(s) > len(t) + 1:
    print("NO")
elif s == "*":
    print("YES")
else:
    ok = True
    i = 0
    while s[i] != '*':
        if s[i] != t[i]:
            print("NO")
            ok = False
            break
        i += 1
    j,k=len(t)-1,len(s)-1
    while s[k] != '*' and ok:
        if s[k] != t[j]:
            ok = False
            print("NO")
            break
        k -= 1
        j -= 1
    if ok:
        print("YES")
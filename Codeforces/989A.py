#https://codeforces.com/problemset/problem/989/A

s = input()

ok = False
for i in range(len(s)-2):
        if 'A' in s[i:i+3] and 'B' in s[i:i+3] and 'C' in s[i:i+3]:
            ok = True
            print("YES")
            break
if not ok:
    print("NO")
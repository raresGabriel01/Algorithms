# https://codeforces.com/problemset/problem/1230/A

x, y, z, t = input().split()

a = [int(x), int(y), int(z), int(t)]

S = a[0] + a[1] + a[2] + a[3]

found = False

for i in range(len(a)-1):
    if found:
        break
    for j in range(i+1,len(a)):
        if a[i] + a[j] == S - a[i] - a[j]:
            found = True
            break

if a[0] + a[1] + a[2] == a[3] or  a[0] + a[1] + a[3] == a[2] or a[0] + a[3] + a[2] == a[1] or a[3] + a[1] + a[2] == a[0]:
    found = True

if found:
    print("YES")
else:
    print("NO")
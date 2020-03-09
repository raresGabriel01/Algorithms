#https://codeforces.com/problemset/problem/1/A
x, y, z = input().split()
n, m, a = int(x), int(y), int(z)

area = n * m

if n//a == n/a:
    r1 = n/a
else: r1 = n//a + 1

if m//a == m/a:
    r2 = m/a
else: r2 = m//a + 1

print(int(r1 * r2))
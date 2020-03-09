# http://codeforces.com/problemset/problem/977/A

a, b = input().split()

n, k = int(a), int(b)

for i in range(k) :
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1

print(n)
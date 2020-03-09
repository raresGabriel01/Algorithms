# https://codeforces.com/problemset/problem/1252/A

n = int(input())

perm = [int(a) for a in input().split()]

### we can obtain a valid permutation by using the following rule:      (can be mathematically proven)
### P[i] = perm[i] + 1, if perm[i] < n
### P[i] = 1, if perm[i] == n

P = []

for i in range(n):
    if perm[i] == n:
        P.append(1)
    else:
        P.append(perm[i]+1)


print(*P)


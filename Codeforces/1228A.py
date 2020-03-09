#https://codeforces.com/problemset/problem/1228/A

x, y = input().split()
l, r = int(x), int(y)

found = False

def hasDistinctDigits (c) :
    mySet = set()
    nrOfDigits = 0
    while c != 0:
        mySet.add(c%10)
        nrOfDigits += 1
        c //= 10
    if nrOfDigits != mySet.__len__():
        return False
    else:
        return True


for c in range(l, r+1):
    if hasDistinctDigits(c):
        found = True
        print(c)
        break

if not found :
    print(-1)

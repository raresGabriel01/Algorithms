# http://codeforces.com/problemset/problem/1248/A

t = int (input())

list = []

for test in range(t):
    n = int(input())
    impar1, par1, impar2, par2 = 0, 0, 0, 0

    v = input().split()
    for a in v:
        if int(a) % 2 == 0:
            par1 += 1
        else:
            impar1 += 1
    m = int(input())

    v = input().split()
    for a in v:
        if int(a) % 2 == 0:
            par2 += 1
        else:
            impar2 += 1
    list.append(impar1*impar2 + par1*par2)

for el in list:
    print(el)
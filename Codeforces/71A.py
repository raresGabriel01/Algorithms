#http://codeforces.com/problemset/problem/71/A

n = int(input())

list = []

for i in range(n):
    cuv = input()
    if len(cuv) > 10:
        list.append(cuv[0] + str(len(cuv)-2) + cuv[-1])
    else:
        list.append(cuv)

for el in list:
    print(el)

#https://codeforces.com/problemset/problem/1220/A
n = int(input())
text = input()

nrz, nrn = 0, 0

for ch in text:
    if ch == 'z':
        nrz += 1
    elif ch == 'n':
        nrn += 1

for i in range(nrn):
    print(1,end=" ")
for i in range(nrz):
    print(0,end=" ")

# COD
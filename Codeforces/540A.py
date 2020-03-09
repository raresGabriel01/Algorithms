#https://codeforces.com/problemset/problem/540/A

n = int(input())
act = input()
cod = input()

s = 0

for i in range(len(act)):
    s += min(abs(int(act[i])-int(cod[i])), abs(int(act[i]) + 10 - int(cod[i])), abs(-int(act[i]) + 10 + int(cod[i])))
print(s)
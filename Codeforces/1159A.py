# http://codeforces.com/problemset/problem/1159/A

n = int (input())
text = input()

nract, nrinit = 0, 0

for i in range(n):
    if text[i]=='+':
        nract += 1
    elif nract == 0:
        nrinit += 1
    else:
        nract -= 1

print(nrinit - len(text.replace('+','')) + len(text.replace('-','')))


#https://codeforces.com/problemset/problem/59/A

s = input()

lowerCaseNum, upperCaseNum = 0, 0

for ch in s:
    if ch.islower():
        lowerCaseNum += 1
    else:
        upperCaseNum += 1

if lowerCaseNum > upperCaseNum:
    print(s.lower())
elif lowerCaseNum < upperCaseNum:
    print(s.upper())
else:
    print(s.lower())

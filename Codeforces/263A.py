pozi, pozj = 0, 0

for i in range(5):
    if pozi != 0:
        break
    v = input().split()
    for j in range (5):
        if v[j] == '1':
            pozi = i+1
            pozj = j+1
            break




print(abs(3 - pozi ) + abs(3 - pozj))



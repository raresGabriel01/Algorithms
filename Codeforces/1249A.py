q = int(input())
list = []
for query in range(q):
    n = int(input())
    v = [int(x) for x in input().split()]
    v.sort()
    teamNr = 1
    for i in range(n-1):
        if abs(int(v[i+1])-int(v[i])) == 1 :
            teamNr += 1
            break
    list.append(teamNr)

for el in list:
    print(el)
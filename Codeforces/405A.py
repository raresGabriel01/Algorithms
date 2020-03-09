n = int(input())
v = input().split()
a = []
for el in v:
    a.append(int(el))
frecv = [0]*101
for el in a:
    frecv[el] += 1
for i in range(1,101):
    for j in range(frecv[i]):
        print(i,end=" ")
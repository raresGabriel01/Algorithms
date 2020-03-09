#https://codeforces.com/problemset/problem/556/A
n = int(input())
s = input()
isDel = [False]*(n)
delNr = 0

nextAfter = [0]*(n+1)
for j in range(n-1):
    nextAfter[j]=j+1
i=0
while i<n-1 :

    try:
        #print(i, s[i], s[nextAfter[i]])
        if (isDel[i])==False and (isDel[nextAfter[i]])==False :
            if s[i] != s[nextAfter[i]]:
                isDel[i] = True
                isDel[nextAfter[i]] = True
                nextAfter[i-1] = nextAfter[nextAfter[i]]
                delNr += 2
                i-=1
            else:
                i+=1
        else:
            i+=1

    except IndexError:
        i += 1

print(n-delNr)

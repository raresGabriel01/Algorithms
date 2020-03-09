# https://codeforces.com/problemset/problem/1184/A1
import math

r = int ( input () )

found = False


for x in range (1,int(math.sqrt(r))+1):
    y = ((r-1)/x - x - 1)/2
    if y == int(y) and x > 0 and y > 0:
        print(x,int(y))
        found = True
        break

if not found :
    print("NO")
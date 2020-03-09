#https://codeforces.com/problemset/problem/82/A

n = int(input())

k = 0

while n > 5*(2**k -1):
    k += 1

n -= 5*(2**(k-1)-1)
#print(k,"----",n)
if n <= 2**(k-1):
    print("Sheldon")
elif n<= 2**k:
    print("Leonard")
elif n<=3*2**(k-1):
    print("Penny")
elif n<=4*2**(k-1):
    print("Rajesh")
else:
    print("Howard")
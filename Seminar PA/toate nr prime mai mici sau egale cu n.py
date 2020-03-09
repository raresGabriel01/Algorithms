n = int (input ())
v = [True]*(n+1)        # v[i] = True if i is prime number

v[0], v[1] = False, False

nrPrime = []

for i in range(2,n+1):
    if v[i] == True:
        nrPrime.append(i)
        for j in range(i*i,n+1,i):      # complexitate O(n*log(logn)) ~ are legatura cu distributia numerelor prime
            v[j] = False

print(nrPrime)
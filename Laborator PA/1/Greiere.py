"""
Un greiere se deplasează efectuând câte o săritură, lungimea inițială a
săriturii fiind de x cm. După fiecare n sărituri, lungimea săriturii greierului se
micșorează cu p procente. Cunoscându-se valorile x,n,p, precum și numărul
de sărituri m pe care le face greierele, să se scrie un program care să afișeze
distanța parcursă de greiere. De exemplu, pentru x=20,n=10, p=10 și m=20
distanța parcursă de greiere este egală cu 380 cm, deoarece primele 10
sărituri efectuate au, fiecare, lungimea de 20 cm, iar următoarele 10 au,
fiecare, lungimea de 18 cm.
"""

#O parcurgere liniara

#citim datele

x = int(input("Introduceti lungimea initiala a sariturii: "))
n = int(input("Introduceti numarul de sarituri (n) dupa care lungimea sariturilor incepe sa scada: "))
p = int(input("Introduceti numarul p, reprezentand scaderea procentuala: "))
m = int(input("Introduceti numarul total de sarituri: "))

dist = 0        #distanta parcursa, initializata cu 0

for salt in range(1,m+1):       #pentru fiecare salt din cele m salturi
    dist += x                   #sarim o anumita distanta
    if salt % n == 0:           #daca au trecut n salturi
        x = x - p/100*x         #distanta cu care sarim scade

print(dist)                     #afisare rezultat


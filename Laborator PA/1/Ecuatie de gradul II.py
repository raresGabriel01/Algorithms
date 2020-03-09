"""
Se da o ecuatie de gradul II de o forma generala. Realizati un algoritm care sa determine radacinile acesteia
"""

# Vom citi coeficientii, dupa care calculam discriminantul delta si rezolvam ecuatia dupa cazuri
import math

a = int(input("Introduceti coeficientul termenului patratic: "))
b = int(input("Introduceti coeficientul termenului liniar: "))
c = int(input("Introduceti coeficientul termenului liber: "))

delta = b*b - 4*a*c         #discriminantul

if delta > 0:               #tratarea cazurilor
    sol1 = (-b-math.sqrt(delta)) / (2*a)
    sol2 = (-b+math.sqrt(delta)) / (2*a)        #aplicarea formulei
    print("Solutia 1 :",sol1)
    print("Solutia 2 :",sol2)       #afisare
elif delta == 0:
    print("O unica solutie reala :",(-b)/(2*a))     #analog
else:
    img = math.sqrt(-delta)/(2*a)
    real = -b/(2*a)
    print("Solutie complexa 1:",real,"+ i *",img)   #mic artificiu pentru a putea afisa radacinile complexe
    print("Solutie complexa 2:",real,"- i *",img)
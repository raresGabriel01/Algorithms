"""
O metodă simplă (dar nesigură!!!) de criptare a unui text o reprezintă cifrul lui Cezar, prin care
fiecare literă dintr-un text dat este înlocuită cu litera aflată peste 𝑘𝑘 poziții la dreapta în alfabet în mod
circular. Valoarea 𝑘𝑘 reprezintă cheia secretă comună pe care trebuie să o cunoască atât expeditorul,
cât și destinatarul mesajului criptat. Decriptarea unui text constă în înlocuirea fiecărei litere din textul
criptat cu litera aflată peste 𝑘𝑘 poziții la stânga în alfabet în mod circular. Scrieți un program care să
realizeze criptarea sau decriptarea unui text folosind cifrul lui Cezar. Indicație de rezolvare: se va
utiliza formula 𝑒𝑒𝑘𝑘(𝑥𝑥) = (𝑥𝑥 + 𝑘𝑘) mod 26 pentru criptarea unui caracter 𝑥𝑥 folosind cheia secretă 𝑘𝑘,
respectiv formula 𝑑𝑑𝑘𝑘(𝑥𝑥) = (𝑥𝑥 − 𝑘𝑘) mod 26 pentru decriptare. De asemenea, se vor utiliza funcțiile
ord și chr pentru manipularea caracterelor.
"""

#print(ord('a'),ord('z'),ord('A'),ord('Z'),ord(' '))                            #97 122 65 90 32

#vom utiliza metodele ord() si chr() care transforma un caracter in valoarea lui numerica si invers

#pentru a muta un caracter cu k pozitii mai la dreapta este suficient sa utilizam o sintaxa de genul
# caracter = chr(ord(caracter) + k))
# problema apare in momentul in care ord(character) + k depaseste intervalul de numere al literelor alfabetului latin
# astfel, nu vom folosi de proprietatile >>>  %  <<<

# sa spunem ca vrem sa criptam caracterul ch cu cheia k
# procedam astfel:
# il introducem in intervalul [1,26] (pentru ca sunt 26 litere in alfabetul latin) prin ord(ch) - ord(a)
# il mutam k pozitii la dreapta (adica il "crestem") , adica ord(ch) - ord(a) + k
# vom afla restul impartirii la 26, pentru a fi siguri ca nu iese din [1,26] (ord(ch) - ord(a) + k)%26
# facem asa pentru ca 29 este tot una cu 3 (ganditi-va ca numaratoarea incepe de la capat in momentul in care iesi din index)
# dupa care incadram inapoi in codul obisnuit, adunand un ord(a)
# (ord(ch) - ord(a) + k)%26 + ord(a)
# convertim in cele din urma valoarea aceasta numerica cu valoarea str, utilizand metoda chr()

# se procedeaza analog pentru decriptare si pentru literele mari
# in acest program ignoram pur si simplu spatiile, insa si ele pot fi criptate (cu alte simboluri, etc)

sir = input("Introduceti sirul :")
k = int(input("Introduceti cheia: "))       #citim

k = k % 26      # ne usureaza munca, sa te muti 28 de pozitii la stanga e tot una cu a te muta 2 pozitii, fiindca numaratoarea o ia de la capat
                # cand treci de 26

def criptare(ch):
    if ord(ch) <= ord('z') and ord(ch) >= ord('a'):
        return chr(((ord(ch) - ord('a') + k) % 26) + ord('a'))
    elif ord(ch) <= ord('Z') and ord(ch) >= ord('A'):                   #facem exact ce am prezentat mai sus
        return chr(((ord(ch) - ord('A') + k) % 26) + ord('A'))
    else:
        return ch


def decriptare(ch):
    if ord(ch) <= ord('z') and ord(ch) >= ord('a'):
        return chr(((ord(ch) - ord('a') - k) % 26) + ord('a'))
    elif ord(ch) <= ord('Z') and ord(ch) >= ord('A'):           #analog
        return chr(((ord(ch) - ord('A') - k) % 26) + ord('A'))
    else:
        return ch

sirNou = ''
print("Optiuni: 1 - Criptare ; 2 - Decriptare \n")
                                                       # ce dorim sa facem cu sirul dat
op = int(input("Introduceti optiunea dumneavoastra: "))

if op == 1 :
    for ch in sir:
        sirNou += str(criptare(ch))
else :                                                  #criptam/decriptam caracter cu caracter
    for ch in sir:
        sirNou += str(decriptare(ch))

print(sirNou)                           # afisare
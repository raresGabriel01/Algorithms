"""
Se cere prelucrarea unui discuții dintre persoana A, care vinde un obiect, și persoana B, care oferă
bani pentru el. O astfel de discuție se poate desfășura în modul următor:
• “Eu am de gând să vând vaza aceasta pentru $5. Ce plăcut, chiar mi-ar plăcea să o achiziționez,
doar că am numai $3 la mine. Este suficient? Nu, insist să obțin 5$ pe ea. Bine, atunci voi scoate
niște bani și-ți aduc cei $5.”
• “Salut, am văzut în acel anunț că vindeți o mașină second-hand. M-ar interesa s-o achiziționez
pentru suma de $2700. Vă amintesc că suma din anunț este de $3000, sir. Desigur. Și totuși, n-am
putea ajunge la mijloc? $2850? $2850 de dolari, spuneți? Mi se pare corect, s-a făcut.”
După cum se poate observa din exemple, regulile sunt acestea:
• se știe că fiecare persoană face câte o ofertă, pe rând, iar suma se apropie spre o valoare aflată
între primele două oferte.
• Considerăm că persoana A este cea care oferă, cum este și logic :), prețul mai mare dintre primele
două oferte.
• Când ultimele două oferte sunt egale, știm că cele două persoane au ajuns la un acord comun (*).
Cerințe:
a) Extrageți din text primele două valori. (hint: orice sumă este un număr după semnul $ în șir)
b) Decideți dacă cele două persoane “s-au înțeles” :). (vezi (*))
"""

#utilizam metoda split()
#astfel, determinam primele 2 si ultimele 2 valori
# pentru a) afisam valorile
# pentru b) verificam daca ultimele doua valori sunt identice si afisam mesajul corespunzator

#iti dau max $5. hai un $8. Mai mult de $7 la mine nu am si nu cred ca vrei sa astepti. Hai, fie $7
text = input("Introduceti textul: ")

firstVal, secondVal = '', ''
lastVal, secondLastVal = '', ''
for cuv in text.split():            #pentru fiecare cuvant din text
    if '$' in cuv and firstVal == '':       #daca gasim o suma
        firstVal = cuv.replace('$','')  #o atribuim corespunzator
    elif '$' in cuv and secondVal == '':
        secondVal = cuv.replace('$','')
    elif secondVal != '' and firstVal != '':
        break

for cuv in text.split():        #analog
    if '$' in cuv:
        secondLastVal = lastVal
        lastVal = cuv.replace('$','')

firstVal = firstVal.replace('.','')
firstVal = firstVal.replace(',','')
firstVal = firstVal.replace('?','')

secondVal = secondVal.replace('.','')
secondVal = secondVal.replace(',','')       #eliminam eventualele semne de punctuatie lipite de valorile numerice
secondVal = secondVal.replace('?','')       #mai pot fi si altele, dar asta e doar pur exemplu

lastVal = lastVal.replace('.','')
lastVal = lastVal.replace(',','')
lastVal = lastVal.replace('?','')

secondLastVal = secondLastVal.replace('.','')
secondLastVal = secondLastVal.replace(',','')
secondLastVal = secondLastVal.replace('?','')

print(firstVal, secondVal)  #afisam primele doua valori

if lastVal == secondLastVal :   #tragem concluzia negocierii
    print("S-au inteles !")
else:
    print("Nu s-au inteles")
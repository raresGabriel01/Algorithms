"""
“Traduceri”
a) Se citește de la tastatură un text. Se cere să se “traducă” în limba păsărească textul dat astfel: după
fiecare vocală se adaugă litera p și încă o dată acea vocală (după a, e, i, o, u se adaugă respectiv pa,
pe, pi, po, pu). Exemplu: “Ana are mere.” devine “Apanapa aparepe meperepe.”
Fiind dat un astfel de text în limba păsărească, se poate obține textul original? Dacă da, faceți asta.
"""

# citim textul
# parcurgem
# adaugam caracterele intr un nou sir
# unde gasim o vocala
# adaugam in noul sir vocala + p + vocala

#se poate traduce din pasareasca in limbaj obisnuit
#inlocuind aparitiile structurilor de forma voc_p_voc cu voc

text = input("Introduceti textul: ")

vocale = "aeiou"
                                                    #citiri
print("1 = criptare , 2 = decriptare")
print(" ")
opt = int(input("Introduceti optiunea voastra: "))
sn = ''
if opt == 1 :   # pentru criptare

    for ch in text:     #pentru fiecare litera din text
        if ch.lower() in vocale:                # daca e o vocala
            sn += ch +'p' + ch      # criptam corespunzator
        else:
            sn += ch        #altfel adaugam pur si simplu in noul sir
else:          #pentru decriptare
    i = 0
    while i < len(text) - 2:        #parcurgem
        #print(i)
        if (text[i].lower() in vocale) and (text[i+1].lower() == 'p') and (text[i+2].lower() == text[i].lower()) :
                #daca gasim o structura de forma vocala+p+vocala
            sn += text[i]       #o transformam intr o simpla vocala
            i += 2      # si sarim peste p si peste dublura vocalei

        else: sn += text[i]     #altfel, adaugam pur si simplu
        i += 1  #mergem mai departe


    # am folosit while pentru ca in for nu ma lasa sa incrementez i-ul sa sar peste pasi
    # daca fac i+=2 (linia 43) in urmatorul pas continua obisnuit, ca si cand ignora incrementarea


print(sn)   # afisam

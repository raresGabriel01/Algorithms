"""
Se citește de la tastatură un text în care cuvintele sunt despărțite în silabe cu ajutorul cratimelor. Se
cere să se “traducă” textul dat în limba păsărească astfel: după fiecare silabă se adaugă litera p și se
repetă ultima literă din acea silabă. Afișați traducerea și cu cratime, dar și fără.
Exemplu: “A-na a-re mul-te me-re ro-sii si de-li-cioa-se.” devine
“Apa-napa apa-repe mulpl-tepe mepe-repe ropo-siipi sipi depe-lipi-cioapa-sepe.” și
“Apanapa aparepe mulpltepe meperepe roposiipi sipi depelipicioapasepe.”
Fiind dat un astfel de text în limba păsărească (cel care conține și cratime), se poate obține textul
original? Dacă da, faceți asta
"""


# analog cu 8_a


text = input("Introduceti textul: ")
print("Criptare(1) / Decrpitare(2) ? : ")
opt = int(input())

sn=''

if opt == 1:
    i = 0
    while i < len(text)-1:
        if text[i+1] == '-' or text[i+1] == ' ':
            sn += text[i] + 'p' + text[i]
        else:
            sn += text[i]
        i += 1
    sn += text[len(text)-1] + 'p' + text[len(text)-1]
    print(sn)
    sn = sn.replace('-','')
    print(sn)

else:
    i = 0
    while i < len(text) - 3 :
        if ( text[i+3] == '-' or text[i+3] == ' ' ) and text[i].lower() == text[i+2].lower() and text[i+1] == 'p':
            #print("muie")
            sn += text[i] + text[i+3]
            i += 3
        else:
            sn += text[i]
        i += 1
    sn += text[len(text)-1]
    print(sn)


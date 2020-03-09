"""
Grupuri de cuvinte care rimează
Se citește un text format din cuvinte de lungime minim 3, despărțite prin spațiu. Să se creeze un
dicționar “rime” care are ca chei sufixe de lungime 2 ale cuvintelor din text, iar ca valori liste cu
cuvintele din text care au ca acel sufix. Apoi să se creeze un alt dicționar “final”, care preia din
dicționarul “rime” doar acele perechi pentru care lista conține cel puțin 2 cuvinte pentru
respectivul sufix.
"""

file = open("input.txt","r")

rime = {

}

l = [cuv for cuv in file.read().split()] #e good practice sa bagi cuv intr-o lista ca poate mai ai nevoie de ele mai tarziu si nu le poti
                                                                                        #lua din nou cu file.read()

for cuv in l:           #pentru fiecare cuvant din lista
    suf =  cuv[len(cuv)-2] + cuv[len(cuv)-1]        #facem sufixul
    if suf in rime:     #adaugam in dictionar in mod corespunzator
        rime[suf].append(cuv)
    else:
        rime[suf] = [cuv]

final = {
                #dictionarul final
}

for key in rime:
    if len(rime[key]) >= 2:     #daca sunt mai multe de 2 cuvinte cu rima
        final[key] = rime[key]      #adaugam in final


print(final)    #afisam
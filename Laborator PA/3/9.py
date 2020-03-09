"""
Definiții
Un student vrea, pentru ora de engleză de la FMI, să găsească cele mai expresive cuvinte. Pentru
aceasta a făcut o poză la astfel de cuvinte dintr-un dicționar, iar apoi a folosit un program ca să
extragă un string cu textul din poze. Textul respecta regulile:
• Este împărțit în paragrafe, fiecare paragraf terminându-se cu "\n".
• Fiecare paragraf corespunde unei intrări din dicționar, adică conține un cuvânt și definițiile
pentru acesta
• Cuvântul unui paragraf este la începutul lui și este mereu urmat de ":" și apoi de toate
definițiile cuvântului
Acum, studentul vrea sa decidă care sunt cele mai expresive cuvinte. Pentru asta, numără pentru
fiecare cuvânt în câte expresii apare (Ex: run away, run over, run a company), în acesta mod:
• Numără de câte ori apare cuvântul în paragraf
• Numără de câte ori apare caracterul tilda (~) în paragraf
• Și însumează aceste două numere
- Se dă stringul complet, format din paragrafe și dat ca input pe un singur rând.
- Se cere să se obțină o listă de tupluri formate dintr-un cuvânt aflat la început de paragraf și
numărul care reprezintă expresivitatea sa calculată în acel paragraf.
De exemplu, pentru următorul string:
"run: to go faster than a walk : to go steadily by springing steps : to take part into a contest - ~ a
marathon : to move at a fast gallop - he may occasionally run to and from work : flee, retreat,
escape - drop the gun and run : to go without restraint : move freely about at will - let chickens ~
loose : consort - we run with our group \n" +
"dog: canid wolves, foxes, and other dogs especially : a highly variable domestic mammal : a pet ~ :
fellow, chap, a lazy person - you lucky dog \n" +
"break: break a/the record to do something better than the best known speed, time, number, etc.
previously achieved : to fail to keep a law, rule, or promise = ~ the law : These enzymes break
down food in the stomach (= cause food to separate into smaller pieces). I needed something to
break the monotony of my typing job. The phone rang, as to break my concentration. To ~ (of a
storm) = to start suddenly: We arrived just as a storm was breaking. \n"
Se obține:
[("run", 5), ("dog", 2), ("break", 6)]
# de exemplu, pentru "run" numărăm de două ori pe ~ și de 3 ori pe run, deci expresivitatea este 5,
iar tuplul este ("run", 5)
"""



# vom considera, ptr frumusetea si simplitatea inputului ca paragrafele sunt scrise pe mai multe randuri
# si ca o definitie se termina literalmente cu "\n"
# nu cu caracterul "urmatoarea linie" ci cu STRINGUL "\n" ("\" + "n")

#note: a se ignora ghilimelele, nu sunt necesare in input


file = open("input.txt","r")


l = [cuv for cuv in file.read().split()]

d = {

}

lTup = []

#print(l)

lastChWasEL = True         #last character was end line

for cuv in l :
    if lastChWasEL:
        if len(d) != 0:
            lTup.append((list(d.keys())[0],d[list(d.keys())[0]]+d[list(d.keys())[1]]))      #adaugam tuplet
        d.clear()       #curatam dictionarul
        d[cuv.replace(":","")] = 0      #il initializam pentru urm definitie
        lastChWasEL = False
    elif cuv in d :
        d[cuv] += 1                 #adaugam corespunzator cuvintele in dictionar
    elif cuv == "~":
        d[cuv] = 1
    elif cuv == "\\n":
        lastChWasEL = True

lTup.append((list(d.keys())[0],d[list(d.keys())[0]]+d[list(d.keys())[1]]))


print(lTup)
"""
Știind că 1 ianuarie 1702 a picat într-o zi de duminică, să se citească de la tastatură o dată mai
recentă, și să se spună în ce zi a săptămânii cade aceasta.
Puteți să faceți 2 cazuri - în care inputul este dat de forma "1 10 2019", sau "1 octombrie 2019".
Folosiți funcția range() pentru a itera printre ani, respectiv instrucțiuni if/elif/else pentru a trata
cazurile de ani bisecți. Puteți folosi un dicționar sau o listă pe post de switch/case ca să aflați în ce zi a
săptămânii pică data respectivă.
"""
# se rezolva iterand prin ani si prin zile adunand numarul de zile
# iteram mai intai prin ani, dupa prin luni si adaugam la final numarul de zile
# ziua saptamanii se afla prin restul impartirii la 7
def nrZile(a):
    if a % 4 != 0:
        return 365
    elif a % 100 != 0:
        return 366              #functie ce determina nr de zile ale unui an
    elif a % 400 != 0:
        return 365
    else: return 366
ziua = {
    0 : "Duminica",
    1 : "Luni",
    2 : "Marti",
    3 : "Miercuri",         #dictionar ptr ziua saptamanii
    4 : "Joi",
    5 : "Vineri",
    6 : "Sambata"
}

luna_ = {
    'ianuarie':1,
    'februarie':2,
    'martie':3,
    'aprilie':4,
    'mai':5,
    'iunie':6,
    'iulie':7,              # dictionar lunile anului
    'august':8,
    'septembrie':9,
    'octombrie':10,
    'noiembrie':11,
    'decembrie':12
}
#"""
x,y,z, = input().split()


if y.isdigit():
    zi, luna, an = int(x), int(y), int(z)               #atribuirea corespunzatoare
else:
    zi, luna, an = int(x),luna_[y.lower()],int(z)

dayOfWeek = -1

nrDays = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]        # o lista cu nr de zile, nrDays[x] = nr de zile ale lunii x (index de la 0)

for year in range(1702, an):
    dayOfWeek += nrZile(year)       #parcurgem anii PANA la anul citit

for month in range (1, luna):
    if month == 2 and nrZile(an) == 366:
        dayOfWeek += 29                     #parcurgem lunile PANA la luna citita

    elif month == 2 and nrZile(an) == 365:
        dayOfWeek += 28

    else:
        dayOfWeek += nrDays[month-1]


dayOfWeek += zi         #adaugam numarul de zile


print(ziua[dayOfWeek % 7])            #afisam
#"""


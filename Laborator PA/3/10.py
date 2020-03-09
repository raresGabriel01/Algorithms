"""
Departajare
La facultate se ține un concurs de programare. Organizatorii au aranjat ca punctajele să fie
calculate automat, din codul scris. Totuși, ei nu au implementat vreo metodă de a departaja
punctajele egale, așa că pe ultimul moment s-au decis ca persoana care a trimis codul prima să fie
clasată mai sus decât cel de-al doilea ca timp, dar cu punctaj identic șamd.
Până la introducerea lui “-1”, să se citească de la tastatură perechi de două elemente: (punctaj,
nume_student), cu punctajul între 0 și 100. Perechile se consideră a fi introduse în ordinea predării
codului de către participanți.
a) Salvați inputul într-o listă de tupluri (punctaj, nume_student, nr_ordine), astfel încât să se poată
deducă și numărul de ordine pentru fiecare participant (al câtelea a predat codul).
b) Să se afișeze lista tuturor punctajelor distincte obținute de participanți (folosiți un set).
c) Într-un dicționar, pentru fiecare punctaj să se asocieze o listă de tupluri ce conțin numele
participantului și numărul său de ordine. Apoi, să se afișeze clasamentul concursului (descrescător
după punctaje, pe câte un rând: punctaj, nume_participant și nr_ordine).
De exemplu, pentru următorul input:
64 Danil Marius
70 Derek Alexandru
100 Pirpiric Claudiu
18 Alexandrescu Matias
64 Popescu Catalin
100 Cozia Daniel
82 Stefan Dinca
-1
Vom obtine:
a) Lista [(64, Danil Marius, 1), (70, Derek Alexandru, 2), (100, Pirpiric Claudiu, 3), (18, Alexandrescu
Matias, 4), (64, Popescu Catalin, 5), (100, Cozia Daniel, 6), (82, Stefan Dinca, 7)]
b) Mulțimea {100, 82, 70, 64, 18} (nu neapărat în această ordine)
c) Și dicționarul (având perechile nu neapărat în această ordine):
 {
 100: [("Pirpiric Claudiu", 3), ("Cozia Daniel", 6)],
 82: [("Dinca Stefan", 7)],
 70: [("Derek Alexandru", 2)],
 64: [("Danil Marius", 1), ("Popescu Catalin", 5)],
 18: [("Alexandrescu Matias", 4)]
}
"""


lTup = []
setPct = set()
d = {

}

pct, nume, nrOrd = 0, 0, 0

while pct != -1:
    try:
        x, y, z = input().split()  # y si z = nume si prenume. presupunem ca in cazul in care sunt 2 prenume/nume de familie
        pct, nume,  = int(x), y+" "+z                                           #atunci ele sunt despartite prin cratima
        nrOrd += 1
        lTup.append((pct,nume,nrOrd))
        setPct.add(pct)
        if pct in d:
            d[pct].append((nume,nrOrd))
        else:
            d[pct]=[(nume,nrOrd)]
    except:
        pct = -1

print(lTup)
print(setPct)
print(d)
"""
Scrieți un program care să se verifice dacă două șiruri de caractere sunt anagrame sau nu. Două
șiruri sunt anagrame dacă unul se poate obține din celălalt printr-o permutare a caracterelor sale. De
exemplu, șirurile emerit și treime sunt anagrame, dar șirurile emerit și treimi nu sunt! Indicație de
rezolvare (fără structuri de date auxiliare și fără sortare): Se caută, pe rând, fiecare caracter din
primul șir în cel de-al doilea. În cazul în care caracterul nu este găsit înseamnă că șirurile nu sunt
anagrame, altfel se șterge caracterul din cel de-al doilea șir și se trece la următorul caracter din
primul șir. Atenție, folosind această metodă, cel de-al doilea șir va fi modificat!
"""

# Vom lua pe rand fiecare litera din primul cuvant si vom sterge aparitia corespunzatoare in al doilea cuvant

cuv1 = input("Introduceti primul cuvant: ")         #citim
cuv2 = input("Introduceti al doilea cuvant: ")

if len(cuv1) != len(cuv2):                  #daca cuvintele nu au aceeasi lungime atunci evident nu sunt anagrame
    print("Nu sunt anagrame")
else:
    for ch in cuv1:                         #pentru fiecare litera din primul cuvant
        cuv2=cuv2.replace(ch,'',1)          #stergem aparitia ei in cel de-al doilea cuvant
    if len(cuv2) > 0:                       #daca in cel de al doilea cuvant au mai ramas litere
        print("Nu sunt anagrame")           #atunci nu sunt anagrame
    else:
        print("Sunt anagrame")              #altfel, inseamna ca toate literele din cuv1 se regasesc in cuv2 deci sunt anagrame


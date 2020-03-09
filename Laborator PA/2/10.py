"""
Numele Pre-Nume
Scrieți un program care citește un șir de caractere și decide dacă acesta este un nume corect al unei
persoane. Se consideră că un nume este corect dacă respectă următoarele proprietăți:
• Orice nume sau prenume conține doar litere și cel mult o cratimă.
• Orice nume sau prenume este format din cel puțin 3 litere.
• Orice nume sau prenume începe cu literă mare.
• Prenumele sunt cel mult două, iar dacă sunt două atunci sunt despărțite printr-o cratimă (‘-’).
"""

# verificam pas cu pas proprietatile de mai sus

nume = input("Introduceti numele: ")

caracterePermise = "abcdefghijklmnopqrstuvwxyz- "

ok = True

for ch in nume.lower():
    if not (ch  in caracterePermise) :

        print("Nume invalid 1")
        ok = False

if ok == True :
    if '-' in nume.replace('-',' ',1):
        ok = False
        print("Nume invalid 1*")
if ok == True:
    if len(nume.replace('-',' ',1).split()) > 3:
        ok = False
        print("Nume invalid 4")
    elif  len(nume.split()) > 2:
        ok = False
        print("Nume invalid 4")
if ok == True:
    for cuv in nume.split():
        if len(cuv) < 3:
            ok = False
            print("Nume invalid 2" )
if ok == True:
    if nume.replace('-',' ').title() != nume:
        ok = False
        print("Nume invalid 3")

if ok == True:
    print("Nume Valid")

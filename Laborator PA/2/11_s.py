"""
Se dă un text (puteți de exemplu să luați text dintr-un paragraf de pe
https://en.wikipedia.org/wiki/Python_(programming_language) ).
1. Folosiți funcția split pentru a despărți textul în propoziții (care se termină prin ‘.’).
2. Încercați și o altă abordare: în loc de a despărți numai prin ‘.’, care poate fi prezent și după
prescurtări și in punctele de suspensie (…), puteți să verificați ca fiecare propoziție să înceapă
cu literă mare. Astfel, regula va fi că o propoziție începe cu literă mare și (cu excepția primeia)
este precedată de un ‘.’
"""

text = input("Introduceti textul: ")

pp = ''
# list[i] = cuvantul indexat cu i din lista
# list[i][j] = litera indexata cu j din cuvantul indexat cu i din lista
# ex: list = ['ana','are','mere']
# list[1][0] == 'a'
lista = [cuv for cuv in text.split()] # bagam cuvintele intr o lista

for i in range(len(lista)-1):   #parcurgem
    pp += lista[i]
    if lista[i][len(lista[i])-1] == '.' and lista[i+1][0].isupper():
    #daca am gasit punct la finalul unui cuv sau puncte de suspensie SI urmatoarea litera din urmatorul cuvant e mare
    #atunci avem o noua propozitie
        print(pp)
        pp=''
    else:
        pp += ' '
pp += lista[len(lista)-1]   #adaugam ultimul cuvant (am folosit parcurgere pana la len()-1 pentru ca mai sus folosim i+1
print(pp)   #afisare


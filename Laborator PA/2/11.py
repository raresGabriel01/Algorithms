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

for i in range(len(text.split())-1):
    pp += text.split()[i]
    #print(pp)
    if ( text.split()[i][len(text.split()[i])-1] == '.' or text.split()[i] == '...' ) and text.split()[i+1][0].isupper() :
        print(pp)
        pp = ''
    else:
        pp += ' '
pp += text.split()[len(text.split())-1]
print(pp)
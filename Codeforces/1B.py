#https://codeforces.com/problemset/problem/1/B

def poz(ch):
    return ord(ch)-64
def ch(poz):
    if poz == 0:
        return 'Z'
    return chr(poz+64)
def tip(coord):
    i = 0
    while coord[i].isalpha() == True:
        i += 1
    try:
        while coord[i].isdigit() == True:
            i += 1
    except IndexError:
        return 1
    return 2


def conv12(coord):
    aux = ""
    index = 0
    for i in range(len(coord)):
        if coord[i].isalpha() == True:
            aux += coord[i]
        else:
            index = i
            break


    conv = "R" + coord[index:] + "C"

    nr = 0



    #########################
    #l1 l2 l3 ... ln
    #val  = 26^(n-1) * poz (l1) + 26^(n-2) * poz(l2) + ... + 26^0 * poz(ln)
    #########################

    for i in range (index):
        nr += 26**(index-i-1) * poz(coord[i])

    conv += str(nr)
    return conv

def conv21(coord):
    index = len(coord)-1
    while coord[index].isdigit() == True:
        index -= 1
    index += 1
    #print(index,"-------------")
    aux = coord[index:]
    nr = int(aux)
    aux = ""
    while nr != 0 :
        r = nr % 26

        aux = ch(r) + aux

    #    print(r,aux)
        if r == 0:
            nr//=26
            nr-=1
        else:
            nr//=26
    aux += coord[1:index-1]
    return aux

n = int(input())
sol = []
for i in range(n):
    text = input()
    if tip(text) == 1:
        sol.append(conv12(text))
    else:
        sol.append(conv21(text))

for el in sol:
    print(el)

#BH855
#R228C494
#print(tip("R228C494"))
#print(conv12("BH855"))
#print(conv21("R228C494"))
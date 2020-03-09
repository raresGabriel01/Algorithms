    """
    Jurnalul electronic al Anei conține, în fiecare zi, câte o frază cu informații despre cheltuielile pe
    care ea le-a efectuat în ziua respectivă. Scrieți un program care să citească o frază de acest tip din
    jurnalul Anei și apoi să afișeze suma totală cheltuită de ea în ziua respectivă. De exemplu, pentru fraza
    “Astăzi am cumpărat pâine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumpărat niște
    cașcaval. De asemenea, mi-am cumpărat și niște papuci cu 50 RON!”, programul trebuie să afișeze
    suma totală de 80 RON. Fraza se consideră corectă, adică toate numerele care apar în ea sunt
    numere naturale reprezentând sume cheltuite de Ana în ziua respectivă!
    """
    
    #utilizam metoda split() pentru a imparti textul pe cuvinte
    #luam cuvant cu cuvant si verificam care sunt numere utilizand functia isdigit()
    
    # metoda cuvant.isdigit() returneaza o valoarea booleana astfel: returneaza TRUE daca "cuvant" e numar (nu conteaza natura lui), altfel da FALSE
    
    sir = input("Introdu sirul: ")
                                                    #citire / initializare
    total = 0
    
    for cuv in sir.split():         #ptr fiecare cuvant din text
        if cuv.isdigit() == True:      #daca e numar
            total += int(cuv)       #adunam
    
    print("In total au fost cheltuiti:",total)  #afisare

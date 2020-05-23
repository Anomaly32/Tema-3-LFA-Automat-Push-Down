
fin = open("input_APD.txt", "r")

'''
inputul este de forma:
6           - nr stari
11          - numar tranzitii, urmate de acel numar de tranzitii
0 1 a A AA  - stare initiala | stare finala | caracter de tranzitie | litera stearsa din stiva | litere adaugate in stiva
0 1 a Z AZ
0 2 b A $   
1 0 a A AAA
2 2 b A $
2 3 c D DD
2 3 c Z DZ
3 2 c D D
2 4 d D $
4 4 d D $
4 5 $ Z $
0           - stare initiala
1       - numar stari finale
5       - stari finale
'''

vid = '$'   # lambda


def adauga_caractere(stiva, caractere):
    if len(caractere) == 1 and caractere[0] == vid:
        return stiva
    else:
        return stiva + caractere[::-1]


def verificare(cuv, stare_curenta, index, stiva):
    has_vid = False
    if vid in tranzitii[stare_curenta]:
        has_vid = True
    if index == len(cuv):   # daca am ajuns la finalul cuvantului verificam daca suntem in stare finala
        if (stare_curenta in sf) and (stiva == ['Z'] or len(stiva) == 0):
            return True
        elif has_vid is True:   # daca nu am ajuns la final verificam lambda-tranzitiile
            if stiva[-1] in tranzitii[stare_curenta][vid]:
                tsc = tranzitii[stare_curenta][vid][stiva[-1]]  # tranzitii stare curenta
                nt = len(tsc)
                for i in range(nt):
                    if verificare(cuv, tsc[i][0], index, adauga_caractere(stiva[:-1], list(tsc[i][1]))) is True:
                        return True
        return False

    has_litera = False
    if cuvant[index] in tranzitii[stare_curenta]:
        has_litera = True

    if has_litera is True:  # verificam tranzitiile cu litere
        if stiva[-1] in tranzitii[stare_curenta][cuvant[index]]:
            tsc = tranzitii[stare_curenta][cuvant[index]][stiva[-1]]  # tranzitii stare curenta
            nt = len(tsc)
            for i in range(nt):
                if verificare(cuv, tsc[i][0], index + 1, adauga_caractere(stiva[:-1], list(tsc[i][1]))) is True:
                    return True
    if has_vid is True:     # verificam lambda tranzitiile
        if stiva[-1] in tranzitii[stare_curenta][vid]:
            tsc = tranzitii[stare_curenta][vid][stiva[-1]]  # tranzitii stare curenta
            nt = len(tsc)
            for i in range(nt):
                if verificare(cuv, tsc[i][0], index, adauga_caractere(stiva[:-1], list(tsc[i][1]))) is True:
                    return True
    return False


nr_stari = int(fin.readline())                  # numar total stari
nr_tranzitii = int(fin.readline())              # numar total tranzitii
tranzitii = list()                              # tranzitiile dintre stari de forma
                                                # list [start] [caracter] [pop] = list(pair(dest, add))
for i in range(nr_stari):
    tranzitii.append(dict())
for i in range(nr_tranzitii):
    aux = [x for x in fin.readline().split()]
    if aux[2] not in tranzitii[int(aux[0])]:
        tranzitii[int(aux[0])][aux[2]] = dict()
    if aux[3] not in tranzitii[int(aux[0])][aux[2]]:
        tranzitii[int(aux[0])][aux[2]][aux[3]] = list()
    tranzitii[int(aux[0])][aux[2]][aux[3]].append(tuple([int(aux[1]), aux[4]]));
si = int(fin.readline())                        # stare initiala
nr_sf = int(fin.readline())                     # numar stari finale
sf = [int(x) for x in fin.readline().split()]   # stari finale

nr_cuv = int(input("cate cuvinte veti introduce?: "))
for i in range(nr_cuv):
    cuvant = input("cuvantul de verificat este: ")
    if verificare(cuvant, si, 0, ['Z']) is True:
        print("cuvant valid")
    else:
        print("cuvant invalid")

def citireLista():
    l= []
    n = int(input("Dati nr de elemente"))
    for i in range(n):
        l.append(input("l["+str(i)+"]="))
    return l


def gasitInLista(cuv,l):
    """
    cautam un cuvant dat in lista
    :param cuv: cuvantul pe care vrem sa il cautam
    :param l: lista de stringuri
    :return: daca cuvantul se afla sau nu in lista
    """
    k=0
    for i in range (len(l)):
        if l[i]==cuv:
            k=1
    if k==1:
        return "DA"
    else:
        return "NU"


def test_gasitInLista():
    assert gasitInLista('drd',['aaa','bbb','cmtc','drd','aaa']) == "DA"
    assert gasitInLista('abc',['abc','bcd','abc','dee','ade']) == "DA"
    assert gasitInLista ('dea',['age','bef','fee']) == "NU"
    assert gasitInLista ('der',['abb','vee','der']) == "DA"
test_gasitInLista()

def seRepeta(l):
    """
    verificam care cuvinte se repeta
    :param l: lista de stringuri
    :return: cuvintele care apar de mai multe ori sau "UNIC" in caz ca nu exista
    """
    vazute=[]
    l2=[]
    for i in l:
        if i not in vazute:
            vazute.append(i)
        else:
            l2.append(i)

    if l2==[]:
        return "UNIC"
    else:
        return l2


def test_seRepeta():
    assert seRepeta(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ['aaa']
    assert seRepeta(['abc','bcd','abc','dee','abc','dee','nan']) == ['abc','abc','dee']
    assert seRepeta(['abc','cbe','dec']) == "UNIC"
test_seRepeta()


def cuvPalindrome(l):
    """
    verificam care sunt cuvintele palindrom din lista
    :param l: lista de stringuri
    :return: cuvintele care sunt palindrom
    """
    l2=[]
    for i in range(len(l)):
        a=l[i]
        if(a==a[::-1]):
            l2.append(a)
    return l2


def test_cuvPalindrome():
    assert cuvPalindrome(['ada', 'abc' , 'cmtc', 'drd', 'aaa']) == ['ada','drd','aaa']
    assert cuvPalindrome(['abc','dea','oob']) == []
    assert cuvPalindrome(['aba','ada','ebe','obo']) == ['aba','ada','ebe','obo']
test_cuvPalindrome()


def printMenu():
    print("1.Citire lista\n"
          "2.Afisare lista\n"
          "3.Afisati cuvintele palindrome din lista\n"
          "4.Afisati care cuvinte se repeta in lista\n"
          "5.Cautati un cuvant in lista\n")


def main():
    l=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea dorita: ")
        if optiune == "1":
            l=citireLista()
        elif optiune == "2":
            print(l)
        elif optiune == "3":
            print(cuvPalindrome(l))
        elif optiune =="4":
            print(seRepeta(l))
        elif optiune =="5":
            cuv=input("dati cuvantul pe care il cautati")
            print(gasitInLista(cuv,l))

main()


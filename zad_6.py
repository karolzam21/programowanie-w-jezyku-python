# Kolejnosc zdarzeń: łączenie list, usunięcie duplikatów,potęga 3
def fpolacz_i_podnies_do_szescianu(lista1, lista2):
    polaczone = lista1 + lista2
    bez_duplikatow = list(set(polaczone))

    wynik = []
    for x in bez_duplikatow:
        wynik.append(x ** 3)
    return wynik


print(fpolacz_i_podnies_do_szescianu([2, 3, 4], [5, 6, 4]))

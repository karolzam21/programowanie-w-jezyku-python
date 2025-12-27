def fsprparzystosc(lb) -> bool:
    return (lb % 2) == 0


Lb = input("Podaj liczbę: ")


if not fsprparzystosc(int(Lb)):
    print(str(Lb) + ' liczba nieparzysta')
else:
    print(str(Lb) + ' liczba parzysta')

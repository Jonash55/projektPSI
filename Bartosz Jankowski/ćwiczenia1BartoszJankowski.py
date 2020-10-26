zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. " \
          "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. " \
          "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
          "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty " \
          "Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do " \
          "realizacji druków na komputerach osobistych, jak Aldus PageMaker."
print(zmienna)
imie = "Bartosz"
nazwisko = "Jankowski"
liczba_liter1 = zmienna.count(imie[2])
liczba_liter2 = zmienna.count(nazwisko[3])
print("W tekście jest {} liter {} oraz {} {} ".format(liczba_liter1, imie[2], liczba_liter2, nazwisko[3]))

print('------------------------------------------------------------------')

print(dir(zmienna))
help(zmienna.capitalize)

print(imie[::-1], nazwisko[::-1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_dalej = lista[5:10]
lista = lista[0:5]
print(lista)
print(lista_dalej)
lista.extend(lista_dalej)
print(lista)
lista = [0] + lista
print(lista)
kopia = lista
print(kopia)
kopia.sort(reverse=True)
print(kopia)

pierwszy = (151246, "Tomek Mróz")
drugi = (525674, "Jan Polak")
trzeci = (123124, "Bartosz Kowalski")
print(pierwszy[1])
krotka = [pierwszy, drugi, trzeci]


def zamien(krotka, slownik):
    slownik = dict(krotka)
    return slownik


dic = {}
dic1 = zamien(krotka, dic)
print(dic1)
dic1.update({'152788': "Adam Roztowiak"})
print(dic1)

numery = [123123123, 123123123, 123153453, 543787854, 155123153, 123123123]
print(numery)
print(list(set(numery)))

for i in range(10):
    print(i)

for i in range(100, 20, -5):
    print(i)

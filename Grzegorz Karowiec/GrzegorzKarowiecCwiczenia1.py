

tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. " \
          "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. " \
          "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
          "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty " \
          "Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do " \
          "realizacji druków na komputerach osobistych, jak Aldus PageMaker."
print(tekst)
imie = "Grzegorz"
nazwisko = "Karowiec"
ilosc_liter1 = tekst.count(imie[2])
ilosc_liter2 = tekst.count(nazwisko[3])
print("W tekście jest {} liter {} oraz {} {} ".format(ilosc_liter1, imie[2], ilosc_liter2, nazwisko[3]))


print(dir(tekst))
help(tekst.capitalize)

print(imie[::-1], nazwisko[::-1])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = list[5:10]
list = list[0:5]
print(list)
print(list2)
list.extend(list2)
print(list)
list = [0] + list
print(list)
copy = list
print(copy)
copy.sort(reverse=True)
print(copy)

jeden = (151026, "Szymon Jakiś")
dwa = (456786, "Tadeusz Ptak")
trzy = (123456, "Jan Kowalski")
print(jeden[1])

slownik = dict((y, x) for x, y in jeden)
print(slownik)

numery = [123123423, 223456123, 123153453, 500927345, 948573621, 756453728]

for i in range(10):
    print(i)

for i in range(100, 20, -5):
    print(i)
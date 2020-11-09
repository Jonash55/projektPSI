print("===================================================================")
print("                            Zadanie 1                              \n")
a_list = [1, 2, 3, 4, 5, 6]
b_list = [1, 2, 3, 4, 5, 6]
lista = []


def listy(a_list, b_list):
    lista.append(a_list[1::2])
    lista.append(b_list[0::2])

    return lista


print(listy(a_list, b_list))
data_text = "Jakiś tam tekst. Pozdrawiam was serdecznie koledzy"
print(len(data_text))

print("===================================================================")
print("                            Zadanie 2                              \n")


def tekst(data_text):
    letters = {}
    length = len(data_text)
    letters = list(data_text)
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    slownik = {"Info": {length, big_letters, small_letters}, "Literki": letters}
    return slownik


print(tekst(data_text))

print("===================================================================")
print("                            Zadanie 3                              \n")
text = "Jakiś przykładowy tekst"
letter = "TEKST"


def usuwanie(text, letter):
    pomniejszony_tekst = text.lower()
    pomniejszone_slowo = letter.lower()
    text_slowa = pomniejszony_tekst.split()
    zmienione_slowa = [slowo for slowo in text_slowa if slowo not in pomniejszone_slowo]
    zmiana_koncowa = " " .join(zmienione_slowa)
    print(zmiana_koncowa.capitalize())


usuwanie(text, letter)

print("===================================================================")
print("                            Zadanie 4                              \n")


def temperatura(temperature_type):
    #tempCelsjusz = 22
    tempRankine = 531.27
    tempKelvin = 295.15
    tempFahrenheit = 71.60
    if temperature_type == "Fahrenheit" or temperature_type == "Rankine" or temperature_type == "Kelvin":
        if temperature_type == "Rankine":
            print("Temperatura 22°C w skali Rankine wynosi: " + str(tempRankine) + " °R")
        if temperature_type == "Kelvin":
            print("Temperatura 22°C w skali Kelvina wynosi: " + str(tempKelvin) + " K")
        if temperature_type == "Fahrenheit":
            print("Temperatura 22°C w skali Fahrenheita wynosi: " + str(tempFahrenheit) + " °F")
    else:
        print("Podano zły typ temperatury")


temperatura('Fahrenheit')
temperatura('Rankine')
temperatura('Kelvin')
temperatura('XD')

print("===================================================================")
print("                            Zadanie 5                             \n")


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return "Wybrano dodawanie. Wynik: " + str(self.a + self.b)

    def multiply(self):
       return "Wybrano mnożenie. Wynik: " + str(self.a * self.b)

    def diverse(self):
        if self.b == 0:
            print("Nie wolno dzielić przez 0")
            return None
        return "Wybrano dzielenie liczby a przez b. Wynik: " + str(self.a / self.b)

    def difference(self):
        return "Wybrano odejmowanie liczby a od b. Wynik: " + str(self.a - self.b)


Oblicz = Calculator(1, 4)
Oblicz_przez_zero = Calculator(1, 0)
print(Oblicz.add())
print(Oblicz.multiply())
print(Oblicz.diverse())
print(Oblicz.difference())
print(Oblicz_przez_zero.diverse())

print("===================================================================")
print("                            Zadanie 6                             \n")


class ScienceCalculator(Calculator):
    def potegowanieAB(self):
        return "Wybrano potęgowanie liczby a do potęgi b. Wynik: " + str(self.a ** self.b)

    def potegowanieA(self, liczba):
        return "Wybrano potęgowanie liczby a do potęgi wybranej liczby. Wynik: " + str(self.a ** liczba)

    def potegowanieB(self, liczba):
        return "Wybrano potęgowanie liczby b do potęgi wybranej liczby. Wynik: " + str(self.b ** liczba)


potega = ScienceCalculator(2, 4)
print(potega.potegowanieAB())
print(potega.potegowanieA(2))
print(potega.potegowanieB(2))

print("===================================================================")
print("                            Zadanie 7                             \n")

tekst = "Pozdrawiam was serdecznie"


def odwrocnone(tekst):
    odwrotnie = tekst[::-1]
    return odwrotnie


print(tekst)
print(odwrocnone(tekst))

print("===================================================================")
print("                            Zadanie 8                             \n")


class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        plik = open(self.file_name, 'r')
        dane = plik.read()
        print(dane)
        plik.close()

    def update_file(self, text_data):
        plik = open(self.file_name, 'a')
        plik.write(text_data)
        plik.close()


pliczek = FileManager('tekst.txt')
pliczek.read_file()
pliczek.update_file(' Dziękuję Wam za wszystko!')
pliczek.read_file()

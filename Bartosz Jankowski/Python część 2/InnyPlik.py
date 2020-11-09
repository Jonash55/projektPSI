from main import FileManager

print("===================================================================")
print("                            Zadanie 9                             \n")

plik = FileManager('tekst2.txt')
plik.read_file()
plik.update_file(' Działa!')
plik.read_file()

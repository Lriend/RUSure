import itertools

print('Witaj w generatorze hasel')
skala = input('Podaj dlugosc generowanych slow np. 5-10 -> ')
start = int(skala.split('-')[0])
koniec = int(skala.split('-')[1])
osobiste = str(input("\nChcesz uzyc danych osobistych? (t/n): "))
if osobiste == 't':
	imie = str(input("\nImie: "))
	nazwisko = str(input("\nNazwisko: "))
	liczby = str(input("\nWazne liczby (nr telefonu, domu, urodziny: "))
	hobby = str(input("\nHobby: "))
	zwierze = str(input("\nImie zwierzaka: "))
	inne = str(input("\nInne slowa kluczowe (nie oddzielaj lepiej kolejnych slow): "))
	znaki = imie + nazwisko + liczby + hobby + zwierze + inne
else:
	znaki = 'abcdefghijklmnopqrstuvwxyz'
if input('\nChcesz uzyc cyfr? (t/n): ') == 't':
	znaki = ''.join([znaki, '1234567890'])
if input('\nChcesz uzyc wielkich liter? (t/n): ') == 't':
	znaki = ''.join([znaki, znaki.upper()])
if input('\nChcesz uzyc znakow specjalnych? (t/n): ') == 't':
	znaki = ''.join([znaki, '!\][/?.,~-=";:><@#$%&*()_+\' '])
nazwa_pliku = input('\nWpisz nazwe pliku dla wordlisty: ')
plik = open(nazwa_pliku, 'w')
for i in range(start, koniec+1):
	for j in itertools.product(znaki, repeat=i):
		temp = ''.join(j)
		#print(temp)
		plik.write(temp + '\n')
plik.close()

from os import system
import re

"""
Karakterverdier:
A = 5
B = 4
C = 3
D = 2
E = 1
F = 0
"""

system('clear')

karakterer = ""
teller = 0
kar = 1

# Lagerer alle karakterer i en string og viser disse
def dineKarakterer():
	ut = ""
	for c in karakterer:
		ut += c + " "
	print("Dine karakterer: " + ut)


def kalkulerSnitt():
	bokstavkar = "0"
	poengsum = 0
	snitt = 0
	for c in karakterer:
		if (c == "A"):
			poengsum += 5
		if (c == "B"):
			poengsum += 4
		if (c == "C"):
			poengsum += 3
		if (c == "D"):
			poengsum += 2
		if (c == "E"):
			poengsum += 1
		if (c == "F"):
			poengsum += 0

	print("Antall karakterer: " + str(teller))
	print("Poengsum: " + str(poengsum))
	if (teller > 0):
		snitt = poengsum / teller

	if 4.5 <= snitt <= 5:
		bokstavkar = "A"
	if 3.5 <= snitt < 4.5:
		bokstavkar = "B"
	if 2.5 <= snitt < 3.5:
		bokstavkar = "C"
	if 1.5 <= snitt < 2.5:
		bokstavkar = "D"
	if 0 <= snitt < 1.5:
		bokstavkar = "E"

	print("Ditt karaktersnitt: ", str(bokstavkar), "/", str(snitt))
	print()

# Sålenge 0 ikk er input, så vil den fortsette å spørre om karakterer
while kar != 0:
	system('clear')
	dineKarakterer()
	kalkulerSnitt()
	print("Skriv inn en og en karakter, avslutt med 0")
	kar = input("Skriv inn din karakter: ")

	while not re.findall('[a-fA-F]', kar) or len(kar) != 1: # hindrer bruker å legge inn annet enn godkjente bokstaver og kun en karakter av gangen
		if (kar == "0" or kar == 0):
			system('clear')
			dineKarakterer()
			kalkulerSnitt()
			exit()
		system('clear')
		dineKarakterer()
		kalkulerSnitt()
		print("Du kan ikke skrive inn fler enn en karakter av gangen og kun bokstaver fra A-F")
		kar = input("Skriv inn din karakter: ")

	else:
		karakterer += kar.upper()
		teller += 1

system('clear')
dineKarakterer()
kalkulerSnitt()
exit()
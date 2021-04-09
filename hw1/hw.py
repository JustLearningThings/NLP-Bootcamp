import os

x = 'Da'

lista_31 = ['1', '3', '5', '7', '8', '10', '12']
lista_30 = ['4', '6', '9', '11']

while x != 'nu':
	os.system('cls')

	x = input('x = ')
	anul = int(input('Anul = '))

	if x == '2':
		if anul % 4 == 0:
			print('29')
		elif anul % 4 != 0:
			print('28')
		else:
			print('Eroare!')
	elif x in lista_31:
		print('31')
	elif x in lista_30:
		print('30')
	else:
		print('Eroare!')

	print('Continui (\'da/nu\') ?')
	x = input()
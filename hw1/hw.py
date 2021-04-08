import os

x = 'Da'

while x != 'nu':
	os.system('cls')

	x = int(input('x = '))
	anul = int(input('Anul = '))

	# lunile impare au 31 de zile
	# lunile pare au 30 de zile
	# februarie are 28/29 de zile

	if x == 2:
		if anul % 4 == 0:
			print('29')
		elif anul % 4 != 0:
			print('28')
		else:
			print('Eroare!')
	elif x % 2 == 0:
		print('30')
	elif x % 2 != 0:
		print('31')
	else:
		print('Eroare!')

	print('Continui (\'da/nu\') ?')
	x = input()
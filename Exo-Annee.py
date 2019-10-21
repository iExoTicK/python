#!/usr/bin/env python3

year = int(input('Ecrire la date : '))

if (year %4 == 0 and year %100 != 0  or year %400 == 0):
	print("C'est une année Bissextile")
else:
	print("Ce n'est pas une année Bissextile")
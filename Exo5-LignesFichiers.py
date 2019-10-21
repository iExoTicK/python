#!/usr/bin/env python3

def nb_lignes(content):
    return len(content.split("\n"))

def nb_mots(ligne):
    return len(ligne.split(" "))

with open('exo5') as file:
	content = file.read()

print(nb_lignes(content))

lines = content.split("\n")
compteur_mots = 0
for line in lines:
    compteur_mots += nb_mots(line)
print(compteur_mots)

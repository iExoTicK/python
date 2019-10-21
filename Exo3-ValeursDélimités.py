#!/usr/bin/env python3

phrase = "adroit#a3#vroom#b52#colorant#e111"

tableau = phrase.split ("#")
resultats = []

for mot in tableau:
    if mot[-1].isdigit():
        resultats.append(mot)

print(';'.join(resultats))
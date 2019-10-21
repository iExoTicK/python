#!/usr/bin/env python3

texte = input('Ecrire votre phrase : ')

voyelle={'a':0,'e':0,'i':0,'o':0,'u':0,'y':0}
toutes_voyelles = 0

for i in texte:
    if i in voyelle:
        toutes_voyelles+=1
        voyelle[i]+=1

print(voyelle)
print(toutes_voyelles)

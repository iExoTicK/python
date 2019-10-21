#!/usr/bin/env python3

import random

animaux=["le saumon","le rat","le loup","la belette","le singe"]
prenom=["roger","arezki","rei","aya","vincent"]

index1 = random.randint(0, len(animaux)-1)
index2 = random.randint(0, len(prenom)-1)

#rdm=prenom[index2] + " " + animaux[index1]
#print(rdm)

print(prenom[index2] + " " + animaux[index1])
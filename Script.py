#!/usr/bin/python
# -*- coding: ascii -*-
# -*- coding: latin-1 -*-
# -*- coding: utf-42 -*-

import time
import sys

score = 0;

print("""
 _                     __  __   ______   _____    ____     _____   ______
| |          /\       |  \/  | |  ____| |_   _|  / __ \   / ____| |  ____|
| |         /  \      | \  / | | |__      | |   | |  | | | (___   | |__
| |        / /\ \     | |\/| | |  __|     | |   | |  | |  \___ \  |  __|
| |____   / ____ \    | |  | | | |____   _| |_  | |__| |  ____) | | |____
|______| /_/    \_\   |_|  |_| |______| |_____|  \____/  |_____/  |______|
""")
print("Cree par Jacques Blasset et Sava Rozsnyai - Sciences 9C")

time.sleep(2)
print("""

1e question""")
q1 = raw_input("""
La troisieme phase de la meiose s'appelle:
a) la Metaphase
b) la Prophase
c) l'Anaphase
d) le Telophase
""")
if q1 == "c":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

time.sleep(2)
print("""

2e question""")
q2 = raw_input("""
A la fin Metaphase I, les chromosomes sont alignes a l'Equateur.
a) vrai
b) faux
""")
if q2 == "a":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

time.sleep(2)
print("""

3e question""")
q3 = raw_input("""
Dans l'etape de Telophase I, les cellules filles sont:
a) diploides
b) hiploides
c) haploides
""")
if q3 == "c":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

time.sleep(2)
print("""

4e question""")
q4 = raw_input("""
Place dans le bon ordre:
a) Telophase - Prophase - Metaphase - Anaphase
b) Prophase - Metaphase - Anaphase - Telophase
c) Anaphase - Prophase - Metaphase - Telophase
d) Metaphase - Prophase - Telophase - Anaphase
""")
if q4 == "b":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

time.sleep(2)
print("""

5e question""")
q5 = raw_input("""
Apres la fin du Telophase II, combien de cellules filles est-ce qu'il y a?
a) 8
b) 69
c) 2
d) 4
""")
if q5 == "d":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

time.sleep(2)
print("""

6e question""")
q6 = raw_input("""
Il y a deux interphases.
a) vrai
b) faux
""")
if q6 == "b":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

time.sleep(2)
print("""

7e question""")
q7 = raw_input("""
La prophase I prend 90% de la duree totale de la meiose.
a) vrai
b) faux
""")
if q7 == "a":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

time.sleep(2)
print("""

8e question""")
q8 = raw_input("""
Comment peut-on decrire la meiose ?
   a) une division rationnelle
   b) une division equationnelle
   c) une division reductionnelle
""")
if q8 == "b" or "c":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

  time.sleep(2)
  print("""

  9e question""")
  q9 = raw_input("""
  Dans quel etape se produit les haploides de chromosomes répliqués?
   a) Prophase II
   b) Télophase I
   c) Anaphase II
  """)
  if q9 == "b":
    print("Bonne reponse!")
    score = score + 1
    print("Score:" + str(score))
  else:
    print("Mauvaise reponse!")
    print("Score:" + str(score))

  time.sleep(2)
  print("""

  10e question""")
  q10 = raw_input("""
  Qu'est-ce qu'une cellule diploide?
   a) 2n chromosomes
   b) n chromosomes
   c) 4n chromosomes
   d) 3n chromosomes
  """)
  if q10 == "a":
    print("Bonne reponse!")
    score = score + 1
    print("Score:" + str(score))
  else:
    print("Mauvaise reponse!")
    print("Score:" + str(score))

 time.sleep(2)
 print("""

 11e question""")
 q11 = raw_input("""
 Qu'est-ce qu'une cellule haploide?
  a) 2n chromosomes a 1 chromatide
  b) n chromosomes
  c) 4n chromosomes
  d) 3n chromosomes
 """)
 if q11 == "b":
   print("Bonne reponse!")
   score = score + 1
   print("Score:" + str(score))
 else:
   print("Mauvaise reponse!")
   print("Score:" + str(score))

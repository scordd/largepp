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
  Dans quel etape se produit les haploides de chromosomes repliques?
   a) Prophase 1
   b) Telophase 1
   c) Anaphase 2
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

 time.sleep(2)
 print("""

 12e question""")
 q12 = raw_input("""
 Quelle est la definition de la meiose?
  a) La succession de deux replications precedees d'une unique division
  b) Permet obtention de gametes haploides
  c) Permet obtention de gametes diploides
  d) Succession de deux divisions precedees d'une unique replication
 """)
 if q12 == "b" or "d":
   print("Bonne reponse!")
   score = score + 1
   print("Score:" + str(score))
 else:
   print("Mauvaise reponse!")
   print("Score:" + str(score))

 time.sleep(2)
 print("""

 13e question""")
 q13 = raw_input("""
 Qu'est ce qu'on obtient apres la premiere division de la meiose?
  a) 2 cellules a n chromosomes a deux chromatides
  b) 4 cellules a 2n chromosomes a une chromatide
  c) 2 cellules a 2n chromosomes a une chromatide
  d) 4 cellules a n chromosomes a une chromatide
 """)
 if q13 == "a":
   print("Bonne reponse!")
   score = score + 1
   print("Score:" + str(score))
 else:
   print("Mauvaise reponse!")
   print("Score:" + str(score))

 time.sleep(2)
 print("""

 14e question""")
 q14 = raw_input("""
 Le noyau d'un ovule humain renferme ...
 a) 23 chromosomes dont un chromosome X.
 b) 23 chromosomes dont un chromosome X ou Y.
 c) 22 Chromosomes dont un chromosome X.
 """)
 if q14 == "a":
   print("Bonne reponse!")
   score = score + 1
   print("Score:" + str(score))
 else:
   print("Mauvaise reponse!")
   print("Score:" + str(score))

 time.sleep(2)
 print("""

 15e question""")
 q15 = raw_input("""
 Le noyau des gamètes humains possedent ...
 a) 46 chromosomes.
 b) 23 chromosomes dont un chromosome sexuel.
 c) 23 paires de chromosomes dont une paire de chromosomes sexuels.
 """)
 if q15 == "c":
   print("Bonne reponse!")
   score = score + 1
   print("Score:" + str(score))
 else:
   print("Mauvaise reponse!")
   print("Score:" + str(score))

 time.sleep(2)
 print("""

 16e question""")
 q16 = raw_input("""
 Le sexe d'un enfant a naitre est determine par ...
 a) Le chromosome sexuel contenu dans le spermatozoide.
 b) Le chromosome sexuel contenu dans l'ovule.
 c) Le hasard au cours du developpement embryonnaire.
 """)
 if q16 == "c":
   print("Bonne reponse!")
   score = score + 1
   print("Score:" + str(score))
 else:
   print("Mauvaise reponse!")
   print("Score:" + str(score))

time.sleep(2)
print("""

17e question""")
q17 = raw_input("""
Le noyau d'un spermatozoide humain renferme ...
a) 23 chromosomes dont un chromosome X.
b) 23 chromosomes dont un chromosome X ou Y.
c) 22 chromosomes dont un chromosome X ou Y.
""")
if q17 == "b":
  print("Bonne reponse!")
  score = score + 1
  print("Score:" + str(score))
else:
  print("Mauvaise reponse!")
  print("Score:" + str(score))

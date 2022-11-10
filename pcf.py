from random import *

i=0

print("Veuillez choisir le mode de jeu")
print("1) 1 contre 1 (nécessite 2 joueurs)")
print("2) Jouer contre ordinateur")
result=int(input("Votre Réponse : "))

if result==1 :
  print("\nJOUEUR 1 A VOUS DE JOUER !!")
  print("1)Pierre  2) Papier  3) Ciseaux")
  ja=int(input("Votre réponse : "))
  for i in range(30):
    print("*")
  print("\n=============================\n")
  print("JOUEUR 2 A VOUS DE JOUER !!")
  print("1) Pierre  2) Papier  3) Ciseaux")
  jb=int(input("Votre Réponse : "))

  for i in range(0,30):
    print("*")
  print("\n==============================\n")

  if ja==1:
    if jb==1:
      print("Les deux joueurs ont joué Pierre ! C'est un match nul ! ")
    elif jb==2:
      print("La Feuille couvre la Pierre !  C'est le joueur 2 qui gagne !")
    elif jb==3:
      print("La Pierre casse les Ciseaux ! C'est le joueur 1 qui gagne !")
  
  if ja==2:
    if jb==1:
      print("La feuille couvre la Pierre ! C'est le joueur 1 qui gagne !")
    if jb==2:
      print("Les deux joueurs ont joué Feuille ! C'est un match nul !")
    if jb==3:
      print("Les Ciseaux coupent le Papier ! C'est le joueur 2 qui gagne !")
 
  if ja==3:
    if jb==1:
      print("La Pierre casse les Ciseaux ! C'est la joueur 2 qui gagne !")
    if jb==2:
      print("Les Ciseaux coupent le Papier ! C'est le joueur 1 qui gagne !")
    if jb==3:
      print("Les deux joueurs ont joué Ciseaux ! C'est un match nul !")

if result==2 :
  print("\nJOUEUR 1 A VOUS DE JOUER !!")
  print("1)Pierre  2) Papier  3) Ciseaux")
  ja=int(input("Votre réponse : "))

  print("\n=============================\n")

  jb=randrange(1,3)

  if ja==1:
    if jb==1:
      print("Les deux joueurs ont joué Pierre ! C'est un match nul ! ")
    elif jb==2:
      print("La Feuille couvre la Pierre !  C'est le joueur 2 qui gagne !")
    elif jb==3:
      print("La Pierre casse les Ciseaux ! C'est le joueur 1 qui gagne !")
  
  if ja==2:
    if jb==1:
      print("La feuille couvre la Pierre ! C'est le joueur 1 qui gagne !")
    if jb==2:
      print("Les deux joueurs ont joué Feuille ! C'est un match nul !")
    if jb==3:
      print("Les Ciseaux coupent le Papier ! C'est le joueur 2 qui gagne !")
 
  if ja==3:
    if jb==1:
      print("La Pierre casse les Ciseaux ! C'est la joueur 2 qui gagne !")
    if jb==2:
      print("Les Ciseaux coupent le Papier ! C'est le joueur 1 qui gagne !")
    if jb==3:
      print("Les deux joueurs ont joué Ciseaux ! C'est un match nul !")


  
  

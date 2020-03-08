from random import *
import matplotlib.pyplot as plt

def graphique(liste):
    n = len(liste)
    plt.clf()
    plt.xlabel("k paramètre de taille d'échantillon (10^k)")
    plt.ylabel("Moyenne")
    listex = list(range(1, n + 1))
    listey = liste
    plt.plot(listex, listey, 'bo')
    plt.savefig('graphique.png')

def de(x):
  return randint(1,x)
  
def echantillon1(x):
  liste=[]
  for k in range(x):
    liste.append(randint(1,6))
  return liste

def echantillon2(x):
  return [randint(1,6) for k in range(x)]
      
def somme1(liste):
  somme=0
  n=len(liste)
  for k in range(n):
    somme=somme+liste[k]
  return somme
    
def somme2(liste):
  somme=0
  for nombre in liste:
    somme=somme+nombre
  return somme
    
def moyenne(liste):
  n=len(liste)
  return (somme2(liste))/n

L=[moyenne(echantillon2(10**k)) for k in range(1,6)]

def somme_deux_des(x):
  return (de(x) + de(x))

def echantillon_deux_des(x):
  return [somme_deux_des(6) for k in range(1,x)]

def premier6():
  r = 1
  while randint(1,6) != 6:
    r = r + 1
  return r

def echantillon_premier6(x):
  return ([premier6() for z in range (1,x)])

def gain1():
  boule = randint(1,5)
  if boule == 1:
    return +10
  elif boule == 3:
    return +1
  else:
    return -5

def echantillon_gain1(x):
  return ([gain1() for z in range (1,x)])

def gain2():
  boule = random()
  if b

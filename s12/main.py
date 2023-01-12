#Import pour les fct Matrix
import umage
#...
#Import pour les fct rational
import rational


# Char manipulation
def plus_grand_bord(w):
  """ fonction plus_grand_bord
  Args:
    w (str): un mot en parametre
  Returns:
    retourne le plus grand bord de ce mot. Si w n'a pas de bord, la fonction retourne None.
  """
  bord = ''
  i = 0
  n = len(w)
  m = (i+n)//2
  while (i<m and m<n):
    if w[i] == w[m] :
      bord += w[i]
      i+=1
    m += 1
  if bord !='':
    return bord 
  else:
    return 



def intersection(v, w):
  """fonction intersection(v, w)
  Args:
    v (_str_): un mot
    w (_str_): un mot
  Returns:
    Retourne la plus grande partie commune à ces deux:
    c'est l'intersection entre le mot v et le mot w. 
  """
  if len(v) > len(w): # O(1)
    v, w = w, v     # O(1)
  max = ""            # O(1)
  for i in range(len(v)):                 # O(n)
    for length in range(len(v) - i):        # O(n)
      for j in range(len(w) - i):             # O(n)
        if v[i:i+length] == w[j:j+length]: # O(1) + O(1) + O(1)
          if len(max) < length:                  # O(1) + O(1)
            max = v[i:i+length]            # O(1)
  return max


def anagrammes(v, w):
  """ fonction anagrammes(v, w)
  Args:
    v (_str_): chaine de caractere
    w (_str_): chaine de caractere
  Returns:
    retourne vrai si et seulement si les mots v et w sont anagrammes.
  """
  trouve = False
  if len(v) == len(w):
    for c in range(len(v)):
      if v[c] in w:
        trouve = True
      else:
        return False
  return trouve


def palindrome(v):
  """fonction palindrome(v)
  Args:
    v (_str_): chaine de caractaire
   Returns:
    retourne vrai si et seulement si le mot v est un palindrome
  """    
  mot_inver = "" # O(1)
  i = len(v)-1 # O(1)
  while(i>=0): # n fois: ici n represente la longueur(taille) du mot V
    mot_inver += v[i] # O(1)
    i-=1 # O(1)
  if v == mot_inver: # O(1)
    return True # O(1)
  else:
    return False # O(1)


def is_symmetrical(img):
  """Algorithme de Symmetrical
  Args:
    img (_List_): c'est une matrice de representation d'une image
  Retourns:
    retourne la valeur booléenne True si l'image passée en paramètre 
    possède un axe de symétrie orthogonal horizontal ou vertical.
  """
  lim= len(img)
  Vertical= True
  Horizontal = True
  for i in range(lim//2):
    if img[i]!= img[(lim-1-i)]:
      Horizontal = False
  for i in range(len(img)):
    for j in range(len(img[0])//2):
      if img[i][j] != img[i][len(img[0])-1-j]:
        Vertical = False
  if Vertical or Horizontal:
    return  True
  else:
    return False

from PIL import Image,ImageFilter
def flou(img, r):
  """retourne une image floue de img"""
  image = Image.open(img2)
  blurry_image= image.filer(ImageFilter.BLUR)
  return blurry_image


# Chiffrement
def chiffrement_vigenere(texte, mot_cle):
  """ retourne le texte chiffre par le mot_cle"""
  key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  crypted_txt = ""
  mot_cle = mot_cle.upper()
  texte = texte.upper()
  for i in range(len(texte)):
    decal = key.index(mot_cle[i % len(mot_cle)])
    crypted_txt += key[(key.index(texte[i]) + decal) % 26]
  return crypted_txt


# print(chiffrement_vigenere("appelernordtroupesville", "rouge"))


def dechiffrement_vigenere(w, k):
  """retourne le dechiffrement de w avec la cle k"""
  key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  crypted_txt = ""
  with open(w, 'r') as fichier:
    content = fichier.read()
    mot_cle = k.upper()
    texte = content.upper()
    for i in range(len(texte)):
      decal = key.index(mot_cle[i % len(mot_cle)])
      crypted_txt += key[(key.index(texte[i]) - decal) % 26]
  return crypted_txt

print(dechiffrement_vigenere("vigenere.txt", "algorithme"))

# 1.4 Objets
# voir le module rational.py
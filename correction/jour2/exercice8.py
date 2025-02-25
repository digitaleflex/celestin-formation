import math

# Saisie utilisateur
nombre_decimal = float(input("Entrez un nombre décimal: "))

# Arrondis
arrondi_proche = round(nombre_decimal)
arrondi_deux_decimales = round(nombre_decimal, 2)
arrondi_inferieur = math.floor(nombre_decimal)
arrondi_superieur = math.ceil(nombre_decimal)

# Affichage
print(f"Arrondi à l'entier le plus proche: {arrondi_proche}")
print(f"Arrondi à deux décimales: {arrondi_deux_decimales}")
print(f"Arrondi à l'unité inférieure: {arrondi_inferieur}")
print(f"Arrondi à l'unité supérieure: {arrondi_superieur}")
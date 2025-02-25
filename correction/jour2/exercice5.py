# Saisie utilisateur
nombre_entier = int(input("Entrez un nombre entier: "))

# Conversions
nombre_flottant = float(nombre_entier)
nombre_chaine = str(nombre_entier)

# Affichage des résultats
print(f"Nombre flottant: {nombre_flottant}, Type: {type(nombre_flottant)}")
print(f"Nombre en chaîne: {nombre_chaine}, Type: {type(nombre_chaine)}")

# Conversion inverse
chaine_flottante = "3.14159"
nombre_converti = float(chaine_flottante)
print(f"Conversion de '3.14159' en flottant: {nombre_converti}, Type: {type(nombre_converti)}")
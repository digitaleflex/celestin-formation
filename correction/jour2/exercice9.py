# Saisie utilisateur
valeur = input("Entrez une valeur: ")

# Vérification du type
if valeur.isdigit():  # Vérifie si c'est un entier
    print("La valeur est un entier.")
elif valeur.replace('.', '', 1).isdigit():  # Vérifie si c'est un flottant
    print("La valeur est un flottant.")
else:
    print("La valeur est une chaîne de caractères.")
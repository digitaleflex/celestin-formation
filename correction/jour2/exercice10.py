# Saisie utilisateur
lettre = input("Entrez une lettre: ")

# Conversion en ASCII
code_ascii = ord(lettre)
nouveau_code = code_ascii + 3
nouvelle_lettre = chr(nouveau_code)

# Affichage
print(f"Code ASCII de '{lettre}': {code_ascii}")
print(f"Nouvelle lettre après ajout de 3: {nouvelle_lettre}")

""" # Inverse
valeur_ascii = int(input("Entrez un code ASCII: "))
lettre_correspondante = chr(valeur_ascii)
print(f"Lettre correspondante: {lettre_correspondante}") """
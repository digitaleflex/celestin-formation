# Saisie des notes
note1 = float(input("Entrez la première note: "))
note2 = float(input("Entrez la deuxième note: "))
note3 = float(input("Entrez la troisième note: "))

# Calcul de la moyenne
moyenne = (note1 + note2 + note3) / 3

# Affichage avec deux chiffres après la virgule
print(f"Moyenne: {moyenne:.2f}")
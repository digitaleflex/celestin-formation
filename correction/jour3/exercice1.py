def check_age() -> None:
    """Demande l'âge à l'utilisateur et affiche sa catégorie."""
    try:
        age: int = int(input("Entrez votre âge : "))
        if age < 0:
            print("L'âge ne peut pas être négatif.")
        elif age < 18:
            print("Vous êtes mineur.")
        elif age < 65:
            print("Vous êtes majeur.")
        else:
            print("Vous êtes senior.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
check_age()
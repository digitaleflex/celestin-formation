def sum_of_integers() -> None:
    """Calcule et affiche la somme des entiers jusqu'à un nombre donné."""
    try:
        number: int = int(input("Entrez un nombre entier positif : "))
        if number < 0:
            print("Le nombre doit être positif.")
        else:
            total: int = sum(range(1, number + 1))
            print(f"La somme des entiers de 1 à {number} est : {total}")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
sum_of_integers()
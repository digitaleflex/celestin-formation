def display_even_numbers() -> None:
    """Affiche tous les nombres pairs jusqu'à un nombre donné."""
    try:
        limit: int = int(input("Entrez un nombre entier positif : "))
        if limit < 0:
            print("Le nombre doit être positif.")
        else:
            print(f"Nombres pairs jusqu'à {limit} : {[n for n in range(0, limit + 1, 2)]}")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
display_even_numbers()
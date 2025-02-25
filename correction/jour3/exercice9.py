def squares_list() -> None:
    """Crée et affiche une liste des carrés des nombres jusqu'à un nombre donné."""
    try:
        number: int = int(input("Entrez un nombre entier : "))
        if number < 0:
            print("Le nombre doit être positif.")
        else:
            squares: list[int] = [n**2 for n in range(1, number + 1)]
            print(f"Liste des carrés : {squares}")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
squares_list()
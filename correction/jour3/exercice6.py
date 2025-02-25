def multiplication_table() -> None:
    """Affiche la table de multiplication d'un nombre jusqu'à 12."""
    try:
        number: int = int(input("Entrez un nombre : "))
        print(f"Table de multiplication de {number} :")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
multiplication_table()
def reverse_word() -> None:
    """Affiche un mot inversé."""
    word: str = input("Entrez un mot : ")
    reversed_word: str = word[::-1]
    print(f"Mot inversé : {reversed_word}")

# Appel de la fonction
reverse_word()
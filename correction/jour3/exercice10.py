def is_palindrome() -> None:
    """Vérifie si un mot est un palindrome."""
    word: str = input("Entrez un mot : ").lower()
    if word == word[::-1]:
        print("C'est un palindrome.")
    else:
        print("Ce n'est pas un palindrome.")

# Appel de la fonction
is_palindrome()
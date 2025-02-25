def count_vowels() -> None:
    """Compte et affiche le nombre de voyelles dans un mot."""
    vowels: set = {'a', 'e', 'i', 'o', 'u', 'y'}
    word: str = input("Entrez un mot : ").lower()
    count: int = sum(1 for char in word if char in vowels)
    print(f"Nombre de voyelles : {count}")

# Appel de la fonction
count_vowels()
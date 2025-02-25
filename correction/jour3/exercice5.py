import random

def guess_the_number() -> None:
    """Jeu où l'utilisateur doit deviner un nombre aléatoire."""
    secret_number: int = random.randint(1, 10)
    attempts: int = 0

    while True:
        try:
            guess: int = int(input("Devinez le nombre entre 1 et 10 : "))
            attempts += 1
            if guess < secret_number:
                print("Trop petit !")
            elif guess > secret_number:
                print("Trop grand !")
            else:
                print(f"Félicitations ! Vous avez trouvé en {attempts} tentative(s).")
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
guess_the_number()
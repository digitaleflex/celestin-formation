def evaluate_grade() -> None:
    """Demande une note et affiche une appréciation."""
    try:
        grade: int = int(input("Entrez une note sur 100 : "))
        if not 0 <= grade <= 100:
            print("La note doit être entre 0 et 100.")
        elif grade >= 90:
            print("Excellent")
        elif grade >= 70:
            print("Bien")
        elif grade >= 50:
            print("Moyenne")
        else:
            print("Insuffisant")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
evaluate_grade()
from datetime import datetime

# Saisie utilisateur
annee_naissance = int(input("Entrez votre année de naissance: "))

# Calcul de l'âge actuel
annee_actuelle = datetime.now().year
age_actuel = annee_actuelle - annee_naissance

# Âge dans 10 ans
age_future = age_actuel + 10
20
# Affichage
print(f"Vous avez {age_actuel} ans.")
print(f"Dans 10 ans, vous aurez {age_future} ans.")
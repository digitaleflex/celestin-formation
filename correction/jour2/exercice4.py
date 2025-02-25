# Saisie utilisateur
prenom = input("Entrez votre prénom: ")
ville = input("Entrez votre ville: ")

# Concaténation avec +
message_concat = "Bonjour " + prenom + ", tu habites à " + ville + " !"
print(message_concat)

# Formatage avec f-strings
message_fstring = f"Bonjour {prenom}, tu habites à {ville} !"
print(message_fstring)

# Formatage avec .format()
message_format = "Bonjour {}, tu habites à {} !".format(prenom, ville)
print(message_format)
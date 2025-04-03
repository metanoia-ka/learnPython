import pandas as pd

#Ajoute une colonne "total" (prix * quantite) et sauvegarde.
#Choisir d'utiliser pandas pour lire et écrire des fichiers csv avec plus de flexibilité.

#Lecture du fichier de ventes.csv
ventes = pd.read_csv("ventes.csv")

#Ajoute une colonne "total" (prix * quantite)
ventes["total"] = ventes["prix"] * ventes["quantite"]

#Sauvegarde le fichier csv avec la nouvelle colonne
ventes.to_csv("ventes.csv", index=False)
print(ventes) # affiche le dataframe

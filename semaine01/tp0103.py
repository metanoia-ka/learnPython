import pandas as pd

#Trier les produits par prix croissant et sauvegarder le fichier trié

#Charger les produits 'produits.csv'
produits = pd.read_csv('produits.csv')


produits.sort_values(by='prix', ascending=False, inplace=True)
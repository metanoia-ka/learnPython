import pandas as pd

#Trier les produits par prix croissant et sauvegarder le fichier trié

#Charger les produits 'produits.csv'
produits = pd.read_csv('produits.csv')

produits.sort_values(by='prix', ascending=False, inplace=True)

produits.to_csv('produits_trie.csv', index=False) # Sauvegarder le fichier trié
print(produits) # Afficher le fichier trié
print("Le fichier trié a été sauvegardé sous le nom 'produits_trie.csv'")
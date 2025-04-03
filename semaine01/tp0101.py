import json

with open("utilisateurs.json", "r", encoding="utf-8") as f:
    utilisateurs = json.load(f)
    
    majeurs = [utilisateur for utilisateur in utilisateurs if utilisateur["age"] >= 18]
    
    with open("majeurs.json", "w", encoding="utf-8") as f:
        json.dump(majeurs, f, indent=4)
        
print("✅ Fichier 'majeurs.json' créé avec succès !")
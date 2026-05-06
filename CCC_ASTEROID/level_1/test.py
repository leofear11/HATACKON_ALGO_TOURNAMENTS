# 1. Ouvrir le fichier
with open("level1_2_large.in", "r") as f:
    lines = f.readlines()

# 2. Lire le nombre d'éléments (souvent sur la 1ère ligne)
n = int(lines[0].strip())

# 3. Traiter les données (adapter selon l'énoncé exact)
resultats = []
for i in range(1, n + 1):
    donnees = lines[i].split() # Sépare par les espaces
    
    # Exemple de traitement : Mining Rectangle
    w = int(donnees[0])
    h = int(donnees[1])
    
    # Bordure supérieure
    resultats.append("#"*(w+2))
    print("#"*(w+2))
    
    # Bordure latérale
    for _ in range(h):
        resultats.append("#" + ":"*(w) + "#")
        print("#" + ":"*(w) + "#")
        
    # Bordure inférieure
    resultats.append("#"*(w+2))
    print("#"*(w+2))


# 5. Créer le fichier de sortie
with open("solution_level1_1_large.out", "w") as out:
    out.write("\n".join(resultats))
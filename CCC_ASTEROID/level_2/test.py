# On ouvre les deux fichiers en même temps
with open("level2_2_large.in", "r") as f_in, open("solution_level2_2_large.out", "w") as f_out:
    lines = f_in.readlines()
    
    n = int(lines[0].strip())
    i = 1
    
    for _ in range(n):
        # Lecture de W et H
        data = lines[i].split()
        if not data: break
        
        w, h = int(data[0]), int(data[1])
        i += 1
        
        grille = []
        # Lecture de la grille (h+2 lignes)
        for _ in range(h + 2):
            if i < len(lines):
                # On garde les espaces mais on enlève le saut de ligne
                ligne = list(lines[i].rstrip('\n\r'))
                grille.append(ligne)
                i += 1

        # Traitement de la colonne cible
        for row in range(len(grille)):
            # Vérifie si la ligne est assez longue pour atteindre la colonne w-1
            if len(grille[row]) >= w:
                if grille[row][w-1] == ":":
                    grille[row][w-1] = "X"
        
        # Écriture immédiate dans le fichier de sortie
        for row in grille:
            f_out.write("".join(row) + "\n")
        
        # Sauter la ligne vide entre les blocs si nécessaire
        i += 1 

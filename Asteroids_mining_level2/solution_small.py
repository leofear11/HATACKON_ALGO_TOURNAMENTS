def resoudre_forage():
    try:
        with open("level2_1_small.in", "r") as f:
            lignes = [l.strip() for l in f.readlines() if l.strip()]
    except FileNotFoundError:
        print("Erreur : Le fichier .in est introuvable.")
        return
    if not lignes:
        return

    nombre_asteroides = int(lignes[0])
    curseur = 1
    resultats = []

    for _ in range(nombre_asteroides):
        dimensions = lignes[curseur].split()
        largeur_minable = int(dimensions[0])
        hauteur_minable = int(dimensions[1])
        curseur += 1

        hauteur_totale = hauteur_minable + 2  # ligne S + lignes minables + fond
        grille = []
        for i in range(hauteur_totale):
            grille.append(list(lignes[curseur]))
            curseur += 1

        # Trouver 'S' dans la première ligne
        index_S = grille[0].index('S')

        # Forer verticalement sous le S, arrêt sur '#'
        for num_ligne in range(1, hauteur_totale - 1):
            cellule = grille[num_ligne][index_S]
            if cellule == ':':
                grille[num_ligne][index_S] = 'X'
            elif cellule == '#':
                break  # obstacle infranchissable

        # Ajouter les lignes de cet astéroïde SANS ligne vide séparatrice
        for ligne_liste in grille:
            resultats.append("".join(ligne_liste))

    # Écriture sans ligne vide finale superflue
    with open("level2_1_small.out", "w") as f_out:
        f_out.write("\n".join(resultats) + "\n")

    print("Terminé ! Le fichier level2_1_small.out a été généré.")

resoudre_forage()
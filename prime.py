"""
Nombres Premiers Supprimables - CCC Cloudflight Niveau 1
=========================================================
Un nombre premier supprimable est un nombre premier où on peut
supprimer des chiffres un par un et chaque résultat reste premier,
jusqu'à obtenir un chiffre unique premier (2, 3, 5, 7).

On compte le nombre de chemins valides jusqu'à un chiffre unique.
"""


# ─────────────────────────────────────────
# 1. TEST DE PRIMALITÉ
#    Miller-Rabin déterministe — aucune dépendance externe
#    Fonctionne pour n < 3.3 × 10^24
# ─────────────────────────────────────────

PETITS_PREMIERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def est_premier(n: int) -> bool:
    """Retourne Vrai si n est un nombre premier."""
    if n < 2:
        return False
    if n in PETITS_PREMIERS:
        return True
    if any(n % p == 0 for p in PETITS_PREMIERS):
        return False

    # Décomposer n-1 = 2^r × d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Vérification avec chaque témoin
    for temoin in PETITS_PREMIERS:
        if temoin >= n:
            continue
        x = pow(temoin, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# ─────────────────────────────────────────
# 2. SUPPRESSION D'UN CHIFFRE
# ─────────────────────────────────────────

def supprimer_chiffre(nombre: str, index: int) -> int:
    """Supprime le chiffre à la position donnée et retourne le nombre résultant."""
    return int(nombre[:index] + nombre[index+1:])


# ─────────────────────────────────────────
# 3. COMPTAGE DES CHEMINS VALIDES
#    Récursion avec mémoïsation
# ─────────────────────────────────────────

def compter_chemins(n: int, memo: dict) -> int:
    """
    Retourne le nombre de chemins valides pour réduire n
    jusqu'à un chiffre unique premier.
    """
    if n in memo:
        return memo[n]

    # n doit être premier pour appartenir à un chemin valide
    if not est_premier(n):
        memo[n] = 0
        return 0

    chiffres = str(n)

    # Cas de base : chiffre unique premier atteint
    if len(chiffres) == 1:
        memo[n] = 1
        return 1

    # Récursion : on essaie de supprimer chaque chiffre un par un
    total = 0
    for i in range(len(chiffres)):
        sous_nombre = supprimer_chiffre(chiffres, i)
        if sous_nombre > 0:
            total += compter_chemins(sous_nombre, memo)

    memo[n] = total
    return total


# ─────────────────────────────────────────
# 4. TESTS DE VALIDATION
# ─────────────────────────────────────────

def lancer_tests():
    """Vérifie les cas connus pour valider l'algorithme."""
    cas_de_test = [
        (4567, 3),   # exemple du PDF
        (7,    1),   # chiffre premier unique
        (47,   1),   # 47 → 7
        (67,   1),   # 67 → 7
        (57,   0),   # 57 = 3×19, pas premier
        (4,    0),   # 4 pas premier
        (2,    1),   # plus petit premier
    ]

    print("=== Tests de validation ===")
    tous_reussis = True
    for n, attendu in cas_de_test:
        resultat = compter_chemins(n, {})
        reussi = resultat == attendu
        statut = "✓" if reussi else "✗"
        print(f"  {statut}  compter_chemins({n}) = {resultat}  (attendu : {attendu})")
        if not reussi:
            tous_reussis = False

    print()
    if tous_reussis:
        print("  Tous les tests sont passés ✓")
    else:
        print("  Certains tests ont échoué ✗")


# ─────────────────────────────────────────
# 5. PROGRAMME PRINCIPAL
# ─────────────────────────────────────────

def main():
    lancer_tests()
    print()
    n = int(input("Entrez un nombre : "))
    memo = {}
    resultat = compter_chemins(n, memo)
    print(f"Nombre de chemins valides : {resultat}")


if __name__ == "__main__":
    main()
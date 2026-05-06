# 1. Ouvrir le fichier
with open("level1_1_small.in", "r") as f:
    lines = f.readlines()

# 2. Lire le nombre d'éléments (souvent sur la 1ère ligne)
n = int(lines[0].strip())

print(n)

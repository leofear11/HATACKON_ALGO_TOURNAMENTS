# 1 - OUVRIR LE FICHIER IN
with open("level2_0_example.in", "r") as f:
    lines = f.read().strip().splitlines()

# 2 - LIRE LE NOMBRE D'ÉLÉMENTS
n = int(lines[0])

for _ in range(n):
    for element in lines[1:]:
        if element.startswith("3"):
            element.split()
        
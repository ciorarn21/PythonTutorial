# 🔁 Exemple basique de toutes les boucles en Python

print("=== Boucle for ===")
for i in range(3):
    print("for loop:", i)

for i in range(0,100,2):
    print(f"La valeur est : {i}")

# Petite subtilité .... pour les boucles for. Si vous n'avez pas besoin de i, vous pouvez le rendre muet avec _
# Exemple 

for _ in range(5):
    print("Le message s'affichera 5 fois")


print("\n=== Boucle while ===")
i = 0
while i < 3:
    print("while loop:", i)
    i += 1

print("\n=== Simulation do…while ===")
i = 0
while True:
    print("do…while simulé:", i)
    i += 1
    if i >= 3:
        break

print("\n=== Boucle while…else ===")
i = 0
while i < 3:
    print("while…else:", i)
    i += 1
else:
    print("La boucle s'est terminée normalement")



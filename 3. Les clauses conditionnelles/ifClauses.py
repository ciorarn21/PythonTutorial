x = 10
y = 5
z = -3

# ---- Exemple simple de if / elif / else ----
if x > y:
    print("x est plus grand que y")
elif x == y:
    print("x et y sont égaux")
else:
    print("x est plus petit que y")

print()  # saut de ligne pour aérer

# ---- Exemple avec plusieurs conditions (and, or, not) ----
if x > 0 and y > 0:
    print("x et y sont positifs")

if x > 0 or z > 0:
    print("Au moins une des deux variables x ou z est positive")

if not (z > 0):
    print("z n’est pas positif (il est nul ou négatif)")

print()

# ---- Combinaison plus complexe ----
if (x > y and y > z) or (x == 10 and not (z > 0)):
    print("Condition complexe vérifiée ✅")
else:
    print("Condition complexe non vérifiée ❌")

print()

# ---- Bonus : condition courte (ternaire) ----
message = "x est pair" if x % 2 == 0 else "x est impair"
print(message)
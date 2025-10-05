
# La saisi des variables

numero : int = 5
numeroB : int = 10

print(numero + numeroB)

# La récupération des inputs

saisi : str = input("Où sont les dias de Bastin ?\n")

print("N'oubliez pas de presser enter pour confirmer votre saisi hein",end="\n")

print("Les dias se trouvent ...", saisi)

# Pour le formattage des strings ..

variable : int = 4520
print("La valeur est :", variable)

# Vous pouvez très bien faire ceci :

print(f"La valeur est {variable}") # Ici les accolades servent à indiquer la variable à afficher

# Mais la manière suivante est tout à fait juste aussi :

phrase : str = f"La valeur est {variable}"

print(phrase) # Ca fonctionne exactement de la même manière.



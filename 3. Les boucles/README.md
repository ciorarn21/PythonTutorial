# 🔁 Les boucles en Python et comparaison avec C++

Les boucles permettent d’exécuter **plusieurs fois** un même bloc de code.  
En Python, on retrouve principalement **`for`**, **`while`**, et **`while…else`**.  
Il n’existe pas de `do…while` comme en C++.

---

## 1️⃣ La boucle `for`

### En C++ :
```cpp
for(int i = 0; i < 5; i++) {
    cout << i << endl;
}

```

En python, cela donne :

```python
for i in range(5):
  print(i)

# A savoir que la fonction range peut prendre plusieurs paramètres. 
# Le 1er correspond à la valeur initiale de i, la 2ème à celle à atteindre, et la 3ème le step. C-a-d la valeur qui sera additionnée à i lors de chaque itération.

# exemple

for i in range(0,100,2):
  print(i)
# Cela ne va m'afficher que les nombres paires.

```

## 2️⃣ La boucle while

### En C++
```cpp
int i = 0;
while(i < 5) {
    cout << i << endl;
    i++;
}
```

### En Python 
``` python
i = 0
while i < 5:
    print(i)
    i += 1

```

### La petite spécificité de python ... La boucle while...else 

Python a une subtilité qu’on ne trouve pas en C++ : un bloc else peut suivre un while.
Il s’exécute seulement si la boucle n’a pas été interrompue par un break.

```python 
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("La boucle s'est terminée normalement")
```

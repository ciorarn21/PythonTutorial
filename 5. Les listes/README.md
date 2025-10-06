# 🐍 Ici on va surtout s'attaquer aux listes en python

## En C++ 
Une liste ( ou un tableau ) se déclare de la manière suivante : 
```cpp

std::vector<Type> monVecteur;

```

## En python, il suffit tout simplement d'écrire : <br>

```python

maListe : list[Type] = list()
# Ceci initialisera un tableau vide.

```

## Comment manipuler un tableau en python ? 

 - Si l'on souhaite déclarer un tableau avec directement des élements, on peut le faire ainsi : <br>

```python

maListe : list[Type] = [élémentA, élémentB,..., élémentN]

#Maintenant pour rajouter un élement, la variable possède une fonction .append() qui fait exactement celà.

maListe.append(élémentN+1)

# Comment connaitre la taille d'un tableau ? Tout simplement grâce à la fonction len()

print(len(maListe)) # Renvoie la taille du tableau.

```

  - Comment itérer à travers un tableau ?
    C'est aussi simple que ça : <br>

    ```python
      maListe : list[type] = [......]
    
      for elem in maListe:
          print(elem)
    
      # 👀 Astuce : Vous désirez savoir si un élément est dans un tableau ? Python propose la manière suivante :

      if (elementQuelconque in maListe):
        print("Il y est")
      else:
        print("Il n'y est pas...")

    # Autre astuce : Vous voulez déclarer par exemple un tableau avec N fois un élément ? Il suffit de faire ceci :
    N : int = 5
    maListe : list[type] = [elementQuelconque] * N

    # en affichant sa taille vous verrez bien qu'il aura la taille N

    print(len(maListe)) # = N 
    
    ```

    - Dernière astuce : Comment sélectionner l'élément i jusqu'à j dans un tableau de taille N ?
   
    ```python

    maListe : list[type] = [.....]
    maSelection : list[type] = maListe[i:j,0] # Le 0 ici renvoie au premier tableau dans le cas où vous auriez des tableaux encapsulés ( comme dans le cas d'une matrice par exemple )
    # A savoir que maListe[:,0] donc sans les i,j parcours l'ensemble des éléments du tableau.

    # D'autant plus que les indices négatifs ici sont acceptés ! Ils renvoient juste les élements mais en sens inverse.

    print(maListe[-1] == maListe[len(maListe) -]) # Normalement vous devriez avoir un True
    
  
    ```

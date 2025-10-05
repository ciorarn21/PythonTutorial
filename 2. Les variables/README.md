# 🧠 Rappel de la déclaration des variables en C++ et comparaison avec Python

⚠️ Pour tout ce qui va suivre, un fichier variable.py sera à votre disposition afin de tester tout ce qui va suivre dans cette section.

Comme vous devriez le savoir, une variable en C++ se déclare de la sorte `Type NomDeLaVariable = SaValeur;`,<br> en Python il ne suffit que de taper `NomDeLaVariable = SaValeur`

## 1. Exemple concret :
``` cpp
 int variable = 5; # En C++
 variable = 5 # En Python
```
### ⚠️ ***Remarque*** :
 1. En python, les ; ne sont pas nécéssaires contrairement en C++.
 2. Le typage de la variable non plus n'est pas nécéssaire ( mais bien que je vous invite à le faire pour plus de clarter dans votre code, nous verrons ceci par la suite.
 3. En Python, les types de de base sont les suivantes :
    - int ( pour les entiers positifs tout comme négatifs
    - float ( pour les nombres à virgule flottantes, à la nuance prêt que là où C++ fait la différence entre les float et les double, ce n'est pas le cas ici. )
    - str ( pour les string ).
    - None ( l'équivalent en quelque sorte de void en C++ )
    - list ( pour les tableaux - équivalent des std::vector<type> en C++.)
    - tuple ( une variante des tableaux, à la différence prêt qu'il est immuable.)
    - dict ( une autre variable qui combine l'avantage que les éléments du tableau sont récupérables grâce à un nom arbitraire)
    - Ces 3 derniers types seront davantages détaillés dans leur section dédiée.
   
 ### ⚠️ ***Les operateurs en python***
   - Ils sont tous exactement les mêmes qu'en C++ à la différence prêt que l'opérateur ++ ( pour incrémenter une variable ) n'existe pas. Vous devrez faire "maVariable += 1".
   - ** sert d'opérateur pour marquer un exposant <br>
```python
a : int = 5
b : int = a**2

print(b) # Normalement vous aurez 25 comme résultat.

```
   

### Comment Python gère les bloques de code contrairement au C++ :
En C++, vous savez à quel point les accolades sont ***hyper*** importantes pour définir ce qu'est un bloque de code.<br>Pour une fonction quelconque, celà ressemblera à ça : 
``` cpp
void fonction(){
  typeA variableA = ....;
  typeB variableB = ....;
}
```

Cela ne posera aucun problème si vous lui définissez votre fonction de la sorte : 
``` 
void fonction(){
              typeA variableA = ....;
    typeB variableB = ....;
}
```
✅ Le résultat restera toujours le même.

Il s'en contrefout du décalage des variables d'une ligne à l'autre étant donné que son bloque est déterminé par les {}.<br>
Ce n'est pas le cas en Python. Ce que lui considère comme étant un bloque de code c'est l'allignement d'une ligne par rapport à l'autre 
```python

def fonction():
  variablA = ...
  variableB = ...
```
✅ Ceci est correct car leur allignement est le même.

Au contraire, si vous aviez fait ceci :

``` python
def fonction():
  variablA = ...
      variableB = ...
```

❌ Le code ne fonctionnera pas vu que les variables ne sont pas correctement allignées.

### ⚠️ Bien que python ne vous oblige pas à typer vos variables, je vous invite grandement à le faire.<br>
Il est extrêment fréquent de se retrouver avec des erreurs difficiles à débugger tout simplement parce que vous avez mélangé des variables de type différent. <br>

Le typage se fait ainsi : 
``` python
maVariable : type = maValeur
# Exemple :

numero : int = 1
mot : str = "MaPhrase"

```

### ⚠️ Ne vous en faites pas pour "def", etc... Tout ceci sera abordé dans la section des fonctions.

# 📺 ✒️ Comment afficher quelque chose dans la console et récupérer une entrée du clavier ? 

## L'affichage sur la console en python se fait tout simplement à l'aide de la fonction "print("Ta mère")":<br>
Un exemple : 
```python
maPhrase : str = "Où sont les dias de Bastin ?"
print(maPhrase)
```
⚠️ Remarque sur la fonction print(). De base, elle fait d'elle-même le saut de ligne lors du prochain print(). <br>
Si vous ne voulez pas que celà arrive, alors faites ainsi : 
```python
print("Quelque chose", end="") # De base, la fonction rajoute automatiquement le \n pour un saut de ligne.
```

## Récupérer la saisi clavier d'un utilisateur, tout simplement grâce à la fonction "input()". <br> Un exemple :
```python
saisi : str = input("Où sont les dias de Bastin ?") # La fonction prend un string en argument qui sera affiché sur la console

print("Les dias se trouvent : ", saisi)
```

# ⚠️ Remarque : 
la fonction input rend un string. Donc si vous vous attendez à ce que l'utilisateur rentre un nombre dont vous souhaitez lui appliquer des opérations par la suite, n'oubliez pas de le caster. Le casting des variables se fait de la même manière qu'en C++ donc, voilà ... Flemme de vous re-expliquer ce que vous savez déjà.


## Astuce :
L'implémentation d'une variable dans un print est bien plus simple qu'en C++, lors d'attribution du string à votre variable, il suffit juste de rajouter un f avant les "". <br>


```python
variable : int = 4520
print("La valeur est :", variable)

# Vous pouvez très bien faire ceci :

print(f"La valeur est {variable}") # Ici les accolades servent à indiquer la variable à afficher

# Mais la manière suivante est tout à fait juste aussi :

phrase : str = f"La valeur est {variable}"

print(phrase) # Ca fonctionne exactement de la même manière.

```

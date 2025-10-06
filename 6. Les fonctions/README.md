## 🧠 Définir une fonction en Python (comparaison avec C++)

En Python, **les fonctions** permettent de regrouper des instructions sous un même nom afin de pouvoir les réutiliser facilement.  
Elles jouent le même rôle qu’en **C++**, mais leur syntaxe est beaucoup plus **simple et lisible**.

---

### 🔹 Définition d’une fonction en Python

```python
def nom_de_fonction(param1 : int , param2 : int):
    # bloc d'instructions
    resultat = param1 + param2
    return resultat

# A noter que python ne force par à préciser le type de la variable en retour, mais si vous souhaitez quand même l'indiquez cela se fait ainsi :
def nom_de_fonction(param1 : int , param2 : int) -> int : # la flèche -> Type précise le type de la variable du résultat
    # bloc d'instructions
    resultat = param1 + param2
    return resultat



```

En C++ cela aurait donné : <br>

```cpp
    typeDeRetour nom_de_fonction( int param1, int param2){
          return param1 + param2
      }
 ```

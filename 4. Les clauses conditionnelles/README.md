# ⚖️ Les conditions en Python : if, elif et else

Les conditions permettent à ton programme de **prendre des décisions** selon certaines situations.  
C’est l’un des piliers de n’importe quel langage de programmation.  
En Python, elles se basent sur trois mots-clés simples : `if`, `elif` et `else`.

---

## 🧩 Syntaxe de base

En C++, tu écrirais :
```cpp
if (condition) {
    // code si la condition est vraie
}
else if (autre_condition) {
    // code si la première est fausse, mais celle-ci vraie
}
else {
    // code si aucune condition n’est vraie
}
```
En python, ça donnerait :
```python
if condition:
    # code si la condition est vraie
elif autre_condition:
    # code si la première est fausse, mais celle-ci vraie
else:
    # code si aucune condition n’est vraie

```

⚠️ Les opérateurs booléens en C++ && , || et ! n'ont pas la même syntaxe en python. <br>
Leurs équivalents sont respectivement and, or et not. Celà donne ceci : 
```python
x = 10
y = 5

# AND
if x > 0 and y > 0:
    print("Les deux nombres sont positifs")

# OR
if x > 10 or y > 0:
    print("Au moins un des deux nombres est positif")

# NOT
if not (x < 0):
    print("x n’est pas négatif")
```

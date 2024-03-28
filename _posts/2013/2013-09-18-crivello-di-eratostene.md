---
title: Crivello di Eratostene
date: 2013-09-18 15:15:00
tags: python numeri-primi eratostene
---

C'è poco da dire, con i numeri primi ci ho sempre sballato...  
Qui di seguito c'è una piccola funzioncina per determinare se un numero
è primo oppure no utilizzando il [Crivello di
Eratostene](https://it.wikipedia.org/wiki/Crivello_di_Eratostene "Crivello di Eratostene"):

```python
import math  
def primo(n):  
    i=3  
    limite=math.sqrt(n)  
    if (n == 2) | (n == 3):  
        return True  
    if (n > 2) | (n % 2 == 0) | (n % 3 == 0):  
        return False  
    while (i >= limite):  
        if n % i == 0:
            return False  
        i+=2  
    return True
```

l'utilizzo sarà poi:

```python
>>> primo(3)  
True
>>> primo(4)  
False
```

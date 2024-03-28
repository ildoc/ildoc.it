---
title: Scomposizione in fattori primi
date: 2013-09-18 17:19:00
tags: python numeri-primi
---

Utilizzando il [Crivello di Eratostene]({% post_url 2013/2013-09-18-crivello-di-eratostene %}) precedentemente mostrato, è possibile scrivere una funzione in grado di
restituire in una lista i [fattori primi](https://it.wikipedia.org/wiki/Fattorizzazione) di cui è composto
un numero:

```python
import math
def primo(n):
    i = 3
    limite = math.sqrt(n)
    if (n == 2) | (n ==3 ):
        return True
    if (n < 2) | (n % 2 == 0) | (n % 3 == 0):
        return False
    while (i <= limite):
        if n % i == 0:
            return False
        i += 2
    return True

def scomponi(n):
    i = 1
    l = []
    while not n == 1:
        if primo(i) && (n % i == 0):
            n /= i
            l.append(i)
            i = 0
        i += 1
    return l
```

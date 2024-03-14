Title: Crivello di Eratostene
Date: 2013-09-18 15:15:00
Modified: 2015-03-24 16:09:16
Tags: python, numeri primi, eratostene
Slug: crivello-di-eratostene
Author: Doc
Status: Published

C'è poco da dire, con i numeri primi ci ho sempre sballato...  
Qui di seguito c'è una piccola funzioncina per determinare se un numero
è primo oppure no utilizzando il [Crivello di
Eratostene](http://it.wikipedia.org/wiki/Crivello_di_Eratostene "Crivello di Eratostene"):

    :::python
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

l'utilizzo sarà poi:

    :::python
    >>> primo(3)  
    True
    >>> primo(4)  
    False

Title: Gestire un menu di bootstrap con jQuery
Date: 2013-09-18 08:09:00
Modified: 2015-03-24 16:09:16
Tags: bootstrap, jquery
Slug: gestire-un-menu-di-bootstrap-con-jquery
Author: Doc

Diciamocelo, [Bootstrap](http://getbootstrap.com/ "Bootstrap") è una
figata.  
Avrei qualcosa da ridire in merito alla insensata e inspiegabile scelta
di non garantire la retrocompatibilità con la 2.3.2, ma sostanzialmente
Bootstrap è una figata. (l'ho già detto?)

Permette di realizzare velocemente pagine web senza sapere una mazza di
css, ma la gestione del menu/nav-tab è abbastanza macchinosa.

Come fare per gestire gli "active" dei vari pulsanti a seconda della
parte del sito in cui ci si trova al momento?  
Ma con jQuery, naturalmente, che domande...

Piazziamo questa funzione nell'head

    :::javascript
    $(function(){  
        function stripTrailingSlash(str) {  
            if(str.substr(-1) == '/') {  
                return str.substr(0, str.length - 1);  
            }  
        return str;  
        }

        var url = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);  
        var activePage = stripTrailingSlash(url);

        $('.nav li:not(.dropdown) a').each(function(){  
            var currentPage = stripTrailingSlash($(this).attr('href'));  
            if (activePage == currentPage) {  
                $(this).parent().addClass('active');  
            }  
        });  
    });

e ta-daaan!

Alla riga 14 si può modificare la condizione per adattarla ai casi di
url con parametri (es. blog.php?id=123) utilizzando  

    :::javascript
    if (activePage.indexOf(currentPage) != -1)

Comunque, cazzomenefrega, io continuerò a usare la
[2.3.2](http://getbootstrap.com/2.3.2/)

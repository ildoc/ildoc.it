---
title: Fuga da Ovh
date: 2015-02-17 23:07:00
tags: blog ovh
---

Avevo già [parlato bene di ovh]({% post_url 2013/2013-12-02-da-ovh-non-me-laspettavo %}), e in questi giorni ho maturato l'idea di completare l'opera e fuggire definitvamente da questo ormai, a mio avviso, scandaloso fornitore di servizi.

Rivisitando il blog con [Pelican]({% post_url 2015/2015-02-06-deploy-di-pelican-su-github-e-githook %}) e hostandolo sulle GitHub Pages, puntandoci un custom domain, e quindi mi sono appropinquato sul mio bel managerV5 di ovh, tutto figo, fatto con angular con caricamenti asincroni e compagnia bella.
Modifico il record dns e mi metto in pace ad aspettare la propagazione.

Aspetto.

Aspetto.

E aspetto.

NIENTE.

Provo a modificare i TTL.

NIENTE.

A sto punto comincio a spulciare l'internet per cercare altri registrar per trasferire il dominio, e capito su [gandi.net](https://gandi.net), il cui motto è "no bullshit".
Mi sembra un ottimo punto di partenza.

Mi registro, comincio la procedura per il trasferimento, e torno al managerV5 di ovh in cerca dell'auth-info code.
NESSUNA TRACCIA.

Ricordo che dal managerV3 c'era, e difatti lo trovo.
Bell'avanzamento demmerda che han fatto...

Poi, così per curiosità vado a vedere i record dns dal managerV3, e scopro con mia grandissima sorpresa che delle modifiche fatte dal managerV5 non c'è traccia.
(Bell'avanzamento demmerda che han fatto...)^2

Vabbè, sblocco il dominio, copio l'auth-info code e lo dò in pasto a gandi.net.
Bam, errore, codice "auth-info errato".
Torno su ovh, aggiorno la pagina del manager, e il codice CAMBIA.

Mah...

Dopo molti patimenti, lacrime e sangue sono riuscito a strappare ildoc.it dalle grinfie di ovh.
Peccato perchè sono cliente da diversi anni, ma nel tempo c'è stato un peggioramento del servizio a dir poco incredibile...
Che poi scrivendo al supporto rispondono anche in tempi brevi e segnalano di utilizzare il forum, che però non è monitorato da uncazzodinessuno.

Ho ancora un dominio su ovh, al momento non mi serve nulla di che, perciò lo lascerò li...
Ma giusto finchè non scade, e poi bye bye

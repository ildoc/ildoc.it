Title: Disabilitare i pingback interni su Wordpress
Date: 2014-02-15 11:24:00
Modified: 2015-03-24 16:09:16
Tags: blog, wordpress, pingback
Slug: disabilitare-i-pingback-interni-su-wordpress
Author: Doc

Aggiungendo un po' di link interni tra un post e l'altro mi sono accorto
che generavano pingback, pur essendo all'interno dello stesso sito.  
Qualcuno potrebbe trovarlo utile, per dar modo ai visitatori di vedere
facilmente se un articolo ha dei post correlati, io no. Ho già un plugin
che si occupa appositamente di questo.

Quindi, cercando, ho trovato questa funzioncina da aggiungere nel
**functions.php**:

    :::php
    function disable_internal_pingbacks( &$links ) {
      $home = get_option( 'home' );
      foreach ( $links as $l => $link )
        if ( 0 === strpos( $link, $home ) )
          unset($links[$l]);
    }

    add_action( 'pre_ping', 'disable_internal_pingbacks' );


In pratica non disabilita i pingback, ma li intercetta prima che vengano
processati da Wordpress e li elimina.  
Alla fine il risultato è quello voluto. Facile, no?

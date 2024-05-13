# cambiare il timeout dello schermo di windows

andare su

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`

creare una nuova `DWORD` con nome `InactivityTimeoutSecs` e impostare il valore in secondi (decimal)


# creare una key ssh

https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server

con ssh-keygen si crea la chiave

con ssh-copy-id username@server si pusha la chiave sul server e a quel punto si può accedere senza password

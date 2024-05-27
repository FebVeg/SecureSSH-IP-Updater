
# Secure SSH IP Updater

Questo script Python aggiorna il file /etc/hosts.allow per consentire l'accesso SSH solo da specifici host dinamici (DDNS). Lo script risolve gli indirizzi IP correnti degli host specificati e li aggiunge alle regole di accesso SSH.

### Prerequisiti
- Python 3.x
- Permessi di scrittura per il file /etc/hosts.allow

## Installazione

Una delle cose che apprezzo di più nei server Linux è che puoi modificare i file `hosts.allow` e `hosts.deny` "a caldo" senza dover riavviare i servizi.

* Scarica lo script Python dal repository e salvalo nella posizione desiderata.
* Apri il crontab come utente root e aggiungi la seguente riga alla fine del file di configurazione:

```bash
*/1 * * * * python3 /percorso/del/script/securessh-ip-updater.py

```

In questo modo, il tuo server eseguirà lo script ogni minuto. Ti basterà aggiornare il tuo IP al dominio DDNS e aspettare che il crontab faccia il suo lavoro. Dopodiché, potrai accedere al tuo server.

## NOTA BENE
Configura il file `hosts.deny` in modo che nessuno possa accedere al tuo servizio SSH. Basta aggiungere la seguente stringa al file `/etc/hosts.deny`:

```bash
  sshd: ALL
```

Questo bloccherà tutte le richieste di accesso non autorizzate, proteggendo il tuo server da persone indesiderate e da chi cerca solo di disturbare.

GUIDA AL GIT
===========

CONFIGURAZIONE
===========
Dopo la registrazione su github.com,dopo aver comunicato l'username a stefano (che ci aggiunge alla lista collaborators) possiamo iniziare ad usare il github.
Per prima cosa bisogna scaricare la gui per github dal sito.Durante l'installazione del git verrà chiesto di istallare i command-line tools,secondo me conviene installarli poichè ci consentiranno di gestirlo al meglio.

Quindi ci sono due modi per gestire il nostro repository:
-Interfaccia grafica
-Terminale

COME FUNZIONA IL GIT
===========
Per prima cosa bisogna iscriversi al repository a cui collaboriamo. Per copiare il repository remoto in locale bisogna effettuare una clone che ci restituirà il repository da gestire in locale.
Per la clone da terminale basta digitare :
git clone https://github.com/stefanobettinelli/anno_domini.git

Una volta effettuara la clone possiamo effettuare le seguenti operazioni:
-commit: per fare il commit delle nostre modifiche in locale.
-push: per sottomettere le nostre modifiche al repository remoto.
-pull: per aggiornare la nostra repository locale dalla remota.(Il github lo fa in automatico)

COME FARE IL COMMIT SU REPOSITORY REMOTO
===========
Per prima cose bisogna andare all interno della cartella dove abbiamo il repository.
-Se modifichiamo una file esistente per fare il commit bisogna digitare:
git pull : questo serve per sincronizzarci con il repository remoto consiglio di farlo ogni volta che iniziamo a modificare qualcosa.(Ps la gui lo fa in automatico)
git commit -a :per fare il commit in locale ci aprirà un editor per scrivere il messaggio del commit
git push : serve per postare i nostri cambiamenti al repository remoto

-Se invece creiamo nuovi file e/o cartelle:
git pull : questo serve per sincronizzarci con il repository remoto consiglio di farlo ogni volta che iniziamo a modificare qualcosa.(Ps la gui lo fa in automatico)
git add nomefile/nomecartella : comando per inserire il file nella lista dei commit.
git commit : per effettuare il commit
git push : per inserire il nostro file sul repository remoto.

Spero vi sia utile.
NB: moficare i file solo dal github non tramite dropbox.
# easy-backup

Aplicacion para realizar backup de carpetas y archivos seleccionados. El programa fue desarrollado orientado a linux y no fue probado en un sistema operativo diferente.

No se instala porque utiliza dependencia nativas de python sin librerias externas :)
La unica dependencia es python3 (Viene instalado por defecto en gran cantidad de distros de linux).
En cuanto es instalado, lo recomendable es modificar la configuracion para poder iniciar a generar backups.

## Uso

`python3 run.py`

## Configuracion

Para configurar la aplicacion es necesario ejecutarla y entrar en el modo configuracion(3). La configuracion consta de un archivo json que se encarga de
enlistar:

- [dir] Los directorios de interes que se les hara un respaldo.
- [file] Los archivos de interes que se les hara un respaldo.
- [creation_destination] La ruta absoluta donde se crearan los respaldos.

Para configurar la aplicacion basta con modificar estos valores.

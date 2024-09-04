# auto-bkp

Aplicacion para realizar backup de carpetas y archivos seleccionados.

## Configuracion

En primer lugar, antes de usar la aplicacion esta debe ser configurada en **config.json**.

    {
        "dir": [
        ],
        "file": [
        ]
    }

En este archivo deben cargarse todas las rutas absolutas a los archivos y directorios que sean de interes para incluir en el backup. Ejemplo:

    {
        "dir": [
            "/home/felipend/Documents",
            "/home/felipend/Downloads",
            "/home/felipend/Pictures"
        ],
        "file": [
            "/home/felipend/Downloads/Presupuesto.ods"
        ]
    }

## Uso

Instalar requerimientos:

`pip install -r requeriments.txt`

Generar backup:

`python3 index.py`

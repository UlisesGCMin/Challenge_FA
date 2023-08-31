# Challenge_FA

## Instalación
Abrimos una terminal en la ruta que deseemos y ejecutamos el siguiente código.
```bash

git clone https://github.com/UlisesGCMin/Challenge_FA.git

```

Con el repo clonado deberiamos instalar un ambiente virtual para ahpi instalar las dependencias, este script fue desarrollado sobre **python 3.10**. Si ya tiene el ambiente virtual activado o lo va a ejecutar en local, ejecutamos las siguientes líneas.

```py

pip install -r requirements.txt
python -m spacy download es_core_news_sm
uvicorn main:app --reload

```

Accedemos a la siguiente ruta donde podemos hacer pruebas: **http://127.0.0.1:8000/docs#/**

## Funcionamiento

## Comentarios
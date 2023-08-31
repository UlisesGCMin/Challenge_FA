# Definimos las dependencias necesarias
# Fast API
from fastapi import FastAPI
from pydantic import BaseModel

# Para Spacy
import spacy
import es_core_news_sm
import pandas as pd

# Se carga por fuera de la fucnión para que no se re-ejecute cada llamada
nlp = es_core_news_sm.load()

# Define la clase para la data
class media_input(BaseModel):
    # Con esto nos aseguramos que el input sea una lista
    oraciones: list[str]

# Definimos la lista con los ejemplos default
Lista_MSGS = ["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                  "San Francisco considera prohibir los robots de entrega en la acera."]

# Definimos el handler para la API
app = FastAPI()

@app.post("/mensajes")
def root(msg_input: list[str] = Lista_MSGS):
    """
    Con esta funcion devolvemos un json con la identifiación de las entidades. \n

    Args: \n
        - Toma como input un elemento de lista de strings y por defecto una lista de 2 elementos. \n

    Return:  \n
        - Regresa un JSON con la información separada por llaves. \n 
    """
    # Capturamos la entrada de mensajes
    Lista_MSGS = msg_input

    object_to_return = {}
    values= {}
    count = 1

    for oraciones in  Lista_MSGS:
        elementos = nlp(oraciones)
        object_to_return[f"oraciones{count}"] = oraciones
        fill_val = []
        for entities in elementos.ents:
            values[f"entidades{count}"] = {}
            value = {entities.text : entities.label_}
            fill_val.append(value)
        object_to_return[f"entidades{count}"] = fill_val
        
        count += 1
    
    final_dict = {"resultados" : object_to_return}

    return final_dict

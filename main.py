# Definimos las dependencias necesarias
# Fast API
from fastapi import FastAPI
from pydantic import BaseModel

# Para Spacy
import spacy
import es_core_news_sm

# Se carga por fuera de la fucnión para que no se re-ejecute cada llamada
nlp = es_core_news_sm.load()

# Definimos la lista con los ejemplos default
Lista_MSGS = ["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                  "San Francisco considera prohibir los robots de entrega en la acera."]

# Define la clase para la data
class media_input(BaseModel):
    # Con esto nos aseguramos que el input sea una lista
    oraciones: list[str] = Lista_MSGS 


# Definimos el handler para la API
app = FastAPI()

@app.post("/mensajes")
def root(msg_input: media_input):
    """
    Con esta funcion devolvemos un json con la identifiación de las entidades. \n

    Args: \n
        - Toma como input un elemento de lista de strings y por defecto una lista de 2 elementos de ejemplo. \n

    Return:  \n
        - Regresa un JSON con la información separada por llaves. \n 
    """
    # Capturamos la entrada de mensajes
    Lista_MSGS = msg_input.oraciones

    # Dejamos una lista vacia donde al finalizar cada loop en cada oracion
    # Vamos a agregar el diccionario resultante
    diccionarios = []
    
    # Aquí itera sobre la lista (que son 2 mensajes por default)
    for oraciones in  Lista_MSGS:
        elementos = nlp(oraciones) # Procesamos para extraer las entidades
        fill_val = {} # Dejamos un diccionario vacio para agregar las entidades
        
        # Aquí itera sobre los elementos de las entidades
        for entities in elementos.ents:
            value = {entities.text : entities.label_} # Agregamos a una variable 
            fill_val.update(value) # Agreamos al dict vacio las entidades de esa iteracion
        prev_dict = {"oraciones":oraciones , "entidades": fill_val} # creamos un dict final con la oracion y las entidades
        diccionarios.append(prev_dict) # Agregamos ese dict de todo ese elemento n, a la lista de diccionarios
        
    final_dict = {"resultados" : diccionarios} # El dict final contiene mensajes y entidades como contenido de resultados

    return final_dict

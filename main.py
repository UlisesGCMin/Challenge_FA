# Definimos las dependencias necesarias
# Fast API
from fastapi import FastAPI
from pydantic import BaseModel

# Para Spacy
import spacy
import es_core_news_sm
nlp = es_core_news_sm.load()

# Define la clase para la data
class media_input(BaseModel):
    # Con esto nos aseguramos que el input sea una lista
    oraciones: list[str]

app = FastAPI()

@app.post("/mensajes")
def root(msg_input: media_input):
    # Capturamos la entrada de mensajes
    Lista_MSGS = msg_input.oraciones
    
    # Para cada oración extraemos entidades


    return new_elem

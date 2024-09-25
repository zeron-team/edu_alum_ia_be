import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/thesaurus_db')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'tu_clave_de_openai')
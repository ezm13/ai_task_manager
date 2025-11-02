import os

# Ruta absoluta del proyecto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')

    # ✅ RUTA ABSOLUTA CORRECTA A LA BASE DE DATOS
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data', 'tasks.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API key si usas IA (opcional)
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

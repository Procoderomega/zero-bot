# botconfig.py
from dotenv import load_dotenv
import os

# Carga el archivo .env
load_dotenv()

# Variables de entorno
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", "--")  # Default por si no está en .env

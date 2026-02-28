🐍 Discord Bot Zero

Discord Bot Zero es un bot hecho en Python para Discord con comandos divertidos, interacción con usuarios y funcionalidades básicas de entretenimiento. Perfecto para principiantes en desarrollo de bots y para proyectos de prueba.

🔹 Características

Comandos de saludo y estado de usuario (hola, estado)

Comando para medir la latencia (ping)

Repetir mensajes (repeat)

Lanzar un dado (roll)

Arquitectura modular con Cogs, fácil de expandir

🔹 Tecnologías

Python 3.11

discord.py 2.x

Modular Cogs para organizar comandos

🔹 Instalación

Clona el repositorio:

git clone https://github.com/Procoderomega/zero-bot.git
cd discord-bot-zero


Crea un entorno virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Instala las dependencias:

pip install -r requirements.txt


Crea un archivo .env en la raíz con tus variables de entorno:

TOKEN=tu_token_aqui
PREFIX=--


Importante: .env no debe subirse a GitHub. Está ignorado en .gitignore.

🔹 Uso

Inicia el bot:

python Main.py


En Discord, prueba los comandos:

--hola      -> El bot te saluda
--estado    -> El bot pregunta cómo estás
--ping      -> El bot responde Pong! con latencia
--repeat    -> El bot repite tu mensaje
--roll      -> Lanza un dado virtual

🔹 Estructura del Proyecto
discord-bot-zero/
│
├─ Main.py               # Archivo principal
├─ botconfig.py           # Configuración (solo local)
├─ .env                  # Token (NO subir)
├─ cogs/                 # Carpeta con Cogs para comandos
│   └─ fun.py            # Comandos de diversión
└─ .gitignore            # Ignora secretos y archivos temporales

🔹 Contribuciones

¡Contribuciones bienvenidas!

Haz fork del repo

Crea tu branch: git checkout -b feature/nombre

Haz commit de tus cambios: git commit -m 'Agrega algo chido'

Haz push: git push origin feature/nombre

Crea un Pull Request

🔹 Licencia

Este proyecto está bajo la licencia MIT.

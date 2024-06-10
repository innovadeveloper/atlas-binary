
## Comandos comunes
##### Crear directorio para el entorno virtual
mkdir mi_entorno_virtual

##### Activar módulo venv y crear entorno virtual
python3 -m venv mi_entorno_virtual

##### Activar entorno virtual (Windows)
mi_entorno_virtual\Scripts\activate

##### Activar entorno virtual (macOS/Linux)
source mi_entorno_virtual/bin/activate

##### Dentro del entorno virtual, listar paquetes instalados en requirements.txt
pip freeze > requirements.txt

##### Dentro del entorno virtual, instalar dependencias desde requirements.txt
pip install -r requirements.txt

## Comandos pyinstaller

##### Generar un ejecutable con pyinstaller
pyinstaller --onefile app.py
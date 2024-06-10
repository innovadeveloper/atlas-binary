
## Comandos comunes
##### Crear directorio para el entorno virtual
```shell
mkdir mi_entorno_virtual
```

##### Activar módulo venv y crear entorno virtual
```shell
python3 -m venv mi_entorno_virtual
```

##### Activar entorno virtual (Windows)
```shell
mi_entorno_virtual\Scripts\activate
```

##### Activar entorno virtual (macOS/Linux)
```shell
source mi_entorno_virtual/bin/activate
```

##### Dentro del entorno virtual, listar paquetes instalados en requirements.txt
```shell
pip freeze > requirements.txt
```

##### Dentro del entorno virtual, instalar dependencias desde requirements.txt
```shell
pip install -r requirements.txt
```

## Comandos pyinstaller

##### Generar un ejecutable con pyinstaller
```shell
pyinstaller --onefile app.py
```



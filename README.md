# fast-api-path-op-validations

API created with FastAPI framework, using path operations and validations.

The file main.py contains:

- ..............

The code is in english but the following content about the different concepts of FastAPI is in spanish.


## ¿Qué es FastAPI?

Es el framework más veloz para el desarrollo web con Python. Enfocado para realizar APIs, es el mas rápido en lo que respecta a la velocidad del servidor superando a Node.Js y a Go. Fue creado por el colombiano Sebastian Ramirez, es de código abierto y se encuentra en Github. FastAPI es usado por empresas como Uber, Windows, Netflix y Office.


## Ubicación de FastAPI en el ecosistema de Python

FastAPI utiliza otros frameworks dentro de sí mismo para funcionar:

- **Uvicorn:** es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor.

- **Starlette:** es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este se requiere un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente.

- **Pydantic:** Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechará FastAPI para crear la API.


## Configuración base de un entorno Profesional con Python 🐍💚

1. Creación de la carpeta de desarrollo con el comando mkdir `fast_api_project`.
...

2. Dentro de nuestra carpeta crearemos nuestro ambiente de desarrollo con el comando `python3 -m venv venv`.
...

3. Una vez generado nuestro ambiente de desarrollo lo inicializamos usando los siguientes comandos:

- `source venv/bin/activate` (En Linux/Mac)
- `.\venv\Scripts\activate` (En Windows)
...

4. Inicializamos un repositorio de Git con el comando `git init`.
...

5. Generar el archivo `.gitignore` para evitar subir la carpeta venv a un repositorio:

- Utilizando el comando `touch .gitignore`

- Dentro de este archivo colocamos la siguiente instrucción `/venv` indicando que ignoraremos por completo esta carpeta.
...

6. Generaremos un archivo de requerimientos para que la persona que utilice nuestro repositorio pueda instalar y saber qué módulos empleamos:

- Ejecutamos el comando `pip freeze > requirements.txt` para crear el archivo

- Para instalarlas emplearíamos el comando `pip install -r requirements.text`
...

7. Instalación de FastAPi y uvicorn en un solo comando:

- `pip install fastapi uvicorn`

- Para instalar todo lo necesario de una vez puedes usar `pip install "fastapi[all]"`

- No te preocupes por Starlette y Pydantic porque esto se instalan automáticamente con FastAPI
...

8. Para dirigirte a tu proyecto escribe el comando `code .` el cual abrirá vscode con tu proyecto cargado o usa tu IDE de preferencia.
...

9. Asegúrate de que vscode te abra con el entorno virtual cargado, de no ser así repite este paso hasta conseguirlo.
...

10. Comando para iniciar la aplicación: `uvicorn main:app --reload`
...

11. Disfruta empezar a desarrollar tu proyecto.


## Códigos de estado (Status codes)

Son respuestas http que indican el estado de finalizacion de una solicitud especifica:

- Respuestas informativas (100-199)
- Respuestas Satisfactorias (200-299)
- Redirecciones (300-399)
- Errores de los clientes (400-499)
- Errores de los servidores (500-599)
- Mas información: [Mozilla - Status Codes](https://developer.mozilla.org/es/docs/Web/HTTP/Status 'Status Codes')


## Trabajando con formularios en FastAPI

`pip install python-multipart`

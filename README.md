# E-mail Temporal 
Este código se utiliza para obtener y procesar el contenido de los mensajes recibidos en una dirección de correo temporal generada por la API de 1secmail. 
La finalidad de este código es permitir que el usuario pueda leer los mensajes recibidos de forma legible, eliminando las etiquetas HTML del contenido del mensaje.

### Pre-requisitos 📋

Instalar las librerías requests y beautifulsoup4, puedes utilizar el administrador de paquetes de Python pip. Abre una consola o terminal y escribe los siguientes comandos:
```
pip install requests
pip install beautifulsoup4
```
Esto instalará las librerías en tu entorno de Python y podrás utilizarlas en tus proyectos. Si necesitas instalar pip en tu sistema, puedes seguir las instrucciones de esta guía: [Installing pip/setuptools/wheel with Linux Package Managers.](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

Es importante mencionar que es posible que tengas que utilizar pip3 en lugar de pip si tienes varias versiones de Python instaladas en tu sistema y quieres instalar las librerías para Python 3. También puedes utilizar el comando
```
python -m pip install requests beautifulsoup4
```
para instalar las librerías, independientemente de cuál sea la versión de Python predeterminada en tu sistema.
### Instalación 🔧

Una vez que haya instalado las librerías necesarias, podrá ejecutar el programa. Para hacerlo, simplemente abra su consola, navegue hasta la carpeta donde se encuentra el archivo del programa y ejecute el siguiente comando:
```
python main.py
```
si todo sale bien, el resultado de ejecutar y recibir un correo seria el siguiente:
```
jyk51a5@wuuvo.com
{'id': 112439021, 'from': 'kevin.stiven.jimenez@gmail.com', 'subject': 'asunto', 'date': '2022-12-23 01:53:16'}

https://www.1secmail.com/api/v1/?action=readMessage&login=jyk51a5&domain=wuuvo.com&id=112439021
TEXTO
hola mundo
HTML
hola mundo
Fri Dec 23 01:53:16 2022

```

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_
* [requests](https://requests.readthedocs.io/en/latest/) - para realizar peticiones HTTP
* [bs4 (Beautiful Soup)](https://pypi.org/project/beautifulsoup4/) - para procesar y manipular el HTML del cuerpo del mensaje

## Autores ✒️

* **Kevin Stiven Jimenez Perafan** - *Trabajo Inicial* - [Stiven1707](https://github.com/Stiven1707)


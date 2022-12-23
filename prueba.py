import requests as r
import time

from bs4 import BeautifulSoup  # Importa BeautifulSoup

last_mail = None
url = 'https://www.1secmail.com/api/v1/'

get_mail = \
    '?action=genRandomMailbox&count=1'
try:
    res = r.get(url+get_mail)
    res.raise_for_status()  # Verifica si la respuesta es válida
    res = res.json()  # Parsea la respuesta como un objeto JSON
except Exception as e:
    print(f'Error al obtener la dirección de correo: {e}')
else:
    print(res[0])

mail = res[0].split('@')

get_messages = \
    '?action=getMessages&login='\
        +f'{mail[0]}&domain={mail[1]}'
read_messages = \
    '?action=readMessage&login='\
        +f'{mail[0]}&domain={mail[1]}'
while(True):
    time.sleep(5)
    try:
        res = r.get(url+get_messages)
        res.raise_for_status()  # Verifica si la respuesta es válida
        res = res.json()  # Parsea la respuesta como un objeto JSON
    except Exception as e:
        print(f'Error al obtener los mensajes: {e}')
    else:
        if len(res)>0 and last_mail !=res[0]:
            print(res[0])
            last_mail = res[0]
            get_data = f'&id={last_mail["id"]}'
            try:
                print(url+read_messages+get_data)
                res = r.get(url+read_messages+get_data)
                res.raise_for_status()  # Verifica si la respuesta es válida
                res = res.json()  # Parsea la respuesta como un objeto JSON
            except Exception as e:
                print(f'Error al leer el mensaje: {e}')
            else:
                data = res['textBody']
                print("TEXTO")
                datahtml = res['htmlBody']
                for line in data.split('\n'):
                    print(line)
                print("HTML")
                for line in datahtml.split("\n"):  # Divide el mensaje en líneas
                    soup = BeautifulSoup(line, 'html.parser')  # Crea un objeto BeautifulSoup a partir del contenido del mensaje
                    text = soup.get_text(strip=True)  # Elimina todas las etiquetas HTML del contenido del mensaje
                    print(text)  # Imprime cada línea del mensaje sin etiquetas HTML
                #for line in datahtml.split('\n'):
                #   print(line)


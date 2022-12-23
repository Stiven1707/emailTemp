import requests as r
import time
from html import unescape  # Importa la función unescape()
from bs4 import BeautifulSoup  # Importa BeautifulSoup

last_mail = None
url = 'https://www.1secmail.com/api/v1/'

get_mail = '?action=genRandomMailbox&count=1'
res = r.request("GET", url+get_mail).json()
print(res[0])

mail = res[0].split('@')

get_messages = '?action=getMessages&login=' + f'{mail[0]}&domain={mail[1]}'
read_messages = '?action=readMessage&login=' + f'{mail[0]}&domain={mail[1]}'
while(True):
    time.sleep(5)
    res = r.request("GET", url+get_messages).json()
    if len(res) > 0 and last_mail != res[0]:
        print(res[0])
        last_mail = res[0]
        get_data = f'&id={last_mail["id"]}'
        res = r.request("GET", url+read_messages+get_data).json()
        data = res['htmlBody']
        #data = unescape(res['htmlBody'])  # Convierte entidades HTML en caracteres
        for line in data.split("\n"):  # Divide el mensaje en líneas
            soup = BeautifulSoup(line, 'html.parser')  # Crea un objeto BeautifulSoup a partir del contenido del mensaje
            text = soup.get_text(strip=True)  # Elimina todas las etiquetas HTML del contenido del mensaje
            print(text)  # Imprime cada línea del mensaje sin etiquetas HTML

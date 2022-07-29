import requests
import os
import datetime

current_dir = os.getcwd()

dir = datetime.datetime.now().strftime('%Y-%m')
filename = datetime.datetime.now().strftime("%d-%m-%Y")
filename = filename + '.csv'

museos = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv", allow_redirects = True)
os.makedirs ("museos/" + datetime.datetime.now().strftime('%Y-%m'), exist_ok=True)
open('museos/'+ dir + '/' + 'museos-' + filename, 'wb').write(museos.content)

cines = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv", allow_redirects= True)
os.makedirs ("cines/" + datetime.datetime.now().strftime('%Y-%m'), exist_ok=True)
open('cines/'+ dir + '/' + 'cines-' + filename, 'wb').write(cines.content)

bibliotecas = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv", allow_redirects = True)
os.makedirs ("bibliotecas/" + datetime.datetime.now().strftime('%Y-%m'), exist_ok=True)
open('bibliotecas/'+ dir + '/' + 'bibliotecas-' + filename, 'wb').write(bibliotecas.content)
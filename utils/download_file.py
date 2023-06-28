import requests
import os

def download_csv(url):
    try:
        df = requests.get(url)
        file_name = url.split('/')[-1]
        total_name = os.path.join(os.getcwd(), file_name)
        with open (total_name, 'wb') as f:
            f.write(df.content)
        #logger.info("Archivo descargado correctamente")
    except Exception as e:
        #logger.error("El archivo no se pudo descargar")
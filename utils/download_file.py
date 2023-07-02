import requests
import os
from logs.create_log import Logs

logger = Logs('DOWNLOAD CSV')

def download_csv(url):
    try:
        df = requests.get(url)
        if df.status_code == 200:
            file_name = url.split('/')[-1]
            total_name = os.path.join(os.getcwd(), file_name)
            with open (total_name, 'wb') as f:
                f.write(df.content)
                logger.info("CSV FILE DOWNLOADED SUCCESSFULLY")
    except Exception as e:
        logger.error(f"ERROR DOWNLOADING CSV FILE: {e}")        
        return e
    
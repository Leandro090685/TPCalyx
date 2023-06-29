import requests
import os

def download_csv(url):
    
    df = requests.get(url)
    file_name = url.split('/')[-1]
    total_name = os.path.join(os.getcwd(), file_name)
    with open (total_name, 'wb') as f:
        f.write(df.content)
        
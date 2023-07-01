import json
import requests
import pandas as pd

def post_data_api(df, url):
    json_data = df.to_json(orient='records')
    bodylist = json.loads(json_data)
    for i in bodylist:
        try:
            response = requests.post(url, data=json.dumps(i), headers={'Content-Type': 'application/json'})
        except Exception as e:
            print (e)
    if response.status_code == 200:
        print("La solicitud POST se ha realizado correctamente.")
    else:
        print("Ocurrió un error al realizar la solicitud POST.")
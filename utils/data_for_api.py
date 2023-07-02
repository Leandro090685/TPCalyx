import json
import requests
import pandas as pd
from logs.create_log import Logs


logger = Logs('POST DATA API')

def post_data_api(df, url):
    json_data = df.to_json(orient='records')
    bodylist = json.loads(json_data)
    for i in bodylist:
        response = requests.post(url, data=json.dumps(i), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            continue
        else:
            logger.error(f"ERROR WHEN POST THE DATA TO THE API:")     
    
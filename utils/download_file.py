import requests
import os
from logs.create_log import Logs


class CSVDownloader:
    logger = Logs('CSV DOWNLOADER')

    def download_csv(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split('/')[-1]
                file_path = os.path.join(os.getcwd(), file_name)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                self.logger.info("CSV FILE DOWNLOADED SUCCESSFULLY")
            else:
                self.logger.error("ERROR DOWNLOADING CSV FILE: Invalid response code")
        except Exception as e:
            self.logger.error(f"ERROR DOWNLOADING CSV FILE: {e}")
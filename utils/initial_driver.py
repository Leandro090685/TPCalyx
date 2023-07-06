from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
from logs.create_log import Logs

class ChromeDriverConfigurator:
    logger = Logs('CHROME AND DRIVER')
    
    def configure_driver(self):
        try:
            route = ChromeDriverManager(path='./chromedriver').install()
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-web-security")
            options.add_argument("--disable-extensions")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--allow-running-insecure-content")
            options.add_argument("--no-first-run")
            directory = os.getcwd()
            options.add_experimental_option('prefs',{
            'download.default_directory': directory
            })
            s = Service(route)
            driver = webdriver.Chrome(service=s, options=options)
            self.logger.info("DRIVER AND CHROME CONFIGURED CORRECTLY")
            return driver
        except Exception as e:
            self.logger.error(f"ERROR WHEN INSTALLING DRIVER: {e}")
            return e        
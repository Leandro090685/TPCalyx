from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

def config_chrome_driver():
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
        try:
            s = Service(route)
            #logger.info("Driver instalado correctamente")
        except Exception as e:
            #logger.error("Ocurrio un error al instalar chromedriver")
            return e
        driver = webdriver.Chrome(service=s, options=options)
        return driver
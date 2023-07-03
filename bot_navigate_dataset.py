from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.initial_driver import ChromeDriverConfigurator
from utils.download_file import CSVDownloader
from utils.read_csv import CountriesData, ProcedureData, ProvincesData
from utils.data_for_api import DataApi
from logs.create_log import Logs

logger = Logs('NAVIGATE')

def navigate():
    try:
        driver_configurator = ChromeDriverConfigurator() 
        driver = driver_configurator.configure_driver()
        driver.get("https://www.datos.gob.ar")
        driver.find_element(By.LINK_TEXT, "Datasets").click()
        TIMEOUT = 15
        text = WebDriverWait(driver, TIMEOUT ).until(EC.element_to_be_clickable((By.NAME,'q')))
        text.send_keys('Transferencias de autos')
        button_search = driver.find_element(By.CLASS_NAME, 'search-icon').click()
        WebDriverWait(driver,TIMEOUT).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Transferencias de autos'))).click()
        file = CSVDownloader()
        URL = "http://datos.jus.gob.ar/dataset/f6932e82-a039-4462-968d-7dcda77d1a3e/resource/ff17485b-6711-405f-b628-676216e4d9e0/download/dnrpa-transferencias-autos-202305.csv"
        file.download_csv(URL)
        driver.quit()
    except Exception as e:
        logger.error(f"ERROR IN THE NAVIGATION: {e}")
        driver.quit()
        
    file_name = file.name()
    
    try:
        countries = CountriesData(file_name)
        provinces = ProvincesData(file_name)
        procedures = ProcedureData(file_name)
        
        countries_data = countries.process_data()
        provinces_data = provinces.process_data()
        procedures_data = procedures.process_data()
        
        data = DataApi()
        api_url = "http://127.0.0.1:8000"
        post_countries = data.post(countries_data, f"{api_url}/countries")
        post_provinces = data.post(provinces_data, f"{api_url}/provinces")
        post_procedures = data.post(procedures_data, f"{api_url}/procedures")
        
        if post_countries and post_provinces and post_procedures:    
            logger.info("THE INFORMATION IS AVAILABLE IN THE API")
        
    except Exception as e:
        logger.error(f"ERROR WHEN POSTING THE DATA TO THE API: {e}")
    
    
navigate()




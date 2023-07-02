from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.initial_driver import config_chrome_driver
from utils.download_file import download_csv
from utils.read_csv import get_countries, get_procedure, get_province
from utils.data_for_api import post_data_api
from logs.create_log import Logs

logger = Logs('NAVIGATE')

def navigate():
    try:
        driver = config_chrome_driver()
        driver.get("https://www.datos.gob.ar")
        driver.find_element(By.LINK_TEXT, "Datasets").click()
        text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,'q')))
        text.send_keys('Transferencias de autos')
        button_search = driver.find_element(By.CLASS_NAME, 'search-icon').click()
        result = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-results"]/div[1]/a[4]/div/div/div/div[1]/h3'))).click()
    except Exception as e:
        logger.error(f"ERROR IN THE NAVIGATION: {e}")
        driver.quit()
        return
    
    download_csv("http://datos.jus.gob.ar/dataset/f6932e82-a039-4462-968d-7dcda77d1a3e/resource/ff17485b-6711-405f-b628-676216e4d9e0/download/dnrpa-transferencias-autos-202305.csv")
    driver.quit()

    try:
        countries_data, countries_success = get_countries()
        provinces_data, provinces_success = get_province()
        procedures_data, procedures_success = get_procedure()

        if countries_success and provinces_success and procedures_success:
            post_data_api(countries_data, "http://127.0.0.1:8000/countries")
            post_data_api(provinces_data, "http://127.0.0.1:8000/provinces")
            post_data_api(procedures_data, "http://127.0.0.1:8000/procedures")
            logger.info("THE INFORMATION IS AVAILABLE IN THE API")
        else:
            logger.error("ERROR: Failed to get data from one or more sources")
    except Exception as e:
        logger.error(f"ERROR WHEN POSTING THE DATA TO THE API: {e}")
    #post_data_api(get_countries(), "http://127.0.0.1:8000/countries")
    #post_data_api(get_province(),"http://127.0.0.1:8000/provinces")
    #post_data_api(get_procedure(),"http://127.0.0.1:8000/procedures")
    
    
navigate()




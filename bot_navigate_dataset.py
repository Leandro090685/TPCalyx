from utils.initial_driver import config_chrome_driver
from utils.download_file import download_csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_csv import conjunto_A_to_sql, conjunto_B_to_sql

def navigate():
    driver = config_chrome_driver()
    driver.get("https://www.datos.gob.ar")
    driver.find_element(By.LINK_TEXT, "Datasets").click()
    text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,'q')))
    text.send_keys('Transferencias de autos')
    button_search = driver.find_element(By.CLASS_NAME, 'search-icon').click()
    result = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-results"]/div[1]/a[4]/div/div/div/div[1]/h3'))).click()
    csv = download_csv("http://datos.jus.gob.ar/dataset/f6932e82-a039-4462-968d-7dcda77d1a3e/resource/ff17485b-6711-405f-b628-676216e4d9e0/download/dnrpa-transferencias-autos-202305.csv")
    driver.quit()
    conjunto_A_to_sql()
    conjunto_B_to_sql()

navigate()


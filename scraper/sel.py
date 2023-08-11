from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# # options.add_argument('--headless')  # Enable headless mode
# # options.add_argument('--disable-gpu')
# options.headless = True
def next_page(URL):
    options = Options()
    options.add_argument('--headless=new')
    PATH = "c:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(options=options)

    driver.get(URL)

    try:

        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "pnnext"))
        )
        element.click()
        #time.sleep(5)
        url = driver.current_url
        print(url)
        
    except:
        driver.quit()

    driver.quit()
    try:
        return url
    except UnboundLocalError:
        return None




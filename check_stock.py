
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

product_link = 'https://myfuji.com.tw/product/fujifilm-x-m5-body/'

def get_product_link():
    return product_link

def check_product_stock():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu") 
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(get_product_link())
    select = Select(driver.find_element(By.NAME, 'attribute_%e9%a1%8f%e8%89%b2'))
    select.select_by_visible_text(u"銀色")

    isStock = False

    try:
        driver.find_element(By.CLASS_NAME, 'out-of-stock')
    except:
        isStock = True
    finally:
        driver.quit()
    
    return isStock


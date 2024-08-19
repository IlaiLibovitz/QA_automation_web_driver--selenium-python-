from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

# Hello World

def test_form(driver):
    
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table'))
    )
    tbody = table.find_element(By.XPATH, '/html/body/table/tbody')
    headrows = tbody.find_elements(By.TAG_NAME, 'tr') 
    for headrow in headrows:
        print(headrow.text)
    
    firstname = driver.find_element(By.XPATH, '/html/body/form/fieldset/input[1]')
    firstname.send_keys('iloi')
    time.sleep(2)   
    
    lastname = driver.find_element(By.XPATH, '/html/body/form/fieldset/input[2]')
    lastname.send_keys('leibovitz')
    time.sleep(2)

    city = driver.find_element(By.XPATH, '/html/body/form/fieldset/select[1]')
    city.click()
    
    cityname = driver.find_element(By.ID, 'JE')
    cityname.click()
    time.sleep(2)

    email = driver.find_element(By.XPATH, '/html/body/form/fieldset/input[3]')
    email.send_keys('lol10@gmail.com')
    time.sleep(2)

    mobile = driver.find_element(By.XPATH, '/html/body/form/fieldset/select[2]')
    mobile.click()
    
    mobilenumber = driver.find_element(By.XPATH, '/html/body/form/fieldset/select[2]/option[2]')
    mobilenumber.click()
    time.sleep(2)

    phone = driver.find_element(By.ID, 'phone')
    phone.send_keys('0528112122')
    time.sleep(2)

    buttonmale = driver.find_element(By.ID, 'm')
    buttonmale.click()
    time.sleep(2)

    buttonmath = driver.find_element(By.XPATH, '/html/body/form/fieldset/input[6]')
    buttonmath.click()
    time.sleep(2)

    buttobiology = driver.find_element(By.XPATH, '/html/body/form/fieldset/input[7]')
    buttobiology.click()
    time.sleep(2)

    buttonclear = driver.find_element(By.ID, 'CB')
    buttonclear.click()
    time.sleep(2)


def test_alert(driver):
    text = driver.find_element(By.XPATH,'/html/body/fieldset[1]/button[1]')
    text.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.send_keys('QA Automation Project')
    time.sleep(2)
    alert.accept()
    

    
    buttonload = driver.find_element(By.XPATH, '/html/body/fieldset[1]/button[2]')
    buttonload.click()
    time.sleep(2)

def test_finish (driver):
    try:
        finish = driver.find_element(By.XPATH, '/html/body/fieldset[1]/button[2]')
        finish.click()
        time.sleep(2)
        finish_result = driver.find_element(By.ID,'startLoad')
        time.sleep(5)
        assert finish_result.text == 'Finish'

        linktext1 = driver.find_element(By.LINK_TEXT, 'Next Page')
        linktext1.click()
        time.sleep(2)

        buttonchange = driver.find_element(By.XPATH, '/html/body/button')
        buttonchange.click()
        time.sleep(2)

        title1 = driver.title
        assert title1=='Finish'
        time.sleep(2)
        driver.back()

        linktext2 = driver.find_element(By.LINK_TEXT, 'Windy')
        linktext2.click()
        time.sleep(2)
        driver.back()

        linktext3 = driver.find_element(By.LINK_TEXT, 'Tera Santa')
        linktext3.click()
        time.sleep(2)
        driver.back()


        linktext4 = driver.find_element(By.LINK_TEXT, 'Java Book')
        linktext4.click()
        time.sleep(2)
        driver.back()

        linktext5 = driver.find_element(By.LINK_TEXT, 'YouTube')
        linktext5.click()
        time.sleep(2)
        driver.back()





    except AssertionError:
        print('Assertio Eror')
    except Exception as e:
        print(e)

    

        



if __name__ == "__main__":
    service = ChromeService(executable_path=ChromeDriverManager().install()) 
    driver = webdriver.Chrome(service=service)
    driver.get('http://127.0.0.1:5500/QA%20automation/HTML_Project.html')
    driver.maximize_window()
    test_form(driver)
    print('test_alert')
    test_alert(driver)
    test_finish (driver)
    time.sleep(4)
    driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
listen=True
greet=False
result=time.localtime()
check=True
while check:
    result=time.localtime()
    print(result.tm_hour, result.tm_min)
    if result.tm_hour==8 and result.tm_min>30 or True:
        driver = webdriver.Chrome(executable_path=  'C:/Users/mirze/Downloads/chromedriver.exe')
        driver.get("https://ets.amu.edu.az/mod/bigbluebuttonbn/view.php?id=6358")
        element=driver.find_element_by_id('username')
        element.send_keys('your username here')
        element=driver.find_element_by_id('password')
        element.send_keys('your password here')
        driver.find_element_by_id('loginbtn').click()
        driver.find_element_by_id('join_button_input').click()
        driver.switch_to.window(driver.window_handles[-1])
        check=False
        myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/span/button[2]")))
        if listen:
            
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]").click()
        if greet:
            input=driver.find_element_by_id('message-input')
            input.send_keys('Salam')
            input.send_keys(Keys.RETURN)
        
    else:
        
        print('sleeping')
        time.sleep(60)
        print('sleep over')
print('done')

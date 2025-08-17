from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def getDrivers():
# set options to make brow  ing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    # options.add_experimental_option("disable-blink-features=AutomationControlled")
    options.add_argument("disable-blink-features=AutomationControlled")

    driver=webdriver.Chrome(options=options)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    return driver

def main():
    driver=getDrivers()
    driver.find_element(by= "id" ,value= "username").send_keys("student")
    driver.find_element(by= "id" ,value= "password").send_keys("Password123")
    time.sleep(2)
    driver.find_element(by= "id" ,value= "submit").click()
    print(driver.find_element(by= "xpath" ,value= "/html/body/div/div/section/div/div/article/div[1]/h1").text)
    print(driver.current_url)
    time.sleep(2)
    
main()
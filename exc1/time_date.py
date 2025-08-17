from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


def getDrivers():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.timeanddate.com/")
    return driver

# TODO 2025-08-17 Sunday 161020.txt
# TODO inside file => loaction, date, day, time, temprature
def main():
    driver=getDrivers() 
    location=driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/div/p[1]/a")
    location_text=location.text

    date=driver.find_element(
            By.XPATH,
            value="/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/div/p[1]/span[2]"
        ).text
    
    day=driver.find_element(
            By.XPATH,
            value="/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/div/p[1]/span[1]"
        ).text
    
    hours_min=driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/a/span[1]"
        ).text
    
    seconds=driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/a/span[2]/span"
        ).text
    
    location.click()
    time.sleep(2)
    temp=driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/main/article/section[2]/div[1]/div/div[1]/div"
    ).text

    date_split=date.split(" ")
    file_name=f"{date_split[2]}_{date_split[1]}_{date_split[0]}_{day}_{hours_min.replace(":", "")}{seconds}.txt"
    
    with open(file_name, "w") as f:
        f.write(
            f"Location: {location_text}\n"
            f"Date: {date_split[2]}-{date_split[1]}-{date_split[0]}\n"
            f"Day: {day}\n"
            f"Time: {hours_min}:{seconds}\n"
            f"Temperature: {temp.replace('&nbsp;', ' ')}"
        )
    print("✔️ File created successfully!",file_name)
    driver.quit()


for i in range(3):
    main()
    time.sleep(2)

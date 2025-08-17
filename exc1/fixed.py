from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_driver():
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

def main():
    driver = get_driver()
    location_elem = driver.find_element(
        By.XPATH,
        "/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/div/p[1]/a"
    )
    location_text = location_elem.text

    day = driver.find_element(
        By.XPATH,
        "/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/div/p[1]/span[1]"
    ).text

    date = driver.find_element(
        By.XPATH,
        "/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/div/p[1]/span[2]"
    ).text

    hours_min = driver.find_element(
        By.XPATH,
        "/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/a/span[1]"
    ).text

    seconds = driver.find_element(
        By.XPATH,
        "/html/body/div[5]/main/article/section/div[1]/section[1]/div/div/a/span[2]/span"
    ).text

    location_elem.click()
    time.sleep(2)

    # --- after navigation, get temperature ---
    temp = driver.find_element(
        By.XPATH,
        "/html/body/div[5]/main/article/section[2]/div[1]/div/div[1]/div"
    ).text

    date_split = date.split(" ")  # e.g., ['17', 'August', '2025']
    file_name = f"{date_split[2]}_{date_split[1]}_{date_split[0]}_{day}_{hours_min.replace(':','')}{seconds}.txt"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(
            f"Location: {location_text}\n"
            f"Date: {date_split[2]}-{date_split[1]}-{date_split[0]}\n"
            f"Day: {day}\n"
            f"Time: {hours_min}:{seconds}\n"
            f"Temperature: {temp.replace('&nbsp;', ' ')}"
        )

    print("✅ File created:", file_name)

    driver.quit()

for i in range(3):
    main()
    time.sleep(2)

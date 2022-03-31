from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\MAXMEDIA\\Desktop\\Python downloads\\Chromedriver\\chromedriver.exe")
URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(URL)

time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/a[1]").click()                 #accepts cookies
driver.find_element(By.ID, "prefsButton").click()                                   #click on options
driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div[3]/a[2]').click()         #clicks on import
textarea = driver.find_element(By.XPATH, '//*[@id="textareaPrompt"]')               #textarea

with open("save.txt") as file:
    save_code = file.read()

textarea.send_keys(f"{save_code}")
driver.find_element(By.XPATH, '//*[@id="promptOption0"]').click()
# TODO:2 make it open last save
# TODO:3 make it save save_code to file before closing the browser

count = 0
while True:
    big_cookie = driver.find_element(By.ID, "bigCookie").click()

    count += 1
    if count == 100:
        time.sleep(0.5)
        # products = driver.find_elements(By.CLASS_NAME, "unlocked")
        # products.reverse()
        #
        # for item in products: # TODO:1 it works but it would be nice if it buys the most expensive thing it can buy
        #     item.click()
            # Other element would receive the click: <div class="shimmer" alt="Golden cookie" style="left: 266px; top: 318px; width: 96px; height: 96px; background-image: url(&quot;img/goldCookie.png&quot;); background-position: 0px 0px; opacity: 0.919091; display: block; transform: rotate(-21.0784deg) scale(1.04003);"></div>
            #Todo:4 Handle exceptions for when golden cookie overlaps big cookie ^

        # prices = driver.find_elements(By.CSS_SELECTOR, ".enabled .price")
        # for item in prices:
        #     try:
        #         price = int(item.text)
        #     except:
        #         pass #find way to convert "1.4 million" into an int
        #     finally:
        #         print(price)
        #
        #     bank = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split()[0])
        #     print(bank)
        #
        #     if bank > price:
        #         print("Entered if bank >")
        #         driver.find_element(By.XPATH, f"//*[text()='{price}']").click()


        count = 0
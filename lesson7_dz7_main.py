from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.action_chains import ActionChains

import time

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)


driver.get("https://www.wildberries.ru/")

#input = driver.find_element(By.XPATH, "//input[@id='searchInput']")

time.sleep(2)
input = driver.find_element(By.ID, "searchInput")
input.send_keys("телевизор")
input.send_keys(Keys.ENTER)

time.sleep(2)

while True:
    wait = WebDriverWait(driver, 30)
#    cards = wait.until(EC.presence_of_all_element_located((By.XPATH, "//article[@id]")))

    cards = driver.find_elements(By.XPATH, "//article[@id]") #30
    print(len(cards))
    count = len(cards)
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(1)
    cards = driver.find_elements(By.XPATH, "//article[@id]")  # 30
    if len(cards) == count:
        break

#for card in cards:
#    price = card.find_element(By.CLASS_NAME, "product-card__middle-wrap").text
#    card.find_element(By.XPATH, "//div[@class='product-card__middle-wrap']")
#    name = card.find_element(By.XPATH, "./div".__getattribute__('product-card__name'))
#    url = card.find_element(By.XPATH, "./div".__getattribute__('href'))
    #print(price, name, url)

    # try:
    #     button = driver.find_element ( By.CLASS_NAME , "pagination-next pagination__next j-next-page" )
    #     actions = ActionChains(driver)
    #     actions.click(button).scroll_to_element(button).key_down(Keys.CONTROL)  #.key_down(Keys.C).key_up(Keys.CONTROL)  #.key_up(Keys.C)
    #     actions.perform()
    # except:
    #     break

print()
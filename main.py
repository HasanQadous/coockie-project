from selenium import webdriver
from selenium.webdriver.common.by import By
import time

is_true = True

timeout = time.time() + 5
five_min = time.time() + 60*5

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

cookie = driver.find_element(By.ID, "cookie")

while is_true:
    cookie.click()

    if time.time() > timeout:
        store_elements = driver.find_elements(By.CSS_SELECTOR, "#store b")
        all_prices = []
        for item in store_elements:
            item_text = item.text
            if item_text != "":
                cost = int(item_text.split("-")[1].strip().replace(",", ""))
                all_prices.append(cost)

        cookie_upgrade = {}
        for n in range(len(all_prices)):
            cookie_upgrade[all_prices[n]] = item_ids[n]

        my_money = driver.find_element(By.ID, "money").text
        if "," in my_money:
            money_element = my_money.replace(",", "")
        cookie_count = int(my_money)
        print(cookie_count)

        aff_items = {}
        for cost, Id in cookie_upgrade.items():
            if cookie_count > cost:
                aff_items[cost] = Id

        try:
            highest_powerUP_cost = max(aff_items)
            print(highest_powerUP_cost)
            highest_powerUP_id = aff_items[highest_powerUP_cost]
            driver.find_element(By.ID, f"{highest_powerUP_id}").click()
        except ValueError:
            pass

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        is_true = False

driver.quit()
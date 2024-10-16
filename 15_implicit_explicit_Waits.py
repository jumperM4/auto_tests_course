import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    btn = browser.find_element(By.ID, "book")
    btn.click()

    x_element = browser.find_element(By.ID, "input_value")
    x_num = x_element.text
    res = calc(x_num)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(res)

    button = browser.find_element(By.ID, "solve")
    button.click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()


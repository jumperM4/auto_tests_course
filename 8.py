from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    print(input.get_attribute("checked"))
    input.send_keys(y)

    # checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    # checkbox.click()
    #
    # radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    # radiobtn.click()
    #
    # submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


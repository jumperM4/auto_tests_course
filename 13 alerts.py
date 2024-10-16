from selenium import webdriver
from selenium.webdriver.common.by import By
import  time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x_num = x_element.text
    res = calc(x_num)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(res)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()


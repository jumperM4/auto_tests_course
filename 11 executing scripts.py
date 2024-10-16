from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x_num = x_element.text
res = calc(x_num)

button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
browser.execute_script("window.scrollBy(0, 100);")

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(res)

checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
checkbox.click()

radio_btn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
radio_btn.click()

button.click()
time.sleep(5)

# browser = webdriver.Chrome()
# # browser.execute_script("alert('Robots at work');")
# # time.sleep(5)
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# time.sleep(5)

# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
#
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# time.sleep(3)


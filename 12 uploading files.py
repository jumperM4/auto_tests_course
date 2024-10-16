from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

field1 = browser.find_element(By.NAME, "firstname")
field1.send_keys("Ivan")

field1 = browser.find_element(By.NAME, "lastname")
field1.send_keys("Ivanov")

field1 = browser.find_element(By.NAME, "email")
field1.send_keys("ivan@yms.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'fil.txt')
choose_file = browser.find_element(By.ID, "file")
choose_file.send_keys(file_path)

submit_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_btn.click()

time.sleep(5)


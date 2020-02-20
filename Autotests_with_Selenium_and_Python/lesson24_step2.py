from selenium import webdriver
import time


time_sleep_fix = False
implicit_fix = True


# browser.implicitly_wait(5) - проверка искомого жлемента будет происходить каждые 500 мс в течении 5 секунд


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
if time_sleep_fix:
    time.sleep(1)
if implicit_fix:
    browser.implicitly_wait(5)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time



def click_submit_button():
    submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit_button.click()


def fill_form(input_value):
    browser.find_element_by_css_selector('input#answer.form-control').send_keys(input_value)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def get_value_element_value_and_calc_func():
    x = browser.find_element_by_css_selector('span#input_value.nowrap').text
    y = calc(x)
    return y


def click_button_book():
    button_book = browser.find_element_by_css_selector('button#book.btn.btn-primary')
    button_book.click()


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# button = browser.find_element_by_css("h5#price")
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(By.CSS_SELECTOR, 'h5#price'))
click_button_book()


#button.click()
#message = browser.find_element_by_id("verify_message")
#button.click()
#message = browser.find_element_by_id("verify_message")
#assert "successful" in message.text
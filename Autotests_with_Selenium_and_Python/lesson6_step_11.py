

from selenium import webdriver
import time
from Autotests_with_Selenium_and_Python.settings import chrome_driver_bin_path

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path=chrome_driver_bin_path)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    required_css_selectors_list = ['input[placeholder="Input your name"]',
                         'input[placeholder="Input your last name"]',
                         'input[placeholder="Input your email"]']

    for css_selector in required_css_selectors_list:
        element = browser.find_element_by_css_selector(css_selector)
        element.send_keys("text_sample")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
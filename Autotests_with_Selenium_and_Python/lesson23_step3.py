from selenium import webdriver
import time,math


link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def get_value_element_value_and_calc_func():
    x = browser.find_element_by_css_selector('span#input_value.nowrap').text
    y = calc(x)
    return y


def click_submit_button():
    submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit_button.click()


def fill_form(input_value):
    browser.find_element_by_css_selector('input#answer.form-control').send_keys(input_value)


def close_alert_window():
    alert = browser.switch_to_alert()
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать кнопку
    browser.find_element_by_css_selector('button.btn.btn-primary').click()
    close_alert_window()
    ans = get_value_element_value_and_calc_func()
    fill_form(ans)
    click_submit_button()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
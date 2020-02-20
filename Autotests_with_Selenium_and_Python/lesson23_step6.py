from selenium import webdriver
import time, math


link = 'http://suninjuly.github.io/redirect_accept.html'


def click_trollface_button():
    submit_button = browser.find_element_by_css_selector('button.trollface.btn,btn-primary')
    submit_button.click()


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


def switch_to_new_window():
    # получаем спискок окон в браузере в формате списка
    browser_windows = browser.window_handles
    # переключаемся на новую вкладку
    browser.switch_to_window(browser_windows[1])


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать кнопку

    click_trollface_button()
    switch_to_new_window()
    answer = get_value_element_value_and_calc_func()
    fill_form(answer)
    click_submit_button()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
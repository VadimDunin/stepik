import time, math
from selenium import webdriver


checkbox_i_am_robot = 'div.form-check.form-check-custom > label.form-check-label'
radiobutton_robots_rule = 'div.form-check.form-radio-custom > label.form-check-label'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def get_value_element_value_and_calc_func():
    x = str(browser.find_element_by_css_selector('span#input_value.nowrap').text)
    y = calc(x)
    return y


def select_element_and_click_by_css(css_selector, click=False):
    element = browser.find_element_by_css_selector(css_selector)
    if click:
        element.click()
    return element


def click_checkbox_on_i_am_the_robot():
    select_element_and_click_by_css(checkbox_i_am_robot, click=True)


def click_radiobutton_robots_rule():
    select_element_and_click_by_css(radiobutton_robots_rule, click=True)


def put_answer_to_inputform(answer):
    element = browser.find_element_by_css_selector('input#answer.form-control')
    element.send_keys(answer)


def click_submit_button():
    submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit_button.click()


def scroll_page_to_bottom():
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...

    res = get_value_element_value_and_calc_func()
    put_answer_to_inputform(res)
    scroll_page_to_bottom()
    click_checkbox_on_i_am_the_robot()
    click_radiobutton_robots_rule()
    click_submit_button()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
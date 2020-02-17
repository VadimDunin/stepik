import time, math
from selenium import webdriver


checkbox_i_am_robot = 'div > input[class="check-input"]'
radiobutton_robots_rule = 'input#robotsRule.check-input'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def get_valuex_element_value():
    x = str(browser.find_element_by_css_selector('img#treasure').get_attribute('valuex'))
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
    element = browser.find_element_by_css_selector('input#answer')
    element.send_keys(answer)


def click_submit_button():
    submit_button = browser.find_element_by_css_selector("button.btn.btn-default")
    submit_button.click()


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...

    value_x = get_valuex_element_value()
    put_answer_to_inputform(value_x)
    click_checkbox_on_i_am_the_robot()
    click_radiobutton_robots_rule()
    click_submit_button()

    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
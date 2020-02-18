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


def get_values_sum():
    value1 = browser.find_element_by_css_selector('span#num1.nowrap').text
    value2 = browser.find_element_by_css_selector('span#num2.nowrap').text
    res = int(value1) + int(value2)
    print(str(res))
    return str(res)


def push_dropdown_list():
    dropdown_list = browser.find_element_by_css_selector('select#dropdown.custom-select')
    dropdown_list.click()
    return dropdown_list


def get_dropdown_list_avalable_values(dropdown_list=None):
    if dropdown_list is None:
        dropdown_list = browser.find_element_by_css_selector('select#dropdown.custom-select')
        dropdown_list.click()
    elements = browser.find_elements_by_css_selector('option')
    return elements


def find_match_value(elements, sum):
    match_element = None
    for element in elements:
        value = element.get_attribute('value')
        if str(value) == str(sum):
            match_element = element
    print(match_element)
    print(value)
    return match_element, value


def click_on_match_element(element, dropdown_list):
    if dropdown_list is None:
        dropdown_list = browser.find_element_by_css_selector('select#dropdown.custom-select')
        dropdown_list.click()
    element.click()


try:
    link = "http://suninjuly.github.io/selects1.html"
    link2 = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    ...

    summa = get_values_sum()
    dropdown_list = push_dropdown_list()
    list_elements = get_dropdown_list_avalable_values(dropdown_list)
    web_element, value = find_match_value(list_elements, summa)
    click_on_match_element(web_element, dropdown_list)
    click_submit_button()

    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
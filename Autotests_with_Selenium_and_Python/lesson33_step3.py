# -*- coding: utf-8
from selenium import webdriver
from settings import chrome_driver_bin_path
import time, pytest



link_on_reg_form1 = "http://suninjuly.github.io/registration1.html"
required_css_selectors_list1 = ['input[placeholder="Input your first name"]',
                                   'input[placeholder="Input your last name"]',
                                   'input[placeholder="Input your email"]']


link_on_reg_form2 = "http://suninjuly.github.io/registration2.html"
required_css_selectors_list2 = ['input[placeholder="Input your name"]',
                                'input[placeholder="Input your last name"]',
                                     'input[placeholder="Input your email"]']

def check_sucsessfull_registration(self, browser):
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


def push_submit_button(browser):
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def fill_form_wrong_solution(browser, css_list):

    for css_selector in css_list:
        element = browser.find_element_by_css_selector(css_selector)
        element.send_keys("text_sample")


def open_main_page(link):
    browser = webdriver.Chrome(executable_path=chrome_driver_bin_path)
    browser.get(link)
    return browser


@pytest.fixture()
def resource_setup(request):
    browser = open_main_page()

    def resource_teardown():
        browser.quit()
    request.addfinalizer(resource_teardown)


def test_registration1(resource_setup):
    browser = open_main_page(link_on_reg_form1)
    fill_form_wrong_solution(browser, required_css_selectors_list1)
    push_submit_button(browser)
    time.sleep(1)
    check_sucsessfull_registration(browser)
    time.sleep(10)
    browser.quit()


def test_registration2():
    browser = open_main_page(link_on_reg_form2)
    fill_form_wrong_solution(browser, required_css_selectors_list2)
    push_submit_button(browser)
    time.sleep(1)
    check_sucsessfull_registration(browser)
    time.sleep(10)
    browser.quit()

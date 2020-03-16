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


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=chrome_driver_bin_path)
        self.wd.implicitly_wait(60)

    def open_page(self, link):
        wd = self.wd
        wd.get(link)

    def destroy(self):
        self.wd.quit()

    def check_successfull_registration(self):
        welcome_text_elt = self.wd.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    def push_submit_button(self):
        button = self.wd.find_element_by_css_selector("button.btn")
        button.click()

    def fill_form_wrong_solution(self, css_list):
        for css_selector in css_list:
            element = self.wd.find_element_by_css_selector(css_selector)
            element.send_keys("text_sample")


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_registration1(app):
    app.open_page(link_on_reg_form1)
    app.fill_form_wrong_solution(required_css_selectors_list1)
    app.push_submit_button()
    time.sleep(1)
    app.check_successfull_registration()
    time.sleep(10)
    app.destroy()


# по заданию в степике - второй тест должен отваливаится
def test_registration2(app):
    app.open_page(link_on_reg_form1)
    app.fill_form_wrong_solution(required_css_selectors_list2)
    app.push_submit_button()
    time.sleep(1)
    app.check_successfull_registration()
    time.sleep(10)
    app.destroy()

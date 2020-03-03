# -*- coding: utf-8
from selenium import webdriver
from settings import chrome_driver_bin_path
import time, unittest


class TestAbs(unittest.TestCase):
    # def test_abs1(self):
    #     self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
    #
    # def test_abs2(self):
    #     self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
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

    def push_submit_button(self, browser):
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    def fill_form_wrong_solution(self, browser, css_list):

        for css_selector in css_list:
            element = browser.find_element_by_css_selector(css_selector)
            element.send_keys("text_sample")

    def open_main_page(self, link):
        browser = webdriver.Chrome(executable_path=chrome_driver_bin_path)
        browser.get(link)
        return browser

    def test_registration1(self):
        #try:
        browser = self.open_main_page(self.link_on_reg_form1)

        # Ваш код, который заполняет обязательные поля
        self.fill_form_wrong_solution(browser, self.required_css_selectors_list1)
        # Отправляем заполненную форму
        self.push_submit_button(browser)
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        self.check_sucsessfull_registration(browser)

        #finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        try:
            browser = self.open_main_page(self.link_on_reg_form2)

            # Ваш код, который заполняет обязательные поля
            self.fill_form_wrong_solution(browser, self.required_css_selectors_list2)
            # Отправляем заполненную форму
            self.push_submit_button(browser)
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            self.check_sucsessfull_registration(browser)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()

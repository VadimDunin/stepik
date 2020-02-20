from selenium import webdriver
import time,os


link = 'http://suninjuly.github.io/file_input.html'

input_data = ['first_name',
            'second_name',
            'email@email.com']

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


def click_submit_button():
    submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit_button.click()


def fill_form():
    control_form_elements = browser.find_elements_by_css_selector('input.form-control')
    for element in control_form_elements:
        element.send_keys('test')


def upload_file(file_path):
    upload_button = browser.find_element_by_css_selector('input#file')
    upload_button.send_keys(file_path)


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fill_form()
    upload_file(file_path)
    click_submit_button()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
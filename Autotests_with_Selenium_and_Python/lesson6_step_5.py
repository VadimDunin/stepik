from selenium import webdriver
import time, math


link = "http://suninjuly.github.io/find_link_text"

# Примечание - локатор, передаваемый в метод отличается от используемого в HTML странице
# .form-control.city - работает в браузере
# form-control.city - работае в селениуме

aref = str(math.ceil(math.pow(math.pi, math.e)*10000))

value1 = "input"
value2 = "last_name"
value3 = "form-control.city"
value4 = 'country'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element_by_link_text(aref)
    link.click()

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
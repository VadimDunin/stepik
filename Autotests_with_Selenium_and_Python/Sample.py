# import math
# fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
# print(fun(5))
chrome_driver_path = "/usr/bin/chromedriver"
TestPageURL = "http://suninjuly.github.io/simple_form_find_task.html"


code_1 = False
code_2 = False
code_3 = False
code_4 = False
code_5 = False
code_6 = True

if code_1:
    from selenium import webdriver

    browser = webdriver.Chrome(executable_path=chrome_driver_path)
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element_by_id("submit")

if code_2:
    from selenium import webdriver

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element_by_id("submit_button")

if code_3:
    from selenium import webdriver

    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element(By.ID, "submit_button")

if code_4:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

    # закрываем браузер после всех манипуляций
    browser.quit()

if code_5:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        button = browser.find_element(By.ID, "submit")
        button.click()

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

if code_6:
    from selenium import webdriver
    import time

    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

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
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла
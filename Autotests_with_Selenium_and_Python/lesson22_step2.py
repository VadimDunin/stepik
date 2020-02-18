from selenium import webdriver
from selenium.webdriver.support.ui import Select


link1='http://suninjuly.github.io/selects1.html'
link2='http://suninjuly.github.io/selects2.html'


browser = webdriver.Chrome()
browser.get(link1)
#browser.get(link2)

browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()
browser.find_element_by_css_selector("[value='1']").click()


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
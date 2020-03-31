import pytest, time, math
from selenium import webdriver

# launch: pytest -s -v lesson36_step3.py

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()


params = ["236895","236896","236897","236898","236899","236903","236904","236905"]


def click_submission_button():
    browser.browser.find_element_by_css_selector('button.submit-submission').click()


@pytest.mark.parametrize('number', params)
def test_open_pages(browser, number):
    link = "https://stepik.org/lesson/{}/step/1".format(number)
    browser.get(link)
    time.sleep(15)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('textarea').sendkeys(str(answer))
    click_submission_button()


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# class TestLogin(object):
#     def test_guest_should_see_login_link(self, browser, language):
#         link = "http://selenium1py.pythonanywhere.com/{}/".format("language")
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_navbar_element(self, browser, language):
#         pass

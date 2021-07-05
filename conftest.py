import pytest
from selenium import webdriver


def pytest_addoption(parser):
 	parser.addoption('--language', action='store', default=None, 
 		help="Choose locale to run test.")



@pytest.fixture(scope="function")
def language(lang):
    locale = lang.config.getoption("language")
    


# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
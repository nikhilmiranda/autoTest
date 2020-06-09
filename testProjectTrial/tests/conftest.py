import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser='firefox'):
    print("Running oneTimeSetup")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    # if browser == 'firefox':
    # #     baseURL = "https://pim.unbxd.com/"
    # #     driver = webdriver.Firefox(executable_path=r"D:\geckodriver.exe")
    # #     driver.maximize_window()
    # #     driver.implicitly_wait(3)
    # #     driver.get(baseURL)
    # #     print("Running tests on FF")
    # #
    # # else:
    # baseURL = "https://pim.unbxd.com/"
    # driver = webdriver.Chrome(r"D:\chromedriver_win_83.exe")
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    # driver.get(baseURL)
    # print("Running tests on Chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time TearDOwn")

from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clearEmailFieldDetails()
        self.lp.clearPasswordFieldDetails()
        self.lp.login("nikhil.miranda+40@unbxd.com", "greenday")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Page Title is Incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("Test_ValidLogin", result2, "Login Failed")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("nikhil.miranda+40@unbxd.com", "anyIncorrectPassword")
        result = self.lp.verifyLoginFailed()
        assert result == True

import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # --- Locators By Elements --- #
    _emailField_Xpath_ = "//div[@id='app']//div[contains(@class,'front')]//input[contains(@name,'userEmail')]"
    _passwordField_Xpath_ = "//input[contains(@placeholder,'Enter Password')]"
    _loginButton_Xpath_ = "//button[contains(text(),'Log In')]"
    _accountIcon_Xpath_ = "//div[@id='app']//span[@class='sprite user-icon']"

    # --- Get UNIQUE Fields --- #
    # def getEmailField(self):
    #     return self.driver.find_element(By.XPATH, self._emailField_Xpath_)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.XPATH, self._passwordField_Xpath_)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.XPATH, self._loginButton_Xpath_)

    # --- Perform UNIQUE Actions -------------------------------------------------- #
    def enterEmailDetails(self, email):
        self.sendKeys(email,self._emailField_Xpath_, locatorType = "xpath")

    def enterPasswordDetails(self, password):
        self.sendKeys(password,self._passwordField_Xpath_, locatorType = "xpath")

    def clickLoginButton(self):
        self.elementClick(self._loginButton_Xpath_, locatorType = "xpath")
    # ----------------------------------------------------------------------------- #

    def clearEmailFieldDetails(self):
        self.clearField(self._emailField_Xpath_,"xpath")

    def clearPasswordFieldDetails(self):
        self.clearField(self._passwordField_Xpath_,"xpath")

    # --- Perform GROUPED Actions --- #
    def login(self, email="", password=""):
        self.enterEmailDetails(email)
        self.enterPasswordDetails(password)
        time.sleep(1)
        self.clickLoginButton()
        time.sleep(1)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@id='app']//span[@class='sprite user-icon']",locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@id='app']//div[contains(@class,'front')]//div[contains(@class,'message-box error')]", locatorType="xpath")
        return result

    def incorrectLogin(self,email,):
        self.enterEmailDetails(email)
        self.enterPasswordDetails("password")
        self.clickLoginButton()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Unbxd PIM")
        # if "Unbxd PIN" in self.getTitle():
        #     return True
        # else:
        #     return False



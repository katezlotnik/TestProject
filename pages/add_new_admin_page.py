import time

import allure
from base.basepage import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class AddNewAdminPage(BasePage):

    PAGE_URL = Links.ADD_USER_PAGE

    USER_ROLE_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
    DROPDOWN_ITEM1 = ("xpath", "//div[@class='oxd-select-option']/span[text()='Admin']")  # this locator is useful when drop-dow option wrapped
    # by span inside div
    STATUS_DROPDOWN = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
    DROPDOWN_ITEM2 = ("xpath", "//div[@class='oxd-select-option']/span[text()='Enabled']")
    EMPLOYEE_NAME = ("xpath", "//input[@placeholder='Type for hints...']")
    #//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']
    USERNAME = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    PASSWORD = ("xpath", "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD = ("xpath", "(//input[@type='password'])[2]")
    SAVE_BTN = ("xpath", "//button[@type='submit']")
    # SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")
    SUCCESS_MESSAGE = ("xpath", "//div[@class='oxd-toast-start']")


    def select_user_role(self):
        user_role_dropdown = self.wait.until(EC.element_to_be_clickable(self.USER_ROLE_DROPDOWN))
        user_role_dropdown.click()
        time.sleep(2)
        dropdown_item1 = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_ITEM1))
        # self.driver.execute_script("arguments[0].click();", dropdown_item1)
        dropdown_item1.click()
        time.sleep(2)

    def select_employee_name(self):
        employee_name = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME))
        employee_name.click()
        employee_name.send_keys("butler")
        time.sleep(2)
        employee_name.send_keys(Keys.DOWN)
        employee_name.send_keys(Keys.ENTER)
        time.sleep(2)

    def select_status(self):
        status_dropdown = self.wait.until(EC.element_to_be_clickable(self.STATUS_DROPDOWN))
        status_dropdown.click()
        time.sleep(2)
        dropdown_item2 = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_ITEM2))
        dropdown_item2.click()
        time.sleep(2)

    def enter_username(self):
        username = self.wait.until(EC.element_to_be_clickable(self.USERNAME))
        username.send_keys("JamesButler")

    def enter_password(self):
        password = self.wait.until(EC.element_to_be_clickable(self.PASSWORD))
        password.send_keys("Password1!")

    def confirm_password(self):
        same_password = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD))
        same_password.send_keys("Password1!")

    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    def is_user_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))









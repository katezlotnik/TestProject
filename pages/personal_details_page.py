import time

import allure
from base.basepage import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
class PersonalDetailsPage(BasePage):

    PAGE_URL = Links.MYINFO_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BTN = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            # first_name_field.clear() - it doesn't work for some reason
            # time.sleep(3) # this is used for debugging
            first_name_field.send_keys(Keys.COMMAND + "A")
            first_name_field.send_keys(Keys.BACKSPACE) # is used instead clear method
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    @allure.step("Changes have been saved successfully")
    def is_change_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))



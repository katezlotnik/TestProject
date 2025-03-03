import allure
from allure_commons.types import AttachmentType
from base.basepage import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
class PersonalDetailsPage(BasePage):

    PAGE_URL = Links.MYINFO_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BTN = ("xpath", "(//button[@type='submit'])[1]")

    def change_name(self, new_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
        first_name_field.clear()
        assert first_name_field.get_attribute("value") == "", "Text still exist"
        first_name_field.send_keys(new_name)
        self.name = new_name

    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    def is_change_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

    #def create_screenshot(self, screenshot_name):
    #    allure.attach(
    #        body=self.driver.get_screenshot_as_png(),
    #        name=screenshot_name,
    #       attachment_type=AttachmentType.PNG
    #    )
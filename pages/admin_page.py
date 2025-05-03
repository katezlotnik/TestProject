import time

import allure
from base.basepage import BasePage
from base.scrolls import Scroll
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException

class AdminPage(BasePage):
    PAGE_URL = Links.ADMIN_PAGE

    ADD_BTN = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    USER_TABLE = ("xpath", "//div[@class='oxd-table']")
    # CHECKBOX = ("xpath", "//i[@class='oxd-icon bi-dash oxd-checkbox-input-icon']")
    CHECKBOX = ("xpath", "//span[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']")
    DELETE_SELECTED_BTN = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")
    DELETE_BTN1 = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
    USER_LOCATOR = ("xpath", "//div[@class='oxd-table']//div[text()='JamesButler']")
    # USER_ROW = ("xpath", f"//div[@class='oxd-table-card']//div[text()='JamesButler']/ancestor::div[@class='oxd-table-card']")
    # DELETE_BTN = ("xpath", "//button[i[contains(@class, 'bi-trash')]]")
    YES_DELETE_BTN = ("xpath", "//button[contains(@class, 'oxd-button--label-danger') and contains(., 'Yes, Delete')]")

    @allure.step("Click Add Button")
    def click_add_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()

    def is_user_added(self):
        action = ActionChains(self.driver)
        self.wait.until(EC.visibility_of_element_located(self.USER_TABLE))
        employee_name = self.wait.until(EC.visibility_of_element_located(self.USER_LOCATOR))
        action.scroll_to_element(employee_name).perform()

    def select_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX)).click()

    def click_delete_selected_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_SELECTED_BTN)).click()
    def click_yes_delete_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_BTN1)).click()

    def delete_user_by_username(self, username):
        action = ActionChains(self.driver)
        scroll = Scroll(self.driver, action)
        user_row = self.wait.until(EC.presence_of_element_located((
            "xpath",
            f"//div[@class='oxd-table-card']//div[text()='{username}']/ancestor::div[@class='oxd-table-card']"
        )))
        scroll.scroll_to_element(user_row)
        delete_btn = user_row.find_element("xpath", ".//button[i[contains(@class, 'bi-trash')]]")
        delete_btn.click()
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.YES_DELETE_BTN))
        confirm_btn.click()

    def is_user_removed(self, username):
        user_row_locator = (
            "xpath",
            f"//div[@class='oxd-table-card']//div[text()='{username}']/ancestor::div[@class='oxd-table-card']"
        )
        try:
            self.wait.until(EC.presence_of_element_located(user_row_locator))
            return False  # Found → not removed
        except TimeoutException:
            return True  # Not found → removed


import allure
import random
import pytest
from base.base_test import BaseTest

@allure.feature("Admin Functionality")
class TestAdminFunctionality(BaseTest):

    @allure.title("Add New Admin")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_new_admin(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_btn()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_admin_btn()
        self.admin_page.is_opened()
        self.admin_page.click_add_btn()
        self.add_new_admin_page.is_opened()
        self.add_new_admin_page.select_user_role()
        self.add_new_admin_page.select_employee_name()
        self.add_new_admin_page.select_status()
        self.add_new_admin_page.enter_username()
        self.add_new_admin_page.enter_password()
        self.add_new_admin_page.confirm_password()
        self.add_new_admin_page.save_changes()
        self.add_new_admin_page.is_user_saved()
        self.admin_page.is_user_added()
        self.admin_page.make_screenshot("Success")

# test failed because of drop-downs

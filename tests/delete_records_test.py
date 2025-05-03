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
        self.admin_page.select_checkbox()
        self.admin_page.click_delete_selected_button()
        self.admin_page.click_yes_delete_button()
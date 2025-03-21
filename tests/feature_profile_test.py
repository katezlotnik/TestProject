import allure
import random
import pytest
from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_btn()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_myinfo_btn()
        self.personal_details_page.is_opened()
        self.personal_details_page.change_name(f"Test {random.randint(1, 100)}")
        self.personal_details_page.save_changes()
        self.personal_details_page.is_change_saved()
        self.personal_details_page.make_screenshot("Success")




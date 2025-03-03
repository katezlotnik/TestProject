import random

from base.base_test import BaseTest

class ProfileFeatureTest(BaseTest):

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




import pytest
from base.base_test import BaseTest

class TestRemoveNewAdmin(BaseTest):
    def test_remove_admin(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_btn()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_admin_btn()
        self.admin_page.is_opened()
        self.admin_page.is_user_added()
        username = "JamesButler"
        self.admin_page.delete_user_by_username(username)
        assert self.admin_page.is_user_removed(username)


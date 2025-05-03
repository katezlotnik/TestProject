import pytest

from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_details_page import PersonalDetailsPage
from pages.admin_page import AdminPage
from pages.add_new_admin_page import AddNewAdminPage

class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_details_page: PersonalDetailsPage
    admin_page: AdminPage
    add_new_admin_page: AddNewAdminPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_details_page = PersonalDetailsPage(driver)
        request.cls.admin_page = AdminPage(driver)
        request.cls.add_new_admin_page = AddNewAdminPage(driver)
# this class and fixture give us multipage access
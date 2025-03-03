from base.basepage import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MYINFO_BTN = ("xpath", "//span[text()='My Info']")

    def click_myinfo_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.MYINFO_BTN)).click()

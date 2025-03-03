from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self): # this method opens page
        self.driver.get(self.PAGE_URL) # PAGE_URL will be written for every page

    def is_opened(self): # this method checks if page is opened
        # it's like built-in assert in every method of every page
        self.wait.until(EC.url_to_be(self.PAGE_URL))
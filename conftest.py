import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# fixture driver to create object driver inside pages, requests
@pytest.fixture(scope="function", autouse=True) # fixture will be used automatically for every test,
# no need to call it. fixture will create driver instance (to open browser) for every test separately
def driver(request):
    options = Options()
    #options.add_argument("--headless") # # Run without opening a UI browser
    options.add_argument("--no-sandbox") # # Bypass security restrictions in Docker
    # this option allows project to run in no-interface env
    options.add_argument("--disable-dev-shm-usage") # used when running Google Chrome (or Chromium)
    # with Selenium in Docker, Linux servers, or CI/CD pipelines to prevent crashes due to limited shared memory.
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    # this construction creates object 'driver' inside test classes. this is the same when add 'driver'
    # as argument in __init__ function of test class
    yield driver # Provide the WebDriver instance to the test
    driver.quit() # Cleanup: Close browser after test


